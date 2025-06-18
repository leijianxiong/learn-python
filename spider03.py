"""
爬取微博列表 pc版

个人主页
种草小星星的最新微博 https://weibo.com/u/6571964646?profile_ftype=1&is_all=1#_0

目的 我想爬取半个月的，现在问题是不知道怎么分页
先爬一个下来看下
"""

import json
from re import A
import requests
from bs4 import BeautifulSoup
from urllib.parse import parse_qs
import time

def main():
    html = fetch02()

    #去掉空白
    html = html.replace("\t", "")
    html = html.replace("\r", "")
    html = html.replace("\n", "")

    soup = BeautifulSoup(html, 'lxml')
    assert soup

    articles = soup.find_all("div", attrs={"action-type":"feed_list_item"})
    assert len(articles)

    dates = []
    mids = []
    texts = []
    pic_ids = []

    for article in articles:
        mids.append(article['mid'])
        date_a = article.find("a", attrs={"node-type":"feed_list_item_date"})
        datetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(date_a['date'])/1e3))
        dates.append(datetime)

        text_div = article.find("div", attrs={"node-type":"feed_list_content"})
        #去掉首行和尾行
        #texts.append(text_div.prettify())
        texts.append(text_div.get_text())
        
        pic_tags = article.find_all("li", attrs={"action-type":"fl_pics"})
        each_pic_ids = []
        for pic_tag in pic_tags:
            param = parse_qs(pic_tag['action-data'])
            each_pic_ids.append(param['pic_id'][0])
        pic_ids.append(each_pic_ids)

        print("\n")

    no = 0
    for mid, date, text, each_pic_ids in zip(mids, dates, texts, pic_ids):
        no += 1
        print("{}: {} {} {} {}\n\n".format(no, mid, date, text, each_pic_ids))
    
def fetch01():
    uri = "https://weibo.com/u/6571964646?pids=Pl_Official_MyProfileFeed__18&profile_ftype=1&is_all=1&ajaxpagelet=1&ajaxpagelet_v6=1&__ref=%2Fu%2F6571964646%3Fprofile_ftype%3D1%26is_all%3D1%23_0&_t=FM_1656403180858120"
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        "cookie": "SINAGLOBAL=370085904757.4068.1598843763432; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W56qhF02XjKl0UPNI71kbTb5JpX5KMhUgL.FoMfeo.EShzRSKB2dJLoIEBLxKnLB--LB-BLxKMLB.zL1heLxKnL1K5LBK-LxK-L1K-L122t; wb_view_log_7529242854=1680*10502; ALF=1687932465; SSOLoginState=1656396466; SCF=AoHISgvzk8qmKqKDTzz_CeXgqcKYUpXC9ea1f9q0rhzinJJfnXg5JUvot0KR-kbBo_Vg8-_muHlFB9nknkPwSO8.; SUB=_2A25PvuriDeRhGeFL6VsT9CzEzjiIHXVsylsqrDV8PUNbmtAfLVjfkW9NQi_dNxmZNFae4rwiYQKRd9sP-nKv6YaY; _s_tentry=login.sina.com.cn; Apache=3635045060309.2563.1656396473512; ULV=1656396473635:19:3:1:3635045060309.2563.1656396473512:1655274289556; wvr=6; PC_TOKEN=8a4af2a949; webim_unReadCount=%7B%22time%22%3A1656404834128%2C%22dm_pub_total%22%3A6%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D",
    }
    resp = requests.get(uri, headers=headers)
    if resp.status_code != 200:
        print("response code {}".format(resp.status_code))
        return

    flen = len('<script>parent.FM.view(')
    elen = len(')</script>')
    json_body = resp.text[flen:-elen-1]

    body_dec = json.loads(json_body)
    html = body_dec['html']
    return html

def fetch02():
    uri = "https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&profile_ftype=1&is_all=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__18&id=1005056571964646&script_uri=/u/6571964646&feed_type=0&page=1&pre_page=1&domain_op=100505&__rnd=1656409502850"
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        "cookie": "SINAGLOBAL=370085904757.4068.1598843763432; UOR=,,login.sina.com.cn; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W56qhF02XjKl0UPNI71kbTb5JpX5KMhUgL.FoMfeo.EShzRSKB2dJLoIEBLxKnLB--LB-BLxKMLB.zL1heLxKnL1K5LBK-LxK-L1K-L122t; wb_view_log_7529242854=1680*10502; ALF=1687932465; SSOLoginState=1656396466; SCF=AoHISgvzk8qmKqKDTzz_CeXgqcKYUpXC9ea1f9q0rhzinJJfnXg5JUvot0KR-kbBo_Vg8-_muHlFB9nknkPwSO8.; SUB=_2A25PvuriDeRhGeFL6VsT9CzEzjiIHXVsylsqrDV8PUNbmtAfLVjfkW9NQi_dNxmZNFae4rwiYQKRd9sP-nKv6YaY; _s_tentry=login.sina.com.cn; Apache=3635045060309.2563.1656396473512; ULV=1656396473635:19:3:1:3635045060309.2563.1656396473512:1655274289556; wvr=6; PC_TOKEN=8a4af2a949; webim_unReadCount=%7B%22time%22%3A1656404834128%2C%22dm_pub_total%22%3A6%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A8%2C%22msgbox%22%3A0%7D",
    }
    resp = requests.get(uri, headers=headers)
    if resp.status_code != 200:
        print("response code {}".format(resp.status_code))
        return
    
    body_dec = json.loads(resp.text)
    html = body_dec['data']
    return html


if __name__ == '__main__':
    main()
