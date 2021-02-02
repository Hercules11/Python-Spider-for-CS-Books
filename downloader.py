import sqlite3
import requests
from bs4 import BeautifulSoup
import time
import random

book_needed = []

conn = sqlite3.connect('book_page.db')
cursor = conn.cursor()

words = cursor.execute("SELECT book_name,pic_link FROM books").fetchall()


def text_format(string):
    result = string.replace('-', ' ').replace('_', ' ').replace('...', '')
    return result.split()


for word in words:
    search_word = ""
    if '\n' in word[0]:
        search_word = word[0].replace('\n', ' ')
    else:
        search_word = word[0]

    author_info = text_format(word[1][8:-4])
    for single in author_info:
        if single in search_word:
            continue
        else:
            search_word += (' ' + single)
    if search_word not in book_needed:
        book_needed.append(search_word)

print(book_needed)
print("total: ", len(book_needed))
conn.close()
