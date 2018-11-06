#coding=utf-8

'''
	Some important operations before training the model, including sample operation, batch operation and so on.

	Implemente sample(including undersample and oversample) operatiion and batch operatiion.

'''

import pandas as pd
import numpy as np


def data_iterator(orig_X, orig_label=None, batch_size=10, shuffle=False, is_normalize=False):
    '''
    	得到根据batch_size, 得到每个batch 
    :param orig_X:
    :param orig_y:
    :param orig_label:
    :param batch_size:
    :param shuffle:
    :return:
    '''
    # Optionally shuffle the data before training
    if shuffle:
        indices = np.random.permutation(orig_X.shape[0])
        data_X = orig_X[indices]
        data_label = orig_label[indices]
    else:
        data_X = orig_X
        data_label = orig_label
    ###
    total_processed_examples = 0
    total_steps = int(np.ceil(data_X.shape[0] / float(batch_size)))
    for step in xrange(total_steps):
        # Create the batch by selecting up to batch_size elements
        batch_start = step * batch_size
        x = data_X[batch_start : batch_start + batch_size]
        y = data_y[batch_start : batch_start + batch_size]
        label = orig_label[batch_start : batch_start + batch_size]
       
        if is_normalize:
            yield normalize(x, axis=0), label
        else:
            yield x, label
        total_processed_examples += x.shape[0]
    # Sanity check to make sure we iterated over all the dataset as intended
    assert total_processed_examples == data_X.shape[0], 'Expected {} and processed {}'.format(data_X.shape[0], total_processed_examples)


def sample(x, p=0.025, col='y'):
    '''
    	上采样或者下采样, 根据正样本比例来
    :param p, 采样过后正样本的比例
    :param col, 按照哪一列确定正样本比例
    :param x, DataFrame类型, 原始数据
    '''

    pos = x[x[col] == 1]
    neg = x[x[col] == 0]
    pos_len = len(pos)
    neg_len = len(neg)
    
    pos_rate = pos_len*1.0/(neg_len+pos_len)
    print 'Before sample pos_rate: ', pos_rate
    
    if pos_rate > p:
        add = int(pos_len*1.0 / p - pos_len - neg_len)
        print 'oversample of neg samples %d / %d . ' % (add+neg_len, neg_len)
        neg = pd.concat([neg, neg.iloc[np.random.randint(0, neg_len, size=(add, ))]], axis=0)
    else:
        add = int(pos_len * 1.0 / p - pos_len)
        print 'undersample of neg samples %d / %d . ' % (add, neg_len)
        neg = neg.iloc[np.random.randint(0, neg_len, size=(add, ))]
    
    pos_rate = pos_len*1.0/(len(neg)+pos_len)
    print 'After sample pos_rate: ', pos_rate
    return pd.concat([pos, neg], axis=0)


if __name__ == '__main__':
	print produce_value_day_range(['1', '2', '3'], ['2015-01-01', '2015-01-02', '2015-01-03'])

