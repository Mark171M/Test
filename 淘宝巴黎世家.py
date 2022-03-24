import json
import random
import time
import requests
import re
import pprint
import csv

f = open('淘宝巴黎世家.csv', mode='a', encoding='utf-8', newline='')     # a追加写入 不覆盖
csv_write = csv.DictWriter(f, fieldnames=[
    'raw_title',
    'pic_url',
    'detail_url',
    'view_sales',
    'item_loc',
    'nick',
])
csv_write.writeheader()   # 写入表头

headers ={
    'cookie': '_samesite_flag_=true; cookie2=1d2b07368caa5c4d396a497c12f60083; t=62969909291195f82b0dbc7f9cc81203; _tb_token_=e8e95be85be31; cna=ot+hGpxTcmgCAXW1Ll4r2tWC; xlly_s=1; sgcookie=E100l8qgQYW9h8%2BGLfA8v%2BKpeH%2FGlTyTo0vzfcfjL2luFMLKkWf1MvlIHibasSo8dsWNT5YDH4nMoUqKhKs3S8BCGblRAmNQ30D4nv6CQ2d68H9KGMMWSfY3HWbblKRYCs3X; unb=3212992399; uc1=cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie21=W5iHLLyFe3xm&existShop=false&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&pas=0&cookie14=UoewBj1%2FcU7PSw%3D%3D; uc3=nk2=odNtHmAnf8Sez8KU&vt3=F8dCvUFijpfFqRUTHv4%3D&id2=UNJQ75qVY3%2FWgg%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D; csg=35161c0d; lgc=%5Cu9A6C%5Cu9A6C%5Cu9A6C553366; cancelledSubSites=empty; cookie17=UNJQ75qVY3%2FWgg%3D%3D; dnk=%5Cu9A6C%5Cu9A6C%5Cu9A6C553366; skt=100aa1432f3f040e; existShop=MTY0NjcxMTkxOA%3D%3D; uc4=nk4=0%40o5sDAzvVzPdQakvt%2BDqNk%2BaX2CEyr3E%3D&id4=0%40UgXXlv%2Fq1%2BttdsmMbeVsUWQJQFmq; tracknick=%5Cu9A6C%5Cu9A6C%5Cu9A6C553366; _cc_=V32FPkk%2Fhw%3D%3D; _l_g_=Ug%3D%3D; sg=69b; _nk_=%5Cu9A6C%5Cu9A6C%5Cu9A6C553366; cookie1=AibkMOrGi9Lr%2F4bfRBMwCn0pNy8FvTfqDQKY0IW338o%3D; enc=vY%2FnhHB%2BpFGOJ2SkphI8XraD7LmOmpc1RgAGm%2FnRt8U%2BHPLTgP0xl3Fi%2BwlYPKq%2F9uCHc75IiZv%2B73%2Ftb1aCQA%3D%3D; l=eBx5fgIuLap7wDPsBO5Clurza779NCOH1kPzaNbMiIncC6qFNjvtYt-Q07ETjKtRR8XciTYk4fXnORetfFnYJyMjJ0YEae1VivE2Cef..; tfstk=cPHdB3bQWFYHoyEt0XdiPaQd4O0RaTY85Maleh4hawfVTd1VisAjnxuTmBZ7lg-O.; isg=BBgYvx2azt1rx-JZ1oXbva9M50aqAXyLqPG6OFIMRtHc7bPX8BOaG-iPJSVdZjRj; JSESSIONID=D916A61783E15B6AF8B6E7F814AD8A2E',
    'referer': 'https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.jianhua.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E5%B7%B4%E9%BB%8E%E4%B8%96%E5%AE%B6%E4%B8%9D%E8%A2%9C&suggest=0_1&_input_charset=utf-8&wq=%E5%B7%B4%E9%BB%8E%E4%B8%96%E5%AE%B6&suggest_query=%E5%B7%B4%E9%BB%8E%E4%B8%96%E5%AE%B6&source=suggest',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
}

for page in range(1, 5):                # 爬取的页数
    time.sleep(random.randint(3, 5))
    url = f'https://s.taobao.com/search?data-key=s&data-value=176&ajax=true&_ksTS=1646716306555_1496&callback=jsonp1497&initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.jianhua.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E5%B7%B4%E9%BB%8E%E4%B8%96%E5%AE%B6%E4%B8%9D%E8%A2%9C&suggest=0_1&_input_charset=utf-8&wq=%E5%B7%B4%E9%BB%8E%E4%B8%96%E5%AE%B6&suggest_query=%E5%B7%B4%E9%BB%8E%E4%B8%96%E5%AE%B6&source=suggest&bcoffset=4&p4ppushleft=2%2C48&ntoffset=4&s={page*44}'
    response = requests.get(url=url, headers=headers)
    # print(response.text)
    # html_data = re.findall('g_page_config = (.*);', response.text)[0]
    html_data = response.text[12:-2]
    print(html_data)
    json_data = json.loads(html_data)
    auctions_list = json_data['mods']['itemlist']['data']['auctions']
    for data in auctions_list:
        raw_title = data['raw_title']
        pic_url = data['pic_url']
        detail_url = data['detail_url']
        view_sales = data['view_sales']
        item_loc = data['item_loc']
        nick = data['nick']
        with open('淘宝巴黎世家' + '.csv', mode='a', encoding='utf-8', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([raw_title, pic_url, detail_url, view_sales, item_loc, nick])
        print(raw_title, pic_url, detail_url, view_sales, item_loc, nick)




