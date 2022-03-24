import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

key_word = input('请输入商品关键词：')
key_page = eval(input('请输入爬取页数：'))
f = open(f'{key_word}.csv', mode='a', encoding='utf-8', newline='')
csv_write = csv.DictWriter(f, fieldnames=[
    '标题',
    '价格',
    '评论量',
    '店铺名字',
    '详情页',
])

driver = webdriver.Chrome()  # 这里需要下载谷歌驱动

driver.get('https://www.jd.com/')


driver.find_element(by=By.CSS_SELECTOR, value='#key').send_keys(key_word)

driver.find_element(by=By.CSS_SELECTOR, value='#search > div > div.form > button').click()

# 自动下滑代码
def drop_down():
    """执行页面滚动的操作"""  # javascript
    for x in range(1, 12, 2):  # 1 3 5 7 9  在你不断的下拉过程中, 页面高度也会变的
        time.sleep(1)
        j = x / 9  # 1/9  3/9  5/9  9/9
        # document.documentElement.scrollTop  指定滚动条的位置
        # document.documentElement.scrollHeight 获取浏览器页面的最大高度
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


def get_shop_info():
    driver.implicitly_wait(10)  # 隐式等待  什么时候加载完，什么时候继续下一步
    drop_down()
    lis = driver.find_elements(by=By.CSS_SELECTOR, value='#J_goodsList > ul > li')
    for li in lis:
        title = li.find_element(by=By.CSS_SELECTOR, value='.p-name a em').text
        price = li.find_element(by=By.CSS_SELECTOR, value='.p-price i').text
        comment = li.find_element(by=By.CSS_SELECTOR, value='.p-commit a').text
        shop_name = li.find_element(by=By.CSS_SELECTOR, value='.p-shop a').text
        href = li.find_element(by=By.CSS_SELECTOR, value='.p-name a').get_attribute('href')   # 提取链接
        dit = {
            '标题': title,
            '价格': price,
            '评论量': comment,
            '店铺名字': shop_name,
            '详情页': href,
        }
        csv_write.writerow(dit)
    driver.find_element(by=By.CSS_SELECTOR, value='.pn-next').click()

for page in range(1, key_page):   #手动设置页数
    time.sleep(1)
    get_shop_info()
driver.quit()       # 运行结束后关闭

# get_shop_info()


