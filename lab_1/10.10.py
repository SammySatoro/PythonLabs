def lab10task10():
    N, K = [int(i) for i in input().split()]
    start_gap = [[int(j) for j in input().split()] for i in range(K)]
    united = set()
    strike_dates = [united | {int(j) for j in range(i[0], N + 1, i[1])} for i in start_gap]
    for i in strike_dates:
        united ^= i
    print(united, '\n', len(united))
