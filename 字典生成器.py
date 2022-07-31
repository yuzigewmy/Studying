import itertools
str=input("请输入字典元素：")
num=int(input("请输入复杂度："))
temp=itertools.permutations(str,num)
with open("./passwd.txt",'a',encoding='utf-8') as f:
    for i in temp:
        f.write(''.join(i))
        f.write(''.join('\n'))
