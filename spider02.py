import requests
from bs4 import BeautifulSoup

def main():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }
    uri = "https://movie.douban.com/chart"
    resp = requests.get(uri, headers=headers)
    print("resp code = {}".format(resp.status_code))

    init_page = resp.text
    init_soup = BeautifulSoup(init_page, "lxml")

    titles = []
    summaries = []

    for table in init_soup.find_all("table"):
        titles.append(table.find("a")["title"])
        summaries.append(table.find("p").get_text())

    for title, summary in zip(titles, summaries):
        print("{} {}".format(title, summary))

if __name__ == '__main__':
    main()