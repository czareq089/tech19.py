#==============================================
#1
a = int(input())
b = int(input())

if (a + b) % 2 == 0:
    print("jest parzysta")
else:
    print("nie jest parzysta")

#==============================================

#2

from math import sqrt
a = float(input())
g = float(input())
if (a + g) / 2 > sqrt(a * g) : 
    print("tak, średnia arytmetyczna jest większa")
else :
    print("nie, średnia erytmetyczna jest mniejsza")

#==============================================

#3
k = int(input())
l = int(input())
m = int(input())


if k == l or l == m or k == m:
    print ("tak")
else:
    print("nie")

#==============================================

#4
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < b and a < c and a < d:
    print (a)
elif b < a and b < c and b < d:
    print (b)
elif c < a and c < b and c < d:
    print (c)
 elif d < a and d < b and d < c:
    print (d)

#==============================================

#5

a = int(input())
b = int(input())
c = int(input())

if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b :
    print("tak, spełnia nierówność")
else:
    print("nie spełnia nierówności")

#==============================================

#6

a = int(input())
b = int(input())
c = int(input())
if a < b + c and b < a + c and c < a + b :
    print("ten trójkąt może powstać")
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2 :
        print("trójkat będzie prostokątny")
    elif a**2 + b**2 < c**2 or b**2 + c**2 < a**2 or c**2 + a**2 < b**2 :
        print("trójkąt będzie rozwartokątny")
    elif a**2 + b**2 > c**2 or b**2 + c**2 > a**2 or c**2 + a**2 > b**2 :
        print("trójkąt będzie ostrokątny")
else :
    print("ten trójkąt nie może postać")

