## If you are an interviewer, what skill do you most expect your interviewee have ?
- Ownership 
- Don't hesitate to learn new things
- Skillful


## 题库：
- 最近公共父亲
    - <a, b> root->a, root->b  the last diff

- 判断是否是全二叉树
    - 用bfs， 并用一个变量记录下是否是非满的情况，如果是非满并且当前有孩子的话就不行
    
- 哈弗曼树
    - 树的带权路径长度规定为所有叶子结点的带权路径长度之和，记为WPL。
    - 给定n个权值作为n个叶子结点，构造一棵二叉树，若该树的带权路径长度达到最小，称这样的二叉树为最优二叉树，也称为哈夫曼树(Huffman Tree)。哈夫曼树是带权路径长度最短的树，权值较大的结点离根较近。

- 输出长度不超过n且旋转180度后和自己相同的数
    - 1 - 1
    - 6 - 9
    - 8 - 8
    - 9 - 6
    - 0 - 0
    - 数位dp

- 最长递增子序列
    - dp[i] = dp[j] + 1 (if save[j] < save[i]) 时间复杂度
    - follow up :  n log(n)  min[i] 表示长度为i时的最小递增序列, 优先队列
    
- 最大连续子序列
    - dp[i] = dp[j] + save[j+1 ~ i]


## 基础代码能力考察
- 字符串
    - 字符串拷贝函数
    - 


## 估计时间复杂度


## 大数据处理
- hadoop
    - 统计单词的个数？
- spark
    - repartition和coalesce的区别
    - 
- 数据分析
    - pandas
    - numpy


## 深度学习