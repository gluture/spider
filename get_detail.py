import requests
from bs4 import BeautifulSoup

#
#    下面是针对“环球网地图中娱乐”页面抓取娱乐新闻地址，再抓起新闻内容
#

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63'
}
path = "C:\\Users\\admin\\Desktop\\娱乐\\"
count = 30000
for page in range(0,300):
    content = requests.get('https://www.huanqiu.com/sitelist?node=/e3pmh1jtb&offset='+str(page*40)+'&limit=40&ltime=1483228800000&rtime=1514678400000',headers=headers).text
    sou = BeautifulSoup(content,'lxml')
    divs = sou.find_all('div',attrs={'class':'item'})
    for div in divs:
        a = div.find('a').get('href')
        detail_content = requests.get('http:'+a,headers=headers).text
        soup = BeautifulSoup(detail_content, 'lxml')
        if(soup.article.select('p')!=None):
            results = soup.article.select('p')
        else:
            results = soup.article.section.select('p')
        detail = ''
        for result in results:
            if result.get_text().strip() != None:
                detail = detail + result.get_text().strip()
        line = detail + '\n'
        full_path = path+str(count)+'.txt'
        file = open(full_path,'w',encoding='utf=8')
        file.write(line)
        file.close()
        count = count + 1
