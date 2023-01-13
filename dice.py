import random

num1=random.choice([1,2,3,4,5,6])
num2=random.choice([1,2,3,4,5,6])
num3=random.choice([1,2,3,4,5,6])
num4=random.choice([1,2,3,4,5,6])
num5=random.choice([1,2,3,4,5,6])


if num1==6 and num2!=6:#1
    print(num1)
    print(num2)
    print("You can move out")
elif (num1==6 and num2==6) and (num3!=6):#2
    print(num1)
    print(num2)
    print(num3)
    print("You can move out")
elif (num1==6 and num2==6) and (num3==6):#3
    print(num1)
    print(num2)
    print(num3)
    print("Your turn is wasted")
elif (num1!=6 and num2!=6) and (num3!=6):#4
    print(num1)
    print(num2)
    print(num3)
    print("Your turn is wasted")
elif (num1!=6 and num2!=6) and num3==6 and num4==6 and num5==6:#5
    print(num1)
    print(num2)
    print(num3)
    print("Your turn is wasted")
elif (num1!=6 and num2!=6) and num3==6 and num4==6 and num5!=6:#6
    print(num1)
    print(num2)
    print(num3)
    print("You can move out")
elif (num1!=6 and num2!=6) and num3==6 and num4!=6:#7
    print(num1)
    print(num2)
    print(num3)
    print(num4)
    print("You can move out")
elif (num1!=6 and num2==6) and num3==6 and num4==6:#8
    print(num1)
    print(num2)
    print(num3)
    print("Your turn is wasted")
elif (num1!=6 and num2==6) and num3==6 and num4!=6:#9
    print(num1)
    print(num2)
    print(num3)
    print("You can move out")
elif (num1!=6 and num2==6) and num3==6 and num4==6:#10
    print(num1)
    print(num2)
    print(num3)
    print("Your turn is wasted")
elif num1!=6 and num2==6 and num3!=6:
    print(num1)
    print(num2)
    print(num3)
    print("You can move out")