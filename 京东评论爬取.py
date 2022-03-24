import requests
import pandas as pd
from openpyxl.workbook import Workbook

key_page = eval(input('请输入爬取页数：'))
url = 'https://club.jd.com/comment/productPageComments.action?'   # 商品链接
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}
lis = []

for page in range(1, key_page):
    data = {
        # 'callback': 'fetchJSON_comment98',
        'productId': '100027793598',
        'score': '0',
        'sortType': '5',
        'page': '1',
        'pageSize': '10',
        'isShadowSku': '0',
        'fold': '1',
    }
    response = requests.get(url=url, params=data, headers=headers)
    # print(response.text)
    comments = response.json()['comments']
    # print(comments)
    for index in comments:
        content = index['content']  # 评论
        date = index['creationTime']  # 评论时间
        product = index['productColor']  # 购买商品
        name = index['nickname']  # 用户昵称
        dit = {
            '评论': content,
            '评论时间': date,
            '购买商品': product,
            '用户昵称': name,
        }
        lis.append(dit)
        print(dit)
        with open('键盘3.txt', mode='a', encoding='utf-8') as f:
            f.write(content)
            f.write('\n')
    pd_data = pd.DataFrame(lis)
    pd_data.to_excel('键盘3.xlsx', index=False)   # 这里用excle表格来存储


#      词云图      #

import wordcloud
import jieba

f = open('键盘3.txt', encoding='utf-8')  # 打开文件
txt = f.read()  #  读取文件
# print(txt)
txt_list = jieba.lcut(txt)  # 分割词汇
# print(txt_list)
string = ' '.join(txt_list)
wc = wordcloud.WordCloud(
    width=500,  # 宽度
    height=500,  # 高度
    background_color='white',  # 背景颜色
    font_path='msyh.ttc',  # 字体文件
)

wc.generate(string)
wc.to_file('键盘.png')