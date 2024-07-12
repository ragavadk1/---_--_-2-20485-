import requests
import re
import json
import os
headers = {
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-platform': '"Android"',
    'dnt': '1',
    'sec-ch-ua-mobile': '?1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36',
    'content-type': 'application/json',
    'accept': '*/*',
    'origin': 'https://dlive.tv',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://dlive.tv/',
    'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'priority': 'u=1, i',
}


url = re.findall("https://.*/src/live.m3u8", requests.get("https://live.prd.dlive.tv/hls/live/funnybunny-yt.m3u8").text)[0]
json_data = {
    'playlisturi': f'{url}'
}

esponse44 = requests.post('https://live.prd.dlive.tv/hls/sign/url', headers=headers, json=json_data).text
print(esponse44)

os.system(f"ffmpeg -headers $'User-Agent: Mozilla/5.0 (Android; vivo V2311) Android/14 version/1.17.74\r\nHost: livestreamc.prdv3.dlivecdn.com\r\nConnection: Keep-Alive\r\nAccept-Encoding: identity\r\nReferer: https://dlive.tv/\r\n' -re -i '{esponse44}' -threads 4 -vcodec libx264 -b:v 9000k -preset ultrafast -tune zerolatency -flags low_delay -fflags '+nobuffer+flush_packets' -max_delay 0 -muxdelay 0 -x264opts keyint=30 -acodec copy -f flv 'rtmp://txpush.rtmp.nimo.tv/live/su2339515334474r0797ec14751428a3cb6c284c2a9eb8a1?guid=0ad765ea21a98a666f0156c457c404f7&hyapp=81&hymuid=2339515334474&hyroom=4547490916&psign=744e57f4efb3b3217e40813e69915abb&rtag=MzREPe20Ga&sru=KH2MNE2I1&txHost=txpush.rtmp.nimo.tv&ua=d2ViJjEuMC40Jm5pbW9UVg==&appid=81&room=4547490916&muid=4679030655903&seq=1720629004895&streamcode=huya_inner_user'")
