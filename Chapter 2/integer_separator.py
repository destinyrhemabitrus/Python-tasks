""" Exercise 2.11 """

number = int(input('Enter a five digit integer: '))

a = number // 10000
b = number % 10000
c = b // 1000
d = b % 1000
e = d / 100
f = e // 100
g = e % 100
h = g / 10
i = h // 10
j= h % 10

print(a, c, f, i, j)

question2_13.py
