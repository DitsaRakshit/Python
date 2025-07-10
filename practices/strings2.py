mixed_case = "A Song of Ice and Fire"
print(len(mixed_case))
print(mixed_case.isupper())
print(mixed_case.islower())
print(mixed_case.upper())
print(mixed_case.lower())
print(mixed_case.istitle())
title_case = mixed_case.title()
print(title_case)
print(mixed_case.startswith("A"))
print(mixed_case.endswith("e"))
word = mixed_case.split()
print(word)
print("".join(word).isalpha())
print(mixed_case.rjust(12))
print(mixed_case.ljust(2) + " " + "also called game of thrones")
print(mixed_case.ljust(30, "*"))
print(mixed_case.center(30, "$"))
print(mixed_case.rstrip("Fire"))
print(mixed_case.rstrip(",fr ie"))
print(mixed_case.lstrip("A"))
print(mixed_case.strip("A Song"))
print(mixed_case.replace("Fire", "Water"))
the_string = "North Dakota"
print(the_string.ljust(17, "*"))


#new program
word= input("enter a string")
word2= ""
for item in range(len(word) -1, -1, -1):
    word2 += word[item]

print(word2)


#new program
str1 = "i like ice-cream"
str2 = "today it has been raining very heavily"
str3 = "the best people i life are free"
def word_counter(words):
    return len(words.split())
print(word_counter(str1))
print(word_counter(str2))
print(word_counter(str3))

#different approach
txt = " the jungle is scary"
x = txt.split()
print(x)


#using format
n = input("enter name")
f = input("enter favourite fruit")
print("{} favourite fruit is {}".format(n, f))
