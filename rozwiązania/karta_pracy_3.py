# #1
n = int(input())
for i in range(0, n):
    print((i ** 3) + 3)

# #2
for i in range(105, 1000, 15):
    print(i)

#3
n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        print(i)

#4
suma = 0
for i in range(10, 100):
    suma = suma + i
print(suma)

#5
n = int(input())
suma = n * (n+1) / 2

for i in range(1, n+1):
    m = int(input())
    suma = suma - m
print(suma)

#6
n = int(input())
a = 0
b = 1
c = 0
for i in range(0, 2):
    print(i)
for j in range(0, n-2):
    c = a + b
    print(c)
    a = b
    b = c