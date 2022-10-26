import requests
url="https://fanyi.baidu.com/sug"
s=input("输入要翻译的单词：")
bat={"kw":s}
resp=requests.post(url,data=bat)
print(resp.json())
resp.close()

