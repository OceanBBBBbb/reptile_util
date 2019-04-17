from selenium import webdriver
from selenium.webdriver.firefox.options import Options

#返回可操作的browser(携带本地火狐浏览器的cookie)，请记得quit和close
def get_browser(url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    fp = webdriver.FirefoxProfile(r'C:\Users\binhaiyang\AppData\Roaming\Mozilla\Firefox\Profiles\s74r4l93.default')
    browser = webdriver.Firefox(firefox_profile=fp,
                                executable_path=r'D:\files\chromedriver\geckodriver-v0.23.0-win64\geckodriver.exe',
                                firefox_options=options)  # D:\Program Files\Mozilla Firefox webdriver.Firefox(executable_path = 'D:\files\chromedriver\geckodriver-v0.23.0-win64')
    browser.maximize_window()  # 最大化进入头条的发文章页面
    browser.get(url)
    return browser