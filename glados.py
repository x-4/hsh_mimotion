import requests

cookies = {
    'koa:sess': 'eyJ1c2VySWQiOjUyNzgwNCwiX2V4cGlyZSI6MTc3MTE0Mjg1MDE3OSwiX21heEFnZSI6MjU5MjAwMDAwMDB9',
    'koa:sess.sig': 'aQBu0yh4XZQTnstFwI9OnS0QPCs',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': '35760725020723938811840811722317-1080-1920',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://glados.rocks',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
}

json_data = {
    'token': 'glados.one',
}

response = requests.post('https://glados.rocks/api/user/checkin', cookies=cookies, headers=headers, json=json_data)

print(response.text)
