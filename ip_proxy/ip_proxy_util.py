'''
 通过关键字爬取新浪微博内容
'''

from urllib import request,error
import requests
import random
from ip_proxy import db_util_proxy

list_ip=[] # ip池

# 使用远程代码ip池：https://github.com/jhao104/proxy_pool
# 这个有效率太低了
def get_proxy_remote():
    cont = requests.get("http://118.24.52.95:5010/get/").content
    return str(cont).replace('b','').replace('\'','')

def get_proxy_remote_all():
    cont = requests.get("http://118.24.52.95:5010/get_all/").content
    return str(cont).replace('b','').replace('\'[','').replace(']\\n\'','')

#每24小时监测一下，如果可用ip数少于指定数，那就重新get_all一下
#若发现ip不可用，使用者可直接从库中删除
def flush_ip():
    url = "http://www.baidu.com"
    ip_ports = get_proxy_remote_all().split(',')
    for ip in ip_ports:
        ip = ip.replace("\"","")
        proxy = {'http': ip}
        # proxy = {'http': '206.125.41.135:80'}
        proxy_handler = request.ProxyHandler(proxy)
        opener = request.build_opener(proxy_handler)
        request.install_opener(opener)
        try:
            rsp = request.urlopen(url, timeout=5)  # 只要3秒之内有回应的
            if(rsp.status=='200'):
                db_util_proxy.insertOne(ip,"3s")
        except error.URLError as e:
            print(e)
        except Exception as e:
            print(e)

#删除一个代理ip
def delete_ip(ip):
    db_util_proxy.delete_by_proxy(ip)

# 获取一个代理IP
def get_proxy_ip():
    # 如果ip池为空，则初始化一次；随机取一个ip返回
    global list_ip
    if(len(list_ip)>0):
        return random.choice(list_ip)[0]
    else:
        list_ip = db_util_proxy.find_all_proxy()
        return random.choice(list_ip)[0]

if __name__ == '__main__':
    ip1 = get_proxy_ip()
    print(ip1)
    print(get_proxy_ip())
    print(get_proxy_ip())
    print(get_proxy_ip())

    # ip_port = get_proxy_remote()
    # print((ip_port))
    # proxy = {'http': ip_port}
