import requests
from bs4 import BeautifulSoup as bs

#提供一些头供使用
headers_chrome = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
    }
headers_mobile = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Mobile Safari/537.36"
}  # 模拟手机

#通过url获取可定位的utf-8格式的soup，不传heard为默认heard
def get_soup(url,header):
    if header=='':
        header=headers_chrome
    web_data = requests.get(url, headers=header)
    web_data.encoding = 'utf-8'
    return bs(web_data.text, 'lxml')