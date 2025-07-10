print(list("blah"))
check = [1, 2, 3, 4]
print(1 in check)
print( 3 not in check)

#new program
l1 = [4, 5.67, True, "i am a girl", [3, 78, 29]]
l2 = list("memymine")
print("e" in l2)
print("a" not in l2)

#list slicing
m = [2.5, 5.88, False, "my mane is"]
print(m[1] + 4.8)
print(str(m[1]) + m[3])
print(m[:2])
print(m[1:])
print(m[1:4])
m[1] = 7.99
print(m)


#new program on slicing
s = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(s[0])
print(s[3][1])
p = ["chair", "table", "desk", "lamp", "bed"]
print(p[-5])
print("most people own at least" + " " + str(s[0][1]) + " " + p[0] + "s")
q = [0.98, 8.76, 6.54, 4.32]
print(q[1:])
print(q[1:3])
print(q[:2])


#new program on list methods
arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
print(arctic_animals )
arctic_animals.remove("elephant")
print(arctic_animals )
arctic_animals.append("arctic fox")
print(arctic_animals )
arctic_animals.insert(3, "snowy owl")
print(arctic_animals )
arctic_animals.sort()
print(arctic_animals )
arctic_animals.index("reindeer")
print(arctic_animals )
print(arctic_animals.pop())


