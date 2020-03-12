1. loc / iloc slice
# iloc数字索引, loc名字索引(行名或者列名)
# df.iloc[:, :-3] 
# df.loc[['index'], [columns]]
# df.iloc[[0], df.columns.get_loc('column')]

# .loc is another way to slice, using the labels of the columns and indexes
df.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]



