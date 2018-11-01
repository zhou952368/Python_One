# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d * %d = %d"%(i,j,i*j),end="     ")
#     print(" ")

import json
import re
import time

import requests


def get_one_page(url):
    headers ={
            'User-Agent':'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
    response = requests.get(url,headers=headers)
    if response.status_code == 200:
        return response.text
    return None


def parse_one_page(html,offset):
    pattern = re.compile('<div.*?post.*?img.*?src="(.*?)".*?</div>.*?title.*?_blank">(.*?)</a>.*?rating_nums">(.*?)</span>',re.S)
    items = re.findall(pattern,html)
    index = offset
    for item in items:
        index = index + 1
        yield {
            'index':index,
            'image':item[0],
            'title':item[1].strip(),
            'score':item[2]
            }

def write_to_file(content):
    with open("doubandushu.txt",'a',encoding='utf-8') as f:
        #print(type(json.dumps(content)))
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url = "https://www.douban.com/doulist/45004834/?"+'start='+str(offset)+'&sort=time&sub_type='
    html = get_one_page(url)
    for item in parse_one_page(html,offset):
        print(item)
        write_to_file(item)

if __name__=='__main__':
    for i in range(0,4):
        main(offset = i*25)
        time.sleep(1)
