a = {}
for i in iter(input, ''):
    a[' '.join(i.split()[:-1])] = a.get(' '.join(i.split()[:-1]), []) + [int(i.split()[-1])]
b = input()
if b in a:
    c1, c2, res = sum(a[b]), len(a[b]), 0
    while True:
        if c1 / c2 > 4.5 and c2 >= 3:
            break
        c1, c2, res = c1 + 5, c2 + 1, res + 1
    print(res)
else:
    print('Нет предмета')