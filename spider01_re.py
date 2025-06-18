"""
爬虫01 微博详情 正则匹配
"""

import requests
from bs4 import BeautifulSoup
import re


def main():
    uri = "https://m.weibo.cn/status/4776785189014035"
    print("get url {}".format(uri))
    resp = requests.get(uri)
    if resp.status_code != 200:
        raise Exception("resp code {}".format(resp.status_code))

    # 解析得到博文内容
    match_res = re.search(r'"text":\s?"(.*)",', resp.text, re.M)
    if match_res is None:
        print("not matched")
        return
    print("text: {}".format(match_res.group(1)))

    # pics
    match_res = re.search(r'"pic_ids":\s?\[\n\s*(.*?)\n\s*\],', resp.text, re.M|re.S)
    if match_res is None:
        print("not matched")
        return
    print("pic_ids: {}".format(match_res.group(1)))


    print("handle done")


if __name__ == "__main__":
    main()
