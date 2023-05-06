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
len_of_ele = len(list1)
print(len_of_ele)


sum = 0
for position, value in enumerate(list1):
    print(position, value)
    if len_of_ele == 21 and (list1[len_of_ele-2] == 10 or (list1[len_of_ele-2] + list1[len_of_ele-1])== 10):
        sum = sum + value + list1[len_of_ele-2] + list1[len_of_ele-1]
    elif len_of_ele <= 21:
        sum = sum + value

print(sum)