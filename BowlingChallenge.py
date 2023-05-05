import random
list1 = []

for i in range(1,11):
    if i == 10:
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10-num1 if num1<10 else 10)
        list1.append(num1)
        list1.append(num2)
        if num1 + num2 >=10:
            num3 = random.randint(0, 10-num2 if num2<10 else 10)
            list1.append(num3)
        continue
    num1 = random.randint(0,10)
    num2 = random.randint(0,10-num1)
    if num1 ==10:
        list1.append(num1)
        continue
    list1.append(num1)
    list1.append(num2)
print(list1)