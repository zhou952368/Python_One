import json
import requests
from requests.exceptions import RequestException
import re
import time
def get_one_page(url):
    try:
        headers = {#请求头
           'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) +'
                        'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:  #抛出异常
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)  #正则表达式
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0], #网址
            'image': item[1],#图片
            'title': item[2],#作品名
            'actor': item[3].strip()[3:],#演员
            'time': item[4].strip()[5:],#时间
            'score': item[5] + item[6]#评分
        }


def write_to_file(content):
    with open('文件.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)
