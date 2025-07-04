from tkinter.font import names

s = "Just do it!"
print(s[10])
print(s[5:7])
print(s[:4])
s1 = (s[5:11])
con = "dont" + " " + s1
print(con)
a = False
print(type(a))
b = str(45)
print(type(b))


print("*******" + "\n\x20*****" + "\n\x20\x20***")
print("hello\x20world")
print("*******\n *****\n  ***\n   *")


def di_tsa():
    print(2+2)

di_tsa()

st = "the number"


def ari_jit(p1, p2, p3):
    print(p1+ str(p2) + p3)


ari_jit(st,5, "is an integer")

def bony(num1=7, num2=8):
    return num1*num2
print(bony()+ 55)

bony()


def hello_world_printer():
    print("hello world")

hello_world_printer()




l = int(input("enter length"))
w  = int(input("enter width"))
h  = int(input("enter height"))

def prism(l, w, h):
    return l*w*h

print("the vol is" +  str(prism(l, w, h)))


def far(cel):
    return round(1.8*cel+32, 1)
cel = int(input("enter temp in celsius"))
print("the far equivalent of" + str(cel) + "degrees Celsius is" + str(far(cel)))














