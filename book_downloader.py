import sqlite3

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

print(sorted(books_data.items(), key=lambda kv: (kv[1][-1], kv[0]), reverse=True))
# [('Elements of Information Theory', 18), ('Pattern Recognition and Machine Learning', 17),
# ('Introduction to Algorithms', 16), ('The Elements of Statistical Learning', 15),
# ('Signals and Systems', 13), ('Introduction to the Theory of Computation', 13),
# ('Speech and Language Processing', 11), ('Wireless Communications', 10),
# ('Pattern Classification', 10), ('Introduction to Probability', 10), ('Deep Learning', 10),
total = sum([num[-1] for num in books_data.values()])
print(f"合计： {total}")  # 合计： 2345
