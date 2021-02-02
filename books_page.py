import requests
from bs4 import BeautifulSoup
import sqlite3

# 最终的要存储的推荐书籍内容页
BOOK_PAGE = []

# 符合匹配到关键字的再进行下载
KEY_WORD = ['AI', 'Algorithms', 'Coding', 'Cognitive', 'Computer', 'Computing',
            'Distributed', 'Info.', 'Math', 'Networking', 'NLP', 'Pattern',
            'System', 'wireless', 'Other', 'Security', 'Statistics', 'ML', 'Multi',
            'Crypto', 'Compiler', 'Program', 'Architecture', 'Operating', 'Database']


# 匹配到关键字才进行下载链接存储
def filterWord(string_link, word_list):
    for word in word_list:
        if word.lower() in string_link:
            return True
    return False


url = 'https://www.doradolist.com/main.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
req = requests.get(url=url, headers=headers)
req.encoding = 'utf-8'
html = req.text
soup = BeautifulSoup(html, 'lxml')
contentList = soup.center.find_all('a', limit=2)
url_list = []
for el in contentList:
    url_list.append("https://www.doradolist.com" + el['href'])
# print(url_list) 获得第一层跳转的链接 ['https://www.doradolist.com/universities.html', 'https://www.doradolist.com/subjects.html']


reqUniversities = requests.get(url=url_list[0], headers=headers)
reqUniversities.encoding = 'utf-8'
html = reqUniversities.text
soup = BeautifulSoup(html, 'lxml')
contentList = soup.center.next_sibling.find_all('a')
url_list_universities = []
for el in contentList:
    url_list_universities.append("https://www.doradolist.com" + el['href'])
# print(url_list_universities) 获得第二层跳转的链接 ['https://www.doradolist.com/stanford.html', 'https://www.doradolist.com/mit.html',
# 'https://www.doradolist.com/berkeley.html', 'https://www.doradolist.com/caltech.html', 'https://www.doradolist.com/uoft.html',
# 'https://www.doradolist.com/princeton.html', 'https://www.doradolist.com/harvard.html', 'https://www.doradolist.com/ucla.html',...


for university in url_list_universities:
    reqUniversitiesSubjects = requests.get(url=university, headers=headers)
    reqUniversitiesSubjects.encoding = 'utf-8'
    html = reqUniversitiesSubjects.text
    soup = BeautifulSoup(html, 'lxml')
    contentList = soup.find_all("center", limit=2)
    content = contentList[1] if len(contentList[1]) > len(contentList[0]) else contentList[0]
    for el in content.find_all('a'):
        subjectsLink = el['href']
        if filterWord(subjectsLink, KEY_WORD):
            BOOK_PAGE.append("https://www.doradolist.com" + subjectsLink)


reqSubjects = requests.get(url=url_list[1], headers=headers)
reqSubjects.encoding = 'utf-8'
html = reqSubjects.text
soup = BeautifulSoup(html, 'lxml')
contentList = soup.center.find_all('a')
for el in contentList:
    subjectsLink = el['href']
    if filterWord(subjectsLink, KEY_WORD):
        BOOK_PAGE.append("https://www.doradolist.com" + subjectsLink)
# print(url_list_subjects) 获得第三层的跳转链接, 从科目达到书籍页面 ['https://www.doradolist.com/ai.html', 'https://www.doradolist.com/algorithms.html',
# 'https://www.doradolist.com/analog.html', 'https://www.doradolist.com/antennas.html', 'https://www.doradolist.com/biomedical.html',
# 'https://www.doradolist.com/circuits.html', 'https://www.doradolist.com/cns.html', 'https://www.doradolist.com/coding.html',...


# print(BOOK_PAGE)
# print(len(BOOK_PAGE)) ['https://www.doradolist.com/stanford-algorithms.html', 'https://www.doradolist.com/stanford-antenna.html', ...
# 443

conn = sqlite3.connect('book_page.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE link
             (id INTEGER, url TEXT)''')

# Insert a row of data
cursor.executemany("INSERT INTO link VALUES (?, ?)", [((BOOK_PAGE.index(el) + 1), el) for el in BOOK_PAGE])

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
