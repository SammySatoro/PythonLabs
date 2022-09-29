def lab12task11():
    import _io
    from random import choice
    from random import randint
    try:
        with open("words.txt", "r", encoding='utf-8') as inputFile:
            words = sorted(list(filter(lambda word: 7 >= len(word) >= 3 ,inputFile.read().split())), key=len)
            wordsByLen = {i: [] for i in range(3, 8)}
            for word in words:
                wordsByLen[len(word)].append(word)
    # 3 4 5 6 7
            combs = {
                3: [5, 6, 7, ],
                4: [4, 5, 6, ],
                5: [3, 4, 5, ],
                6: [3, 4, ],
                7: [3],
            }
            firtsLen = random.randint(3, 7)
            secondLen = random.choice(combs[firtsLen])
            firstWord = random.choice(wordsByLen[firtsLen])
            secondWord = random.choice(wordsByLen[secondLen])
            password = firstWord[0].upper() + firstWord[1:] + secondWord[0].upper() + secondWord[1:]
            print(password)
            print(len(password))


    except FileNotFoundError:
        print('Invalid directory or file name. Try again.')

    inputFile.close()

# demo
if __name__ == "__main__":
    lab12task11()
