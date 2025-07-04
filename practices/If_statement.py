from itertools import count

veg = input("enter the name of a vegetable")

if veg == "corn":
    print("the veg is corn")

else:
    print("wrong input")


p = int(input("enter class 12 percentage"))
if p>=90:
    s = input("enter stream")
    if s == "science":
        print("engineering college")

    else:
        print("arts college")

else:
    print("not fit for bachelors")


marks = int(input("enter marks"))
if marks>=90:
    print("A")
else:
    if marks>=80 and marks<90:
        print("B")
    else:
        if marks>=70 and marks<80:
            print("C")
        else:
            if marks>=60 and marks<70:
                print("D")
            else:
                print("F")



pwd = input("enter password")
pwd2 = len(pwd)
if pwd2<6:
    print("very weak")
else:
    if pwd2>=6 and pwd2<8:
        print("weak")
    else:
        if pwd2>=8 and pwd2<10:
            print("moderate")
        else:
            if pwd2>=10 and pwd2<12:
                print("strong")
            else:
                if pwd2>=12:
                    print("very strong")


from random import randint
n = randint(1, 10)

if n == 1:
    print("I")
elif n == 2:
    print("II")
elif n == 3:
    print("III")
elif n == 4:
    print ("IV")
elif n== 5:
    print("V")
elif n== 6:
    print("VI")
elif n == 7:
    print("VII")
elif n == 8:
    print("VII")
elif n==9:
    print("IX")
elif n==10:
    print("X")
else:
    print("not valid")