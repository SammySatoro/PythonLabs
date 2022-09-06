
n = int(input())
m = int(input())
k = int(input())

answer = 'YES' if (k % n == 0 or k % m == 0) and k < n * m else 'NO'
print(answer)
