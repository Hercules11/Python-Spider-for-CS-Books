import sqlite3
import requests
from bs4 import BeautifulSoup
import time
import random


conn = sqlite3.connect('book_page.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books
                (book_name TEXT, amazon_link TEXT, pic_link TEXT, cate TEXT)''')

links = cursor.execute("SELECT * FROM link").fetchall()
total = cursor.execute("SELECT COUNT(*) FROM link").fetchone()[0]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

start = time.time()
for link in links:
    try:
        req = requests.get(url=link[1], headers=headers)
        time.sleep(random.random())
        cate = link[1][27:-5]
        req.encoding = 'utf-8'
        html = str(req.text).replace('<br>', ' ')
        soup = BeautifulSoup(html, 'lxml')
        contentList = soup.find_all('div1')
        for el in contentList:
            # print([el.text.lstrip(), el.myframe.a['href'], el.myframe.a.img['data-src'], cate])
            cursor.execute('''INSERT INTO books VALUES (?, ?, ?, ?)''', (el.text.lstrip(), el.myframe.a['href'], el.myframe.a.img['data-src'], cate))
        conn.commit()  # 每轮提交一次
        total -= 1
        print(f"{link[1]} finished, 剩下 {total} 项")
    except Exception as e:
        pass
    continue

# ...
# https://www.doradolist.com/technology-and-society.html finished, 剩下 3 项
# https://www.doradolist.com/wireless.html finished, 剩下 2 项
# https://www.doradolist.com/others.html finished, 剩下 1 项
# https://www.doradolist.com/nontechnical.html finished, 剩下 0 项
# 总用时：869.1676423549652
end = time.time()
print(f"总用时：{end - start}")

conn.close()
