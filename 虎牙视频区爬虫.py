import requests
import os
import re
import pprint

filename = 'vedio\\'

if not os.path.exists(filename):
    os.mkdir(filename)

url = 'https://v.huya.com/g/all?set_id=51&order=mostplay&page=2'

headers ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
response = requests.get(url=url , headers=headers)
# print(response.text)

vedio_ids = re.findall('<li data-vid="(.*?)"><a href=".*?" class="video-wrap" target="_blank" title=".*?">',response.text)
# href = ['https:'+i for i in href]
# print(vedio_ids)

for vedio_id in vedio_ids:
    url_1 =f'https://liveapi.huya.com/moment/getMomentContent?videoId={vedio_id}'
    response_1 = requests.get(url=url_1,headers=headers)
    # pprint.pprint(response_1.text)
    title = re.findall('"title":"(.*?)","content":""',response_1.text)[0]
    # print(title)
    vedio_url = re.findall('"url":"(.*?)","m3u8":".*?","defName":"原画"}',response_1.text)[0]
    # print(title,vedio_url)
    vedio_content = requests.get(url=vedio_url,headers=headers).content
    with open(filename +title +'.mp4',mode='wb') as f:
        f.write(vedio_content)
    print(title+' 视频下载已完成')