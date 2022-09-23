def lab10var4():
    seq = [int(i) for i in input().split()]
    for i in range(len(seq)):
        print('YES' if seq[i] in seq[:i] else 'NO')

if __name__ == "__main__":
    lab10var4()
