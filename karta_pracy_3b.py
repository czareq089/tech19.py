# 1
# print("\tListopad 2022")
#
# print("Pn\tWt\tŚr\tCw\tPt\tSb\tNd")
# d = 1
#
# print("\t", end="")
#
# for i in range(1, 31):
#
#     print(i,end="\t")
#     d += 1
#     if d == 7:
#         print()
#         d = 0

#2
# print("Potęgi liczb nieparzystych")
# n = int(input("\tZakres potęg: "))
#
# for i in range(1, n):
#
#     if i % 2 != 0:
#         print(i**2, end=" ")

#3
# for i in range(999, 10000):
#
#     if i % 379 == 0:
#         print(i, end=" ")
#
#     else:
#         pass

#4
# for i in range(100, 1000):
#
#     if i % 5 == 0:
#         print(i, end=" ")
#
#     elif i % 6 == 0:
#         print(i, end=" ")
#
#     elif i % 11 == 0:
#         print(i, end=" ")
#     else:
#         pass

#5
# n = int(input())
# l = []
# for i in range(0, n):
#     temp = int(input())
#     l.append(temp)
# print(sum(l))

#6
# k = int(input())
# for i in range(2, (k*2)+2,2):
#     suma = suma + i
# print(suma)

#7
# m = int(input())
# for i in range(11, (m*2)+2, 11):
#     suma = suma + i
# print(suma)

#8
# w = int(input("Kapital poczatkowy: "))
# r = int(input("Lata trwania inwestycji: "))
# wk = 0
# suma = w
# for i in range(1 , r*12):
#     kw=suma*0.06*(1/12)
#     suma = suma+kw
# print("Kapital koncowy bedzie wynosil: ", suma)

#9
# a = int(input())
# b = 21
# suma = 0
# for i in range(0, a+1):
#     for j in range(0, i, b):
#         suma = suma + j
#         j = j + 100
# print(suma)

#10
# from cmath import sqrt
# for i in range(1,1000):
#     if i % 10 == sqrt(i):
#         print(i)
#     elif i % 100 == sqrt(i):
#         print(i)