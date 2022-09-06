import math

P = int(input())
X = int(input())
Y = int(input())

X += (Y // 100) + (Y % 100) / 100

value = math.floor(X + (X * (P / 100)))

print(value)
