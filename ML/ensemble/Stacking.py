#coding=utf-8

'''
	最基本的Stacking, 先把训练集分成n折, 用任意n-1折训练layer_1的模型, 
	layer_1层模型对最后一折预测, 把所有的预测拼起来作为layer_2的特征, layer_2模型在这些特征上训练,
	layer_1的模型对验证集进行预测, 作为layer_2模型在验证集上特征, layer_2模型在验证集上的预测结果
	作为最终的预测结果
'''

'''
    Stacking and Blending
    读取数据
    以JD_2017比赛为例子 (http://www.datafountain.cn/#/competitions/247/intro/)
'''
import pandas as pd
import numpy as np
import os
from sklearn.datasets import load_svmlight_files

'''
	加载数据
'''
fe_dir = 'xgb_feature_pool'
fe_file = 'selected_feature.csv'
train_date = '2016-04-06'
valid_date = '2016-04-10'
test_date = '2016-04-16'

train_data = pd.read_csv(os.path.join(fe_dir, train_date, fe_file))
valid_data = pd.read_csv(os.path.join(fe_dir, valid_date, fe_file))
test_data = pd.read_csv(os.path.join(fe_dir, test_date, fe_file))


train_sparse_file = 'XGB输出的稀疏特征/v3.train.svm'
valid_sparse_file = 'XGB输出的稀疏特征/v3.valid.svm'
X_train_sparse, _, X_valid_sparse, _ = load_svmlight_files([train_sparse_file, valid_sparse_file])

valid_data_9 = pd.read_csv(os.path.join(fe_dir, '2016-04-09', fe_file))
valid_data_11 = pd.read_csv(os.path.join(fe_dir, '2016-04-11', fe_file))

train_data.fillna(-1, inplace=True)
valid_data.fillna(-1, inplace=True)
test_data.fillna(-1, inplace=True)
valid_data_9.fillna(-1, inplace=True)
valid_data_11.fillna(-1, inplace=True)

print 'Read done.'


'''
    得到交叉验证索引
'''
from sklearn.model_selection import KFold

test_data['y'] = 0
base_infos = ['user_id', 'cate', 'y']
cols = filter(lambda x: not x in base_infos, train_data.columns)
print 'cols: ', len(cols)

indices = [[] for _ in range(2)]

kf = KFold(n_splits=5, shuffle=True, random_state=0)

for train_0_index, train_1_index in kf.split(train_data.as_matrix()):
    indices[0].append(train_0_index)
    indices[1].append(train_1_index)
    
print 'Handle done.'


'''
    6号训练集 5折，然后4折用来给0 base learner训练，预测1折的结果给1 base learner
    
    layer one: XGB + LR + RF
    layer two: LR 
    
    效果不是很好
'''

import sys
sys.path.append('util')

from system import tools

reload(tools)
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from datetime import datetime

model_cnt = 0
XGBmodels = []
seeds = [0, 1000]
for one in seeds:
    for max_depth in [3]:
        for learning_rate in [0.05]:
            model_cnt += 1
            model = XGBClassifier(max_depth=max_depth, learning_rate=learning_rate, n_estimators=500, silent=True, \
                      objective='binary:logistic', nthread=-1, gamma=0, min_child_weight=1, \
                      max_delta_step=0, subsample=1, colsample_bytree=0.8, colsample_bylevel=0.8, \
                      reg_alpha=0, reg_lambda=1, scale_pos_weight=1, base_score=0.5, seed=one, missing=None)
            XGBmodels.append([model, 50, 5, 'xgb'+str(model_cnt)])
            model_cnt += 1
            XGBmodels.append([model, 20, 5, 'xgb'+str(model_cnt)])
            layer_2_valid['xgb_fe'] += model.predict_proba(valid_data[cols].as_matrix())[:, 0]
            
model_cnt += 1
model = RandomForestClassifier(n_estimators=500, criterion='entropy', max_depth=None, \
           min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, \
           max_features=0.2, max_leaf_nodes=None, min_impurity_split=1e-07, \
           bootstrap=True, oob_score=False, n_jobs=30, random_state=None, verbose=0, \
           warm_start=False, class_weight=None)
XGBmodels.append([model, 50, 5, 'rf'+str(model_cnt)])

LRmodels = []
seeds = [0]
Cs = [0.15]
tols = [0.0001]

model_cnt = 0
for one in seeds:
    for C in Cs:
        for tol in tols:
            model = LogisticRegression(penalty='l1', dual=False, tol=tol, C=C, fit_intercept=True, \
                                intercept_scaling=1, random_state=one, solver='liblinear', \
                                max_iter=300, multi_class='ovr', verbose=100, warm_start=False, n_jobs=-1)
            model_cnt += 1
            LRmodels.append([model, 20, 5, 'lr'+str(model_cnt)])

model2 = LogisticRegression(penalty='l1', dual=False, tol=0.0001, C=0.15, fit_intercept=True, \
                                intercept_scaling=1, random_state=0, solver='liblinear', \
                                max_iter=200, multi_class='ovr', verbose=100, warm_start=False, n_jobs=-1)


folds = range(5)
fes = [i[-1] for i in XGBmodels]
print fes
layer_2_train = None

stacking_train_data = train_data.copy()
layer_2_valid = valid_data.copy()
#stacking_train_sparse = sparse_6.copy()
#stacking_valid_sparse = sparse_11.copy()

for one_fe in fes:
    layer_2_valid[one_fe] = 1.0

for one_fold in folds:
    print 'start fold ', str(one_fold)
    indice_0 = indices[0][one_fold]
    indice_1 = indices[1][one_fold]

    print str(datetime.now())
    train_0 = stacking_train_data.iloc[indice_0]
    train_1 = stacking_train_data.iloc[indice_1]
    print 'Train_0 ', train_0.shape, ' y mean ', np.mean(train_0['y']), ' Train_1 ', \
        train_1.shape, ' y mean ', np.mean(train_1['y'])
    
    for model in XGBmodels:
        model[0].fit(train_0[cols].as_matrix(), train_0['y'].as_matrix(), \
                   sample_weight=np.array([weight(one, sample_weight=model[1], sample_weight_8=model[2]) \
                                  for one in train_0[['cate', 'y']].as_matrix()]))
        now_fe = model[-1]
        train_1[now_fe] = model[0].predict_proba(train_1[cols].as_matrix())[:, 0]
        
        layer_2_valid[now_fe] *= model[0].predict_proba(layer_2_valid[cols].as_matrix())[:, 0]
        
    print 'Layer one XGBs model done.'
    print str(datetime.now())
    
    for model in LRmodels:
        model[0].fit(stacking_train_sparse[indice_0], train_0['y'].as_matrix(), \
                   sample_weight=np.array([weight(one, sample_weight=model[1], sample_weight_8=model[2]) \
                                  for one in train_0[['cate', 'y']].as_matrix()]))
        now_fe = model[-1]
        train_1[now_fe] = model[0].predict_proba(stacking_train_sparse[indice_1])[:, 0]
        
        layer_2_valid[now_fe] += model[0].predict_proba(stacking_valid_sparse)[:, 0]
        
        
    print 'Layer one LR done.'
    print str(datetime.now())
    
    if layer_2_train is None:
        layer_2_train = train_1.copy()
    else:
        layer_2_train = pd.concat([layer_2_train, train_1], axis=0)
    
    print 'Valid in the fold ', str(one_fold), ' of 4'
    
    model2.fit(layer_2_train[fes].as_matrix(), layer_2_train['y'].as_matrix(), \
           sample_weight=[weight(one, sample_weight=1, sample_weight_8=1) \
                          for one in layer_2_train[['cate', 'y']].as_matrix()])
    temp_valid = layer_2_valid.copy()
    for one in fes:
        temp_valid[one] /= len(folds)*1.0
    layer_2_valid['fold'+str(one_fold)] = model2.predict_proba(layer_2_valid[fes].as_matrix())[:, 0]
    tools.calculate(layer_2_valid, 1254, by='fold' + str(one_fold))

    print '******'*10 + '\n\n'

for one in fes:
    layer_2_valid[one] /= len(folds)*1.0
    
print layer_2_train[fes].shape
model2.fit(layer_2_train[fes].as_matrix(), layer_2_train['y'].as_matrix(), \
           sample_weight=[weight(one, sample_weight=1, sample_weight_8=1) \
                          for one in layer_2_train[['cate', 'y']].as_matrix()])
print 'layer 2 fit done.'
print str(datetime.now())
layer_2_valid['pred'] = model2.predict_proba(layer_2_valid[fes].as_matrix())[:, 0]

print '**** XGB Valid '
for one in fes:
    print '****'*10, one
    tools.calculate(layer_2_valid, 1254, by=one)
    print '------'*10
print '......'*10+'\n'

print '**** Stacking Valid'
tools.calculate(layer_2_valid, 1254)
#del stacking_train_data, stacking_train_sparse, stacking_valid_sparse