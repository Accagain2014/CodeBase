
### collection of common regular expression
1. 查找《》的节目名字
    - re.findall(r'《(.+?)》', text)
    
2.


### Functions

def function_1():
    '''
        将第一季变成1
    '''
    have_s = set() 
    d_map = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9, "十": 10, "十一": 11
    , "十二": 12, "十三": 13, "十四": 14, "十五": 15} 
    with open(f) as fr, open(to_f, "w") as fw: 
     for line in fr: 
         line = line.rstrip() 
         match = re.findall(r'第(.+?)季', line) 
         if len(match): 
             match = match[0] 
             if match in list(map(str, d_map.values())): 
                 d_map[match] = match 
             line = line.replace('第{}季'.format(match), "").rstrip() 
             if line in have_s or len(line) == 1: 
                 continue 
             have_s.add(line) 
             have_s.add(line+str(d_map[match])) 
             fw.write("{}\n".format(line)) 
             fw.write("{}\n".format(line+str(d_map[match]))) 
         else: 
             line = line.split()[0] 
             if line in have_s: 
                 continue 
             have_s.add(line) 
             fw.write("{}\n".format(line))  
             


import re
class Entity_Fix:
    def __init__(self):
        pass
    def remove_in(self, f, to_f, patts=[['\(', '\)', ""], ['（', '）', ""]]):
        have_s = set() 
        with open(f) as fr, open(to_f, "w") as fw:
            for line in fr: 
                line = line.rstrip()
                for one_pa in patts:
                    match = re.findall(r'{}(.+?){}'.format(one_pa[0], one_pa[1]), line) 
                    if len(match): 
                        match = match[0] 
                        line = line.replace('{}{}{}'.format(one_pa[0].replace("\\", ""), match, one_pa[1].replace("\\", "")), one_pa[2]).rstrip() 
                line = line.strip() 
                if line in have_s: 
                    continue 
                have_s.add(line) 
                fw.write("{}\n".format(line))