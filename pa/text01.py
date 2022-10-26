import requests
q=input("请输入一个姓名：")

url = f'https://cn.bing.com/search?q={q}'
dic = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42"
}
res = requests.get(url, headers=dic)
res = requests.get(url)
print(res.text)
res.close()