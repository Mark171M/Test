import requests
import re
import os
import json
import pprint
from tqdm import tqdm

url ='https://vd.l.qq.com/proxyhttp'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
data ={"buid":"vinfoad","adparam":"pf=in&ad_type=LD%7CKB%7CPVL&pf_ex=pc&url=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fm441e3rjq9kwpsc%2Fh00251u5sdp.html&refer=https%3A%2F%2Fv.qq.com%2Fx%2Fsearch%2F&ty=web&plugin=1.0.0&v=3.5.57&coverid=m441e3rjq9kwpsc&vid=h00251u5sdp&pt=&flowid=166b3014691edf90a50da85c3d096239_10201&vptag=www_sogou_com%7Cx&pu=0&chid=0&adaptor=2&dtype=1&live=0&resp_type=json&guid=4215f8fb80be442f69a7ffdb80560344&req_type=1&from=0&appversion=1.0.173&platform=10201&tpid=3&rfid=ab76b4078d6c5b13ec76fd38b4fa87b3_1645936712","vinfoparam":"spsrt=1&charge=0&defaultfmt=auto&otype=ojson&guid=4215f8fb80be442f69a7ffdb80560344&flowid=166b3014691edf90a50da85c3d096239_10201&platform=10201&sdtfrom=v1010&defnpayver=1&appVer=3.5.57&host=v.qq.com&ehost=https%3A%2F%2Fv.qq.com%2Fx%2Fcover%2Fm441e3rjq9kwpsc%2Fh00251u5sdp.html&refer=v.qq.com&sphttps=1&tm=1645937109&spwm=4&logintoken=%7B%22main_login%22%3A%22%22%2C%22openid%22%3A%22%22%2C%22appid%22%3A%22%22%2C%22access_token%22%3A%22%22%2C%22vuserid%22%3A%22%22%2C%22vusession%22%3A%22%22%7D&vid=h00251u5sdp&defn=shd&fhdswitch=0&show1080p=1&isHLS=1&dtype=3&sphls=2&spgzip=1&dlver=2&hdcp=0&spau=1&spaudio=15&defsrc=2&encryptVer=9.1&cKey=NiHCU8R_jkl6JZEItZs_lpJX5WB4a2CdS8kHWN6OVaqtHEZQ1c_W6myJ8hQFnmDDGMFrTtafKjvp2vPBr-xE-uhvZyEMY131vUh1H4pgCXe2Op9Lrzb_fbB32kFt6bl1q3wsEERWFNvMluNDEH6IC8EOljLQ2VfW2sTdospNPlD9535CNT9iSo3aNBH9zIg0GafMPJVASLfUSMb5t1pjAAuGkoYGNScB_8lMah6WVCJtO-Ygxs9f-BtA8o_vOrSIjG_VH7z3tWJM-Px_AUNIsHEG9zgzglpES47qAUrvH-0706f5Jz35DBkQKl4XAh32cbzn6-aGRCBn0_bLtiyFnj8Z2EYwYYPpdFF8VJL6DeS2MWnum05yf2VBN_rgOYZ8DPkGBgYGBgYlWpgQ&fp2p=1&spadseg=3"}

response = requests.post(url=url,headers=headers,json=data)
# pprint.pprint(response.json())
result = response.json()['vinfo']
m3u8_url = re.findall('"url":"(.*?)"',result)[3]
# print(m3u8_url)
m3u8_data = requests.get(url=m3u8_url).text
# print(m3u8_data)
m3u8_data = re.sub('#EXTM3U','',m3u8_data)
m3u8_data = re.sub('#EXT-X-VERSION:\d','',m3u8_data)
m3u8_data = re.sub('#EXT-X-MEDIA-SEQUENCE:\d','',m3u8_data)
m3u8_data = re.sub('#EXT-X-TARGETDURATION:\d+','',m3u8_data)
m3u8_data = re.sub('#EXTINF:\d+\.\d+,','',m3u8_data)
m3u8_data = re.sub('#EXT-X-ENDLIST','',m3u8_data)
m3u8_data = re.sub('#EXT-X-PLAYLIST-TYPE:VOD','',m3u8_data).split()   #将字符串切片成列表
# print(m3u8_data)
# print(len(m3u8_data))
for ts in tqdm(m3u8_data):
    ts_url = 'https://apd-f295aa7ea8011fdbc82e99a3e6ce2cf5.v.smtcdns.com/moviets.tc.qq.com/AvlLTU9w3mE73XFM7UBFePlSuHnQyaUH7iQdg3Y6UyWU/uwMROfz2r5zAoaQXGdGnC2df64-iUwCiwZmikOBGnwTA3zLD/VBXW-BOqIEc12-fK0QpmfeJ6Vk-2sGTVypW5tmghpK736VHo_W_wRsCeC79dTGczjDhXf_bmxBuxBrS4t7OH_DX8cwkVc5rriC-kp7h8PSMu5Nne3eUWGw8-TNV_ts65Hd7GsQr9YqRs2TbyUIbVg-UTVubMZ0vJPvtKmmN69AxYCn5pluf7Wg/'+ts
    # print(ts_url)
    ts_content = requests.get(url=ts_url,headers=headers).content
    with open('斗罗大陆第一集.mp4',mode='ab') as f:
        f.write(ts_content)
print('下载完成')
