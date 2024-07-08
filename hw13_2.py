num = input("Число")
while True:
    a = 0
    for i in num:
        a = a + int(i)
    if a <= 9:
        break
    else:
        num = str(a)
        continue
print("Сумма цифр", a)
