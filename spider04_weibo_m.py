"""
爬取微博手机版微博列表
"""

import json
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup


def fetch(since_id):
    uri = "https://m.weibo.cn/api/container/getIndex?type=uid&value=6571964646&containerid=1076036571964646&since_id={}".format(since_id)
    print("fetch uri {}\n".format(uri))
    resp = requests.get(uri)
    if resp.status_code != 200:
        raise Exception("resp code: {}".format(resp.status_code))

    body_json = json.loads(resp.text)
    return body_json

def gettime(timestr):
    return datetime.strptime(timestr, "%a %b %d %H:%M:%S %z %Y")
    

def main():
    fetch_num = 0
    since_id = ""
    weibo_count = 0

    half_month = "2022-06-28"
    half_month = datetime.strptime(half_month, "%Y-%m-%d").astimezone()
    print("half_month {}".format(half_month))

    while True:
        fetch_num += 1
        print("fetch num {}\n".format(fetch_num))
        body_json = fetch(since_id)

        last_weibo = None
        for card in body_json['data']['cards']:
            if "profile_type_id" not in card:
                continue
            #去掉top微博
            if "top" in card['profile_type_id']:
                continue
            if card['card_type'] != 9:
                continue

            weibo_count += 1
            text = BeautifulSoup(card['mblog']['text'], 'lxml')
            assert(text)
            print("{} {} {} {}\n".format(weibo_count, card['mblog']['mid'], card['mblog']['created_at'], text.get_text()))
            last_weibo = card

        since_id = body_json['data']['cardlistInfo']['since_id']
        if since_id == "":
            print("since_id empty")
            break

        last_weibo_time = gettime(last_weibo['mblog']['created_at'])
        if last_weibo_time <= half_month: 
            print("last_weibo_time {} half_month {}".format(last_weibo_time, half_month))
            break

        # if fetch_num >= 5:
        #     print("fetch num >= 5")
        #     break

    print("handle done")

def test_gettime():
    res = gettime("Mon Jun 27 22:38:02 +0800 2022")
    print("res", res)


if __name__ == '__main__':
    main()
    # test_gettime()
