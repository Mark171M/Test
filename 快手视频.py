import json
import requests
import re
import pprint
import os

filename = '快手视频\\'

if not os.path.exists(filename):
    os.mkdir(filename)

user_id = input('请输入用户id:')
url = 'https://www.kuaishou.com/graphql'

headers = {
    'content-type': 'application/json',
    'Cookie': 'did=web_52d28b76ed2b1c5502844f8908df8225; didv=1647075319085; kpf=PC_WEB; kpn=KUAISHOU_VISION; clientid=3',
    'Host': 'www.kuaishou.com',
    'Origin': 'https://www.kuaishou.com',
    'Referer': 'https://www.kuaishou.com/profile/3x8idrcypvp8xxe',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
}



def get_next_page(pcursor):
    data = {
        'operationName': 'visionProfilePhotoList',
        'query': "query visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      type\n      author {\n        id\n        name\n        following\n        headerUrl\n        headerUrls {\n          cdn\n          url\n          __typename\n        }\n        __typename\n      }\n      tags {\n        type\n        name\n        __typename\n      }\n      photo {\n        id\n        duration\n        caption\n        likeCount\n        realLikeCount\n        coverUrl\n        coverUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrls {\n          cdn\n          url\n          __typename\n        }\n        photoUrl\n        liked\n        timestamp\n        expTag\n        animatedCoverUrl\n        stereoType\n        videoRatio\n        profileUserTopPhoto\n        __typename\n      }\n      canAddComment\n      currentPcursor\n      llsid\n      status\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n",
        'variables': {'userId': user_id, 'pcursor': pcursor, 'page': "profile"},
    }

    response = requests.post(url=url, headers=headers, json=data)
    # print(response.text)

    response_json = response.json()
    # pprint.pprint(response_json)

    feeds = response_json['data']['visionProfilePhotoList']['feeds']
    next_pcursor = response_json['data']['visionProfilePhotoList']['pcursor']

    for feed in feeds:
        photoUrl = feed['photo']['photoUrl']
        caption = feed['photo']['caption']
        caption = re.sub(r'[\\\/\:\*\?\"\"\<\>\|]', '_', caption[10])
        # caption = re.sub('[\\/:*?"<>|\n\t]', '', caption)
        # print(caption, photoUrl)
        photoUrl_content = requests.get(url=photoUrl).content
        with open(filename + f'{caption}' + '.mp4', mode='wb') as f:
            f.write(photoUrl_content)
        print(f'{caption}' + '下载完成！')
    get_next_page(next_pcursor)

get_next_page('')