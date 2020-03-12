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

4. 
  - resample, idxmax(0)
  

5. 将group之后的index重新拿出来
    - customers['Country'] = customers.index.get_level_values(1)
    
    
6. 分组可视化
    '''
    # creates the FaceGrid
    g = sns.FacetGrid(customers, col="Country")

    # map over a make a scatterplot
    g.map(plt.scatter, "Quantity", "UnitPrice", alpha=1)

    # adds legend
    g.add_legend()
    '''
    
7. pd.cut
    - buckets = np.arange(price_start,price_end,price_interval)
    - revenue_per_price = online_rt.groupby(pd.cut(online_rt.UnitPrice, buckets)).Revenue.sum()
    