n = int(input())
f1 = 0
f2 = 1

while n:
    f1, f2 = f2, f1 + f2
    n -= 1

# for i in range(n):
#     f1, f2 = f2, f1 + f2

print(f2)
