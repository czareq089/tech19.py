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
if (a + g) / 2 > sqrt(a * g) : print("tak, średnia arytmetyczna jest większa")
else : print("nie, średnia erytmetyczna jest mniejsza")

#==============================================

#3
k = int(input("Podaj liczbe1: "))
l = int(input("Podaj liczbe2: "))
m = int(input("Podaj liczbe3: "))
if k == l and k == m and l == m:
    print("Wszystkie liczby sa sobie rowne")
    if k == l: print("liczba1 i liczba2 sa sobie rowne")
    elif k == m: print("liczba1 i liczba3 sa sobie rowne")
    elif l == m: print("liczba2 i liczba3 sa sobie rowne")
else:
    print("Nie ma rownych sobie liczb")

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
else:
    print("są przynajmniej dwie najmniejsze liczby")
#==============================================

#5

a = int(input())
b = int(input())
c = int(input())

if a + b > b + c > a and a + c > b:
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

