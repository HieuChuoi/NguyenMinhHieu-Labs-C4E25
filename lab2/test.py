from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://dantri.com.vn"

conn = urlopen(url)

raw_data = conn.read()

content = raw_data.decode("utf8")

# f = open("bao.html", "wb")
# f.write(raw_data)
# f.close

soup = BeautifulSoup(content, "html.parser")
ul_news = soup.find("ul", "ul1 ulnew")

li_list = ul_news.find_all("li")
new_list = []
for li in li_list:
    h4 = li.h4
    a = h4.a
    link = url + a["href"]
    title = a.string
    news = {
        "title": title,
        "link": link
    }
    new_list.append(news)

print(new_list)