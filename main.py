print("Hello")
num_sym="123"
let_sym="XO"
print("Новая игра")
cnt_moves=9
hist=[["!", "*", "!"], ["*", "_", "*"], ["!", "*", "!"]]
for i in range(3):
    print(hist[i])
while cnt_moves>0:
    if cnt_moves%2!=0:
        a=str(input("Игрок1: введите номер столбца, номер строки и X/O без пробелов: "))
    else:
        a=str(input("Игрок2: введите номер столбца, номер строки и X/O без пробелов: "))
    if len(a)==3 and (a[:1] in num_sym and a[1:2] in num_sym and a[2:] in let_sym) and\
        hist[int(a[:1])-1][int(a[1:2])-1] in ["!", "_", "*"]:
        cnt_moves-=1
        hist[int(a[:1])-1][int(a[1:2])-1]=a[-1]
    else: print("ИЗМЕНИТЕ ИСХОДНЫЕ ДАННЫЕ")
