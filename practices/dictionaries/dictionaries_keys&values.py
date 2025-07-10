n = {"a" : 1, "b" : 2, "c" :3, "d" : 4, "e" : 5, "f" : 6}
print(len(n))
for key in n.keys():
    print(key)
print(n.values())
for key, value in n.items():
    print(key, value)
print(n.get(8, "not here"))


