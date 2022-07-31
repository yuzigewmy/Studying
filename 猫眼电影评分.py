from lxml import etree
import requests
import redis
def main():
    r = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    for i in range(0,880890,30):
        url = f"https://www.maoyan.com/films?showType=3&offset={i}"
        # print(url)
        headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
        resp=requests.get(url=url,headers=headers)
        html_doc=resp.content.decode("utf-8")
        html=etree.HTML(html_doc)
        moive_name=html.xpath('//div[@class="channel-detail movie-item-title"]/@title')
        for i in range(len(moive_name)):
            print(moive_name[i])
            r.set(moive_name[i],moive_name[i])
if __name__=="__main__":
    main()