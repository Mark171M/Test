import requests
import re
import prettytable
import os

filename = '歌曲下载\\'

if not os.path.exists(filename):
    os.mkdir(filename)

name = input('请输入歌手名字：')
url = f'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?p=1&n=10&w={name}'
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    # 'Cookie': 'pgv_pvid=4227223875; RK=Y0TkAmcewt; ptcz=3a828bb1418fef564dd446864d5d7e6c7562128b5d68f825b464081becb8864e; fqm_pvqid=36f3d133-a426-438a-83d0-1821e340c527; ts_uid=5469654834; LW_uid=Y1L6P2C7r3S822W8D1s1v5N7n8; eas_sid=61d6w2q7A3f8d2Y8J1W1d5X8z3; Qs_lvt_323937=1627382806%2C1628862589; Qs_pv_323937=1419504452504244200%2C153728413586928030; LW_sid=v156O2D9Z121j1k3e0t2a1J5N4; ied_qq=o3421355804; ptui_loginuin=1321228067; _gcl_au=1.1.1508020928.1629704849; pt_235db4a7=uid=ZQvkc6mgZ/IgqUlIz0-9/A&nid=1&vid=-52PpDj4Jxm4Azg-ojxaMw&vn=1&pvn=1&sact=1629704849033&to_flag=0&pl=0KzaISwJA-wYoyVB1nkjpQ*pt*1629704849033; _ga=GA1.2.129533475.1629704849; tmeLoginType=2; pac_uid=1_321228067; iip=0; tvfe_boss_uuid=bb9075b919981d3a; o_cookie=1321228067; fqm_sessionid=cdf92536-8796-42d8-b3df-a5dd1f7ed779; pgv_info=ssid=s8544727808; ts_refer=ADTAGmyqq; _qpsvr_localtk=0.485361667619747; login_type=1; qm_keyst=Q_H_L_24HXk560eyZgA931iPUTiWoSp_xP9wMRpYW0s8WgQWUrkjK_o_ZV6jE8WdjBBU3; qqmusic_key=Q_H_L_24HXk560eyZgA931iPUTiWoSp_xP9wMRpYW0s8WgQWUrkjK_o_ZV6jE8WdjBBU3; wxunionid=; wxopenid=; psrf_qqunionid=FAEE1B5B10434CF5562642FABE749AB9; psrf_qqrefresh_token=309E71065899568052CD8433ECBED69C; wxrefresh_token=; psrf_musickey_createtime=1634632977; uin=1321228067; euin=oKoAoK-ANens7z**; psrf_qqaccess_token=098E5A5A88BFCFF2513A0D2AC9C09C9F; psrf_qqopenid=4F37937E43ECA9EAB02F9E89BE1860E2; psrf_access_token_expiresAt=1642408977; qm_keyst=Q_H_L_24HXk560eyZgA931iPUTiWoSp_xP9wMRpYW0s8WgQWUrkjK_o_ZV6jE8WdjBBU3; ts_last=y.qq.com/n/ryqq/search',
    'Cookie': 'RK=A1tpemi0dY; ptcz=97bdcae2d7309b658b618d80681fffee7e946368ae1a53cfd6ce3a67f911cea2; pgv_pvid=3470157479; o_cookie=1714889726; pac_uid=1_1714889726; iip=0; tvfe_boss_uuid=e88f6c0b4f805ebd; luin=o1714889726; fqm_pvqid=58865504-c009-4bcf-bf48-3efb18fdf97a; ts_uid=213156412; wxopenid=; tmeLoginType=2; psrf_qqopenid=E9AB537EAF45E9F18164D892B416F29B; psrf_qqrefresh_token=B1A0D08662F45B0CD9521EF624FFB076; euin=oKS57ecFNKSA7c**; psrf_qqaccess_token=0252B5E66CE1A94BEDEDA66CF098255D; wxunionid=; psrf_qqunionid=9FD29177181272B844696464FF804465; wxrefresh_token=; ariaDefaultTheme=undefined; lskey=0001000052a6ea9e99a610898dced068ff32db1a9b9221b27eda3e684cd04d4f1f8d8c8d6b719518ade3e1c5; fqm_sessionid=00e19787-67aa-4839-99a2-83358ff46cf3; pgv_info=ssid=s8823320837; ts_refer=www.baidu.com/; _qpsvr_localtk=0.4733289969829315; login_type=1; qm_keyst=Q_H_L_5y7K1w_mlAXEy36_7GSAPioy5aIoZx9WyVZ2HYJOXns9l87U40m7k-Q; psrf_access_token_expiresAt=1654607673; qqmusic_key=Q_H_L_5y7K1w_mlAXEy36_7GSAPioy5aIoZx9WyVZ2HYJOXns9l87U40m7k-Q; qm_keyst=Q_H_L_5y7K1w_mlAXEy36_7GSAPioy5aIoZx9WyVZ2HYJOXns9l87U40m7k-Q; uin=1714889726; psrf_musickey_createtime=1646831673; ts_last=y.qq.com/n/ryqq/singer/002rHyN14UyyaW'
}

response = requests.get(url=url, headers=headers)

json_data = response.text[9:-1]
#将类型转换为字典
json_data = eval(json_data)

# print(type(json_data))

table = prettytable.PrettyTable()
table.field_names = ['序号', '歌名', '歌手', '专辑']
song_list = json_data['data']['song']['list']
music_info_list =[]
count = 0
for song_data in song_list:
    songmid = song_data['songmid']
    songname = song_data['songname']
    singer_name = song_data['singer'][0]['name']
    albumname = song_data['albumname']
    table.add_row([count, songname, singer_name, albumname])
    # 将音乐信息存储在 列表当中
    music_info_list.append([songname, singer_name, songmid])
    count = count + 1
print(table)

while True:
    input_count = input('输入序号下载（-1退出）')
    if input_count == -1:
        print('程序已退出')
        break
    download_info = music_info_list[int(input_count)]
    url_1 = 'https://u.y.qq.com/cgi-bin/musicu.fcg?data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch", "filename":"M800","param":{"guid":"8846039534","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","filename":"M800","param":{"guid":"8846039534","songmid":["%s"],"songtype":[0],"uin":"1152921504784213523","loginflag":1,"platform":"20"}},"comm":{"uin":"1152921504784213523","format":"json","ct":24,"cv":0}}' % download_info[2]
    response_1 = requests.get(url=url_1, headers=headers).json()
    # print(response_1)
    purl = response_1['req_0']['data']['midurlinfo'][0]['purl']
    music_url = 'http://dl.stream.qqmusic.qq.com/' + purl
    print(music_url)
    music_content = requests.get(url=music_url, headers=headers).content
    with open(filename + f'{download_info[0]}-{download_info[1]}.mp3', mode='wb') as f:
        f.write(music_content)
        print(f'{download_info[0]}' + '下载完成')