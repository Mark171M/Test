import requests
import re

url = 'https://music.163.com/discover/toplist'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'
}

response = requests.get(url=url, headers=headers)
# print(response.text)
song_list = re.findall('<a href="/discover/toplist\?id=(.*?)" class="s-fc0">(.*?)</a>', response.text)  # 获取榜单id列表
# print(song_list)

for song_list in song_list:
    print(f'-------------正在爬取: {song_list[1]}-------------')
    list_url = f'https://music.163.com/discover/toplist?id={song_list[0]}'
    list_url_response = requests.get(url=list_url, headers=headers)
    # print(list_url_response.text)
    song_id = re.findall('<li><a href="/song\?id=(.*?)">.*?</a></li>', list_url_response.text)
    song_name = re.findall('<li><a href="/song\?id=.*?">(.*?)</a></li>', list_url_response.text)
    # print(song_id, song_name)
    count = 0
    for id in song_id:
        song_url ='http://music.163.com/song/media/outer/url?id=' + id
        print(song_name[count] + ' ' + song_url)
        song_content = requests.get(url=song_url).content
        with open('歌曲列表/' + song_name[count] + '.mp3', mode='wb') as f:
            f.write(song_content)
        count += 1