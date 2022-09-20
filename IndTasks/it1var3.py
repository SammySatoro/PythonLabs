def indTask1var3():
  from itertools import combinations_with_replacement
  
    def preSort(list: list, item):
        if len(list) >= 2:
            for i in range(len(list)):
                if item > list[len(list) - 1]:
                    list.append(item)
                if item <= list[i]:
                    list.insert(i, item)
                    break

        elif len(list) == 1:
            list.append(item) if list[0] <= item else list.insert(0, item)
        else:
            list.append(item)

    def findIncement(sum):
        for i in range(10):
            if (sum + i) % 10 == 4:
                return i

    def minSum(file, subts):
        sum = 0
        pairsCount = int(file.readline())
        pairs = file.read().split()
        pairsList = []
        for i in range(0, pairsCount * 2, 2):
            pairMax = max(int(pairs[i]), int(pairs[i + 1]))
            pairMin = min(int(pairs[i]), int(pairs[i + 1]))
            if (pairMax - pairMin) % 10 != 0:
                preSort(subts[(pairMax - pairMin) % 10], pairMax - pairMin)
            sum += pairMin
            pairsList.append([int(pairs[i]), int(pairs[i + 1])])
        return sum


    def findAdjustmentSum(dict, sum, inc):
        combs = []
        combWord = ''
        for k, v in dict.items():
            if len(v) != 0:
                combWord += str(k)
        print(combWord)
        for i in range(1, 10):
            for j in combinations_with_replacement(combWord, i):
                incAdjustment = 0
                for k in j:
                    incAdjustment += int(k)
                if incAdjustment == inc:
                    combs.append(j)
        if len(combs) == 0:
            print('There is no such a sum')
            return None

        adjustmentSums = [0 for i in range(len(combs))]
        for comb in combs:
            for key in comb:
                adjustmentSums[combs.index(comb)] += dict[int(key)][0]
        print(combs)
        return min(adjustmentSums)



    try:
        aFile = open('3a.txt', 'r')
        bFile = open('3b.txt', 'r')
        subts = {i : [] for i in  range(1, 10)}
        sum = minSum(bFile, subts)
        inc = findIncement(sum)
        print(inc, sum, subts)
        print('Minimal sum ending in 4 is: ', sum + findAdjustmentSum(subts, sum, inc))

    except FileNotFoundError:
        print('Invalid directory or file name. Try again.')
    finally:
        aFile.close()
        bFile.close()
# demo
if __name__ == "__main__":
    indTask1var3()
