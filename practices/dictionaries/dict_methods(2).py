fruits = {"mango":"summer", "apple":"winter", "banana":"all year"}
vegetable = {"potato":"underground"}
fruits.update(vegetable)
f = fruits.copy()
fruits.clear()
print(f)
print(fruits)
