import random

'''
generateFrames() description:
1. This function generates the frames using python random module.
2. This function returns the frames list.
'''
def generateFrames():
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
    return list1
rolls = generateFrames()
print(rolls)

'''
bowling_score(rolls) description:
1. This method returns the summation of all the values in the frames plus all bonus collected.
'''
def bowling_score(rolls):
    score = 0
    frame = 1
    roll_index = 0

    while frame <= 10:
        if rolls[roll_index] == 10:
            score += 10 + rolls[roll_index+1] + rolls[roll_index+2]
            roll_index += 1
        elif rolls[roll_index] + rolls[roll_index+1] == 10:
            score += 10 + rolls[roll_index+2]
            roll_index += 2
        else:
            score += rolls[roll_index] + rolls[roll_index+1]
            roll_index += 2
        frame += 1

    return score

total_score = bowling_score(rolls)
print(total_score)