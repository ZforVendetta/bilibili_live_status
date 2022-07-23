from logging import exception
import requests
import json



url = 'https://api.bilibili.com/x/space/acc/info?mid='
mid = '1472906636'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
}


html = requests.get(url+mid, headers=head)

msg = ''

if html.status_code  == 200:
    try:
        data = json.loads(html.text.encode("utf-8"))['data']
        live_data = data['live_room']
        # print(live_data)
        live_status = live_data['liveStatus']
        if live_status == 0:
            msg = f"{data['name']}未开播~"
        else:
            live_title = live_data['title']
            live_cover_url = live_data['cover']
            msg = f"{data['name']}开播啦~\n标题:{live_title}"
        if msg != '':
            print(msg)
        else:
            print('No Message!')
    except:
        print("Runtime Error!")

else:
    print("Api Unreached!")
input('\n\n按回车退出...')
