#1
a = int(input())

if a % 3 == 0:
    print("jest podzielna")
else:
    print("nie jest podzielna")

#2
a = int(input())
if a > 100 and a < 1000 and a % 17 == 0:
    print("jest trzycyfrowa i podzielna przez 17")
elif a < 100 and a % 17 == 0:
    print("ma mniej niż trzy cyfry ale jest podzielna przez 17")
elif a > 999 and a % 17 == 0:
    print("ma więcej niż trzy cyfry ale jest podzielna przez 17")
elif a > 100 and a < 1000 and a % 17 != 0:
    print("ma trzy cyfry ale nie dzieli się przez 17")
elif a < 100 and a % 17 != 0:
    print("ma mniej niż trzy cyfry i nie jest podzielna przez 17")
elif a > 999 and a % 17 != 0:
    print("ma więcej niż trzy cyfry i nie jest podzielna przez 17")

#3
wiek = int(input())
if wiek >= 18:
    print("jesteś pełnoletni")
else:
    print("nie jesteś pełnoletni")

#4
limit = 20
waga = int(input())

if waga >= limit:
    print("nie wjedziesz")
else:
    print("zapraszamy")

#5
a = int(input())
b = int(input())
c = int(input())

if c > a and c < b:
    print("TAK")
elif c < a and c > b:
    print("TAK")
else:
    print("NIE")

#6
a = int(input())
p = int(input())

if (a**p - a) % p == 0:
    print("TAK")
else:
    print("NIE")

#7
p = int(input())
k = int(input())
s = int(input())
if (k-p) <= 3*s:
  print("TAK")
else:
  print("NIE")