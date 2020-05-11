import requests
import json
def parse(index, biz, uin, key):
    
    # url前缀
    url = "https://mp.weixin.qq.com/mp/profile_ext"

    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 "
                      "Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.901.400 "
                      "QQBrowser/9.0.2524.400",
    }

    proxies = {
        'https': None,
        'http': None,
    }

    # 重要参数
    param = {
        'action': 'getmsg',
        '__biz': biz,
        'f': 'json',
        'offset': index * 10,
        'count': '10',
        'is_ok': '1',
        'scene': '124',
        'uin': uin,
        'key': key,
        'wxtoken': '',
        'x5': '0',
    }

    # 发送请求，获取响应
    reponse = requests.get(url, headers=headers, params=param, proxies=proxies)
    reponse_dict = reponse.json()

    # print(reponse_dict)
    next_offset = reponse_dict['next_offset']
    can_msg_continue = reponse_dict['can_msg_continue']

    general_msg_list = reponse_dict['general_msg_list']
    data_list = json.loads(general_msg_list)['list']

    print(data_list)

    for data in data_list:
        try:
            datetime = data['comm_msg_info']['datetime']
            date = time.strftime('%Y-%m-%d', time.localtime(datetime))

            msg_info = data['app_msg_ext_info']

            # 标题
            title = msg_info['title']

            # 内容的url
            url = msg_info['content_url'].replace("\\", "").replace("http", "https")
            url = html.unescape(url)
            print(url)

            res = requests.get(url, headers=headers, proxies=proxies)
            with open('C:/Users/admin/Desktop/test/' + title + '.html', 'wb+') as f:
                f.write(res.content)

            print(title + date + '成功')

        except:
            print("不是图文消息")

    if can_msg_continue == 1:
        return True
    else:
        print('全部获取完毕')
        return False