#WHILE LOOP
#program_1
num = 10
while num > 0:
    print(num)
    num-=1


#program_2
pos = int(input("enter a positive integer"))
pos2 = pos
summed = 0
while pos > 0:
    summed+= pos
    pos-=1

print(pos2)
print(summed)


#FOR LOOP
#program_1
word = "hello world"
for letter in word:
    print(letter)


#program_2
var = input("enter a word")
count = 0
for char in var:
    count+=1
print(var)
print(count)


#range()
number = range(5)
for n in number :
    print(n)


