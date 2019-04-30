1. loc / iloc slice
# iloc数字索引, loc名字索引(行名或者列名)
# df.iloc[:, :-3] 
# df.loc[['index'], [columns]]
# df.iloc[[0], df.columns.get_loc('column')]

# .loc is another way to slice, using the labels of the columns and indexes
df.loc[euro12.Team.isin(['England', 'Italy', 'Russia']), ['Team','Shooting Accuracy']]


2. groupby之后仍然是一个df
drinks.groupby('continent').agg(['mean', 'min', 'max'])

Exercise: Iterate over a group and print the name and the whole data from the regiment
# Group the dataframe by regiment, and for each regiment,
for name, group in regiment.groupby('regiment'):
    # print the name of the regiment
    print(name)
    # print the data of that regiment
    print(group)


3. Present the mean preTestScores grouped by regiment and company without heirarchical indexing¶
regiment.groupby(['regiment', 'company']).preTestScore.mean().unstack()

