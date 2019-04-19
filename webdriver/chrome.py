from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 网络直取
def get_html(url):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(chrome_options=chrome_options)
        driver.get(url)
        return driver


print(get_html("http://www.holleyou.com").page_source)