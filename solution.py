n = int(input())
notebook = dict()
for i in range(0, n):
    row = str(input()).split(' ')
    if row[1] in notebook:
        notebook[row[1]].append(row[0])
    else:
        notebook[row[1]] = [row[0]]

n = int(input())
for i in range(0, n):
    name = input()
    if name in notebook:
        print(" ".join(notebook[name]))
    else:
        print("Нет в телефонной книге")