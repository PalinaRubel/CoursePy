# №2 Все четные по значению элементы исходного списка A поместить в новый список B.
import random

A = []
B = []
n = int(input("Размер списка: "))

for i in range(n):
    a = random.randint(0, 100)
    A.append(a)
print(A)

for i in range(len(A)):
    if A[i] % 2 == 0:
        B.append(A[i])
print(B)
