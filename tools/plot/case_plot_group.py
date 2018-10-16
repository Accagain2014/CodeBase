'''
    分组统计，且将值标注在头上
'''

def degree_seg(x):
    floor = int(math.floor(x * 10))
    ceil = min(10, floor + 1)
    return "%d%%~%d%%" % (floor*10, ceil*10)

def basic_stat(df):
    df["degree_seg"] = df['v_watch_degree'].map(degree_seg)
    ax = df.groupby(['degree_seg']).count()['vid'].plot(kind="bar", grid=True)
    for p in ax.patches:
        ax.annotate(str(p.get_height()), (p.get_x()*.99, p.get_height() * 1.02))
    plt.show()