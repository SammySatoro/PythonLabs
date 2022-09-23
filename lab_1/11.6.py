def lab11task6():
    n = int(input())
    lines = sum([input().split() for i in range(n)], [])
    wordsByCount = set(map(lambda item: (lines.count(item), item), lines))
    maxFreq = max(wordsByCount)[0]
    sortedByLex = sum([sorted(list(filter(lambda item: item[0] == i, wordsByCount))) for i in range(1, maxFreq + 1)], [])

    for i in sortedByLex:
        print(f'{i[1]} \t\t {i[0]}')

# demo
if __name__ == "__main__":
    lab11task6()
