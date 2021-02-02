import sqlite3
import os

universities = ['Stanford', 'MIT', 'Berkeley', 'Caltech', 'U of T', 'Princeton',
                'Harvard', 'UCLA', 'USC', 'Oxford', 'Cambridge', 'CMU', 'EPFL']

conn = sqlite3.connect('book_page.db')
cursor = conn.cursor()

books = cursor.execute('SELECT * FROM books').fetchall()


def text_format(string):
    result = ""
    if string.startswith("https://"):
        return string
    elif string.startswith("/images/"):
        return "https://www.doradolist.com" + string
    for index in range(len(string)):
        if string[index] == '\n':
            result += ' '
        elif string[index] in ['-', '_']:
            result += ' '
        else:
            result += string[index]
    return result


def selector(string, source):
    for ob in source:
        compare = ob.lower().replace(' ', '')
        if string.split()[0] in compare:
            return ob
    return None


books_data = {}
for book in books:
    name = text_format(book[0])
    if name in books_data:
        books_data[name][3] += 1
        if (selector(text_format(book[3]), universities) not in books_data[name][2]) and selector(text_format(book[3]), universities) is not None:
            books_data[name][2].append(selector(text_format(book[3]), universities))
    else:
        books_data[name] = [text_format(book[1]), text_format(book[2]), [selector(text_format(book[3]), universities)], 1]

for line in sorted(books_data.items(), key=lambda kv: (kv[1][-1], kv[0]), reverse=True):
    print(line, '\n')
print("总计：", len(books_data))
# 写入完整列表
if os.path.exists("complete_list.md"):
    os.remove("complete_list.md")

md_file = open("complete_list.md", 'w', encoding='UTF-8')
md_file.write("| 书籍 |  | 推荐次数( >= 10) | 用作 推荐教材 的大学 |\n\
| :----:| :---: | :----: | ------|\n")

for line in sorted(books_data.items(), key=lambda kv: (kv[1][-1], kv[0]), reverse=True):
    md_file.write(f"| 《[{line[0]}]({line[1][0]})》 | <img src=\"{line[1][1]}\" width=\"50%\"> | {line[1][3]} | {', '.join([el for el in line[1][2] if el is not None])} |\n")

total = sum([num[-1] for num in books_data.values()])
md_file.write(f"合计： {total}")  # 合计： 2345
md_file.close()

conn.close()
