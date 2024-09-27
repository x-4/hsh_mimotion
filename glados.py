import requests

cookies = {
    '_ga': 'GA1.1.590011439.1727227450',
    'koa:sess': 'eyJ1c2VySWQiOjUyNzgwNCwiX2V4cGlyZSI6MTc1MzE0NzQ3MDU4MiwiX21heEFnZSI6MjU5MjAwMDAwMDB9',
    'koa:sess.sig': 'Avv3SkMxWAVvzbi6yYQopKXZEe4',
    '_ga_CZFVKMNT9J': 'GS1.1.1727227450.1.1.1727227493.0.0.0',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': '47898876190570387765234016300546-746-1516',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://glados.rocks',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
}

json_data = {
    'token': 'glados.one',
}

response = requests.post('https://glados.rocks/api/user/checkin', cookies=cookies, headers=headers, json=json_data)
print(response.json()['message'])
