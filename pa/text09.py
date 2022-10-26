import requests
urls=["https://pic.kontori.top/api/getAllCollections?page=1&limit=15&mode=0","https://pic.kontori.top/api/getAllCollections?page=2&limit=15&mode=0"]
for url in urls:#通过两个API地址依次请求
    resp=requests.get(url)
    info=resp.json()
    download=info["data"]
   # print(info)
    for i in download:
        id=i["collectionId"]
        name=i["name"]
        artist=i["artist"]
        imgurl=i["imgUrl"]
        resp2=requests.get(imgurl)
        img_name=str(id)+"-"+name+"-"+artist+"."+imgurl.split("?")[0].split(".")[-1]#编辑图片名称
        with open("C:/Users/周银/Desktop/task1/"+img_name,mode="wb")as f:
            f.write(resp2.content)
            print("over...")
print("all over !")




