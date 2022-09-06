n = int(input())
n = n + 1 if n % 2 == 0 else n

flake = [[['.', '*']
          [j == i or ((n - j - 1) == i) or (i == n // 2) or j == n // 2]
          for j in range(n)]
         for i in range(n)]

for row in flake:
    for item in row:
        print(item, end=' ')
    print()
