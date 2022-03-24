import json
import requests
import re
import pprint
import csv
import time

f = open('招聘信息.csv', mode='a', encoding='utf-8', newline='')     # a追加写入 不覆盖
csv_write = csv.DictWriter(f, fieldnames=[
    '职位',
    '城市',
    '薪资',
    '要求',
    '公司',
    '福利',
    '发布如期',
    '公司规模',
    '公司类型',
    '详情页'
])
csv_write.writeheader()   # 写入表头

headers ={         # headers需要及时更换
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '_uab_collina=164653452945217906160666; partner=www_baidu_com; privacy=1646534366; guid=9e8a57d84e5dda68190d29929586481b; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%60000000%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA0%A1%FB%A1%FApython%A1%FB%A1%FA2%A1%FB%A1%FA1%7C%21; acw_sc__v2=62242a7b47276797de3174acda3fd804a5c45a7c; acw_tc=ac11000116465391843365773e00cda2594807a39adb3f53532ab707d7db40; acw_sc__v2=622431b075e27c3787adb5574aa98af8f9240720; ssxmod_itna=QqUhqjxx7DOGCDnDl34+O8rreAIBR+awpc0eorKDsF1TDSxGKidDqxBne1eDtdACnOrN4LKzRRwKd8rjEbILzW7aTG=IDB3DEx06xOEDYYCDt4DTD34DYDix5DLDmeD+INKDdjpk5NkuDAQDQ4GyDitDKdiDxG3D0+657G6SBS0DTeDSKAUb7qDMD7tD/fqbHG=DGLnTH7XSSje88DxDChek6Y4kqdeDbOPu3jiDtqD97CtXbn9ySMU2/PpYFEx30fvoSApxjA5oFYx3KBh1d4hs0ixHiXAQIDYQFDDAjieWI7DxD===; ssxmod_itna2=QqUhqjxx7DOGCDnDl34+O8rreAIBR+awpc0eoxikfFNYDlgUDjbn=6vqQid=nFDKwyDkDonMHrdYobLw0zxwCeF6sQ6bqkjs7rFldj+cnDw80jiTwQ7g7ULKyW9g2YH6YN90iiM6QcWFkS2vdVPaq/=B7NiwTOPxDBlYpfZuzDbDpM6eb=iPNeiwm0nDWlByqvEvwr+S8ygANrp0wAZEwQRe+Ogyzraq0Ogqf=CaqYra=Lt8=1DqpcerGZb1oDOwQiaWk/cZ9KaSh/=/AA=GETE=gnj3ogmwQt4aE=WmLd78OxxvL7EXwxefD5datOB5dWNe4mPfihi3O0pY8hRjidPmbaXYFe3=t8QfbZjY4jPRqf7bVCizionAXQZeg2q5crEB5fWfZCtyoP3xpI7x3ZwC/0h3p0ib8In6ibhRTrp6IGKbIKfI=rI6TEpGnKeOXL3q0KvYjfRiwxmtub96/e+9dd09wPHP0Fdi=GZKaDG2iDx/icCrdoiVlMcbuqelWzDDFqD+EXPjoo=U5QDxD===',
    'Host': 'search.51job.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.51job.com/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
}

for page in range(1, 5):        # 爬取1~4页的信息
    url = f'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,{page}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='

    response = requests.get(url=url, headers=headers)
    # print(response.text)

    data = re.findall('window.__SEARCH_RESULT__ =(.*?)</script>', response.text)[0]
    # pprint.pprint(data)
    # print(type(data))

    json_data = json.loads(data)
    # pprint.pprint(json_data['engine_jds'])

    for index in json_data['engine_jds']:
        dit = {
            '职位': index['job_name'],
            '城市': index['workarea_text'],
            '薪资': index['providesalary_text'],
            '要求': index['attribute_text'],
            '公司': index['company_name'],
            '福利': index['jobwelf'],
            '发布如期': index['updatedate'],
            '公司规模': index['companysize_text'],
            '公司类型': index['companytype_text'],
            '详情页': index['job_href'],
        }
        time.sleep(2)
        csv_write.writerow(dit)
        print(dit)

