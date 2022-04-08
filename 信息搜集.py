import whois
import os
import time
import socket
# whois查询
def whois_check(ym):
    q1 = whois.query(ym)
    print(q1.__dict__)
# ip判断
def ip_check(ym):
    # ip=socket.getaddrinfo('baidu.com',8080) #该方法需要域名和端口两个参数
    ip = socket.gethostbyname(ym)  # 根据域名获取服务器ip
    print(ip)
# 判断cdn
def pd_cdn(ym):
    q1 = os.popen(f'nslookup {ym}')
    q2 = q1.read()
    q3 = q2.count('.')
    if q3 > 10:
        print(f'{ym}使用了cdn技术')
    else:
        print(f'{ym}没有使用cdn技术')
# 子域名收集
def domain_scaner(ym):
    for ymqz in open('dic.txt'):
        ymqz = ymqz.replace('\n', '')
        url = ymqz + '.' + ym
        try:
            ip = socket.gethostbyname(url)
            jg = ip + '|' + url
            print(jg + '\n')
        except Exception as e:
            pass
# 端口扫描

# 功能集合
def information_check():
    ym = input('输入域名：')
    ip_check(ym)
    whois_check(ym)
    pd_cdn(ym)
    domain_scaner(ym)


information_check()