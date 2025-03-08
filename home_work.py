summ = 0
# бул цикл чексиз цикл
while True:
    number = int(input("Enter the number: "))
    if number == 0:
        #  break бул циклдын ишин токтотот
        break
    summ += number
    print(f"all summ = {summ}")
