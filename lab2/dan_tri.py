from urllib.request import urlopen
from bs4 import BeautifulSoup

# urllib
url = "https://dantri.com.vn"  # nho xoa dau / o cuoi duong link

#1. Download the page

#1.1 Open connection
conn = urlopen(url)

#1.2 Read data
raw_data = conn.read()

#1.3 Decode data
content = raw_data.decode("utf8")   # utf8 la dinh dang co the in khong phai tieng anh

# print(content)

# # Save file to research or debug
# f = open("dantri.html", "wb")   # w la mo ra de ghi, b la dinh dang tho
# f.write(raw_data)
# f.close()

#2. Find ROI
soup = BeautifulSoup(content, "html.parser")   # để cho beautifulsoup biết là đang muốn crawl data từ định dạng html
# print(soup.prettify())                # lam cho dep hon, lui html
ul_news = soup.find("ul", "ul1 ulnew")  # lan khac tim thi attribute phai ghi ro, vd: soup.find("ul", id="...")  # "u" la name trc class hoac id...
# print(ul_news.prettify())

#3. Copy n Save (excel)
li_list = ul_news.find_all("li")  # find tra ve 1 soup, find_all tra ve list soup
new_list = []
for li in li_list:   # li = li_list[0]  quet bang vong for
    #walking
    h4 = li.h4   # . co nghia la cua. h4 la cua li, a la cua h4
    a = h4.a
    link = url + a["href"]
    # print(link)
    title = a.string
    # print(title)
    # print(title, link)
    # print("----------------")
    news = {
        "title": title,
        "link": link,
    }
    # print(news)
    new_list.append(news)

print(new_list)