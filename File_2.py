from pprint import pprint

def custom_write(file_name, strings):
    d = []
    file = open(file_name, "w", encoding="utf-8")
    for i in strings:
        d.append(file.tell())
        file.write(i+"\n")
    file.close()
    file = open(file_name, "r", encoding="utf-8")

    strings_positions = {}

    g = 0
    for i in file.readlines():
        strings_positions[(g+1, d[g])] = i[:-1]
        g += 1
    return strings_positions



file = "tttt.txt"
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write(file, info)
for elem in result.items():
  print(elem)
