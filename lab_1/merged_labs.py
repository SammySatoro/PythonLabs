import math
import random


#Задание 1 Сумма трёх чисел. Напишите программу, которая считывает
#три числа и выводит их сумму. Каждое число записано в отдельной строке.
def lab1task1():
    a = int(input())
    b = int(input())
    c = int(input())
    print(a + b + c)

# Задание 12 Шоколадка. Шоколадка имеет вид прямоугольника,
# разделенного на × долек. Шоколадку можно один раз разломить по
# прямой на две части. Определите, можно ли таким образом отломить от
# шоколадки часть, состоящую ровно из долек. Программа получает на вход
# три числа: , , и должна вывести YES или NO.
def lab2task12():
    n = int(input())
    m = int(input())
    k = int(input())

    answer = 'YES' if (k % n == 0 or k % m == 0) and k < n * m else 'NO'
    print(answer)

# Задание 16 Проценты. Процентная ставка по вкладу составляет
# процентов годовых, которые прибавляются к сумме вклада. Вклад составляет
# рублей копеек. Определите размер вклада через год.
# Программа получает на вход целые числа , , и должна вывести два
# числа: величину вклада через год в рублях и копейках. Дробная часть копеек
# отбрасывается.
def lab3task16():
    import math
    P = int(input())
    X = int(input())
    Y = int(input())

    X += (Y // 100) + (Y % 100) / 100

    value = math.floor(X + (X * (P / 100)))

    print(value)

# Задание 9 Количество нулей. Дано чисел: сначала вводится число ,
# затем вводится ровно целых чисел. Подсчитайте количество нулей среди
# введенных чисел и выведите это количество. Вам нужно подсчитать
# количество чисел, равных нулю, а не количество цифр.
def lab4task9():
    n = int(input())
    arr = [int(input()) for i in range(n)]
    print(arr.count(0))
    # zero_count = 0
    # for i in arr:
    #     if i == 0:
    #         zero_count += 1
    # print(zero_count)

# Задание 9 Замена подстроки. Дана строка. Замените в этой строке все
# цифры 1 на слово one.
def lab5task9():
    str = input()

    print(str.replace('1', 'one'))

    # res_str = ''.join([i, 'one'][i == '1'] for i in str)
    # print(res_str)

# Задание 14 Числа Фибоначчи. По данному числу n определите n-e число Фибоначчи .
# Эту задачу можно решать и циклом for.
def lab6task14():
    n = int(input())
    f1 = 0
    f2 = 1

    while n:
        f1, f2 = f2, f1 + f2
        n -= 1

    # for i in range(n):
    #     f1, f2 = f2, f1 + f2

    print(f2)

# Задание 12 Вставить элемент. Дан список целых чисел, число и
# значение . Необходимо вставить в список на позицию с индексом элемент,
# равный , сдвинув все элементы, имевшие индекс не менее , вправо.
# Поскольку при этом количество элементов в списке увеличивается,
# после считывания списка в его конец нужно будет добавить новый элемент,
# используя метод append.
def lab7task12():
    n = 10
    list = [int(i) for i in range(n)]
    k = int(input()) % n
    C = int(input())

    # list.insert(k, C)
    # list = list[:k] + [C] + list[k:]
    # list = list[:k] + [C] + [list[i] for i in range(k, n)]

    res_list = []

    for i in range(len(list)):
        if i == k:
            res_list.append(C)
            res_list.append(list[i])
        else:
            res_list.append(list[i])

    print(res_list)

# Задание 3 Большие буквы. Напишите функцию capitalize(), которая
# принимает слово из маленьких латинских букв и возвращает его же, меняя
# первую букву на большую.
def lab8task3():
    def capitalize(word):
        if (ord(word[0]) >= 97 and ord(word[0]) <= 122):
            return ''.join([chr(ord(word[0]) - 32)] + [char for char in word][1:])
        return word

    str = ' '.join([capitalize(word) for word in input().split()])

    print(str)

# Задание 2 Снежинка. Дано нечетное число . Создайте двумерный
# массив из × элементов, заполнив его символами «.» (каждый элемент
# массива является строкой из одного символа). Затем заполните символами «*»
# среднюю строку массива, средний столбец массива, главную диагональ и
# побочную диагональ. В результате единицы в массиве должны образовывать
# изображение звездочки. Выведите полученный массив на экран, разделяя
# элементы массива пробелами.
def lab9task2():
    n = int(input())
    n = n + 1 if n % 2 == 0 else n

    flake = [[['.  ', '*  ']
              [j == i or ((n - j - 1) == i) or (i == n // 2) or j == n // 2]
              for j in range(n)]
             for i in range(n)]

    for row in flake:
        for item in row:
            print(item, end=' ')
        print()

# Задание 10 Забастовки. Политическая жизнь одной страны очень
# оживленная. В стране действует политических партий, каждая из которых
# регулярно объявляет национальную забастовку. Дни, когда хотя бы одна из
# партий объявляет забастовку, при условии, что это не суббота или воскресенье
# (когда и так никто не работает), наносят большой ущерб экономике страны.
# i-я партия объявляет забастовки строго каждые дней, начиная с дня с
# номером . То есть i-я партия объявляет забастовки в дни , + ,
# + 2 ∙ и т.д. Если в какой-то день несколько партий объявляет забастовку,
# то это считается одной общенациональной забастовкой.
# В календаре страны дней, пронумерованных, начиная с единицы.
# Первый день года является понедельником, шестой и седьмой дни
# года – выходные, неделя состоит из семи дней.
# В первой строке даны числа и . Далее идет строк, описывающие
# графики проведения забастовок. -я строка содержит числа и . Вам нужно
# определить число забастовок, произошедших в этой стране в течении года.
def lab10task10():
    N, K = [int(i) for i in input().split()]
    start_gap = [[int(j) for j in input().split()] for i in range(K)]
    united = set()
    strike_dates = [united | {int(j) for j in range(i[0], N + 1, i[1])} for i in start_gap]
    for i in strike_dates:
        united ^= i
    print(united, '\n', len(united))

def lab11task7():
    countries = {'Russia' : ['Moscow', 'Petersburg', 'Novgorod', 'Kaluga'],
                 'Ukraine' : ['Kiev', 'Donetsk', 'Odessa'],
                 'Japan' : ['Osaka', 'Tokyo', 'Kyoto', 'Hiroshima']}
    cityCount = int(input())
    for i in range(cityCount):
        city = input()
        for country in countries:
            if city in countries[country]:
                print(country)



def lab12task19():
    import _io

    def checkLines(inFile: _io.TextIOWrapper, dict: _io.TextIOWrapper):
        text = inFile.read().split()
        words = dict.read().split()
        for word in text:
            if word not in words:
                return False
        return True

    fileName = input('Enter file name: ')
    isFileOpened = False

    while not isFileOpened:
        try:
            inputFile = open(fileName, 'r')
            dict = open('words.txt', 'r')
            isFileOpened = True
            print('The text is correct.' if checkLines(inputFile, dict) else 'The text is incorrect.')
        except FileNotFoundError:
            print('Invalid directory or file name. Try again.')
            fileName = input('Enter file name: ')

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


def lab11task6():
    n = int(input())
    lines = sum([input().split() for i in range(n)], [])
    wordsByCount = set(map(lambda item: (lines.count(item), item), lines))
    maxFreq = max(wordsByCount)[0]
    sortedByLex = sum([sorted(list(filter(lambda item: item[0] == i, wordsByCount))) for i in range(1, maxFreq + 1)], [])

    for i in sortedByLex:
        print(f'{i[1]} \t\t {i[0]}')


def lab11task13():

    def findAncestors(name, people):
        def loop(name, pairs, relatives):
            for pair in pairs:
                if name == pair[0]:
                    relatives.append(pair[1])
                    return loop(pair[1], pairs, relatives)
            return relatives
        rels = [name]
        return loop(name, people, rels)

    n = int(input())
    childToAncestorList = [input().split() for i in range(n - 1)]
    names = input().split()

    firstNameAnc = findAncestors(names[0], childToAncestorList)
    secondNameAnc = findAncestors(names[1], childToAncestorList)
    commonAncs = set(firstNameAnc) & set(secondNameAnc)

    print(firstNameAnc)
    print(secondNameAnc)
    if len(commonAncs) == 0:
        print('No such a Lowest Common Ancestor')
    else:
        print('Lowest Common Ancestor –', firstNameAnc[len(firstNameAnc) - 1])


def lab12task10():
    import _io

    inputFileName = input("Enter name of the input file: ")
    outputFileName = input("Enter name of the output file: ")

    isFileOpened = False

    while not isFileOpened:
        try:
            with open(inputFileName, "r", encoding='utf-8') as inputFile:
                with open(outputFileName, "w", encoding='utf-8') as outputFile:
                    lines = inputFile.readlines()
                    for i in lines:
                        if i.replace(' ', '')[0] != '#':
                            outputFile.write(i)

                    isFileOpened = True

        except FileNotFoundError:
            print('Invalid directory or file name. Try again.')
            inputFileName = input("Enter name of the input file: ")
            outputFileName = input("Enter name of the output file: ")

    inputFile.close()
    outputFile.close()

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


#lab1313131313131313131313


class Animal:

    __name: str

    def __init__(self, name):
        self.__name = name
        print(f"An animal called {name} was born!")

    @property
    def name(self): return self.__name

    @name.setter
    def name(self, name): self.__name = name

    def eat(self, foodName):
        print(f'{self.__name} is eating {foodName}...')

    def makeNoise(self):
        print(f'{self.__name}\'s saying grrrrhh...')

class Cat(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name)
        self.color = color
        self.weight = weight

    def makeNoise(self):
        print('Meow!')

class Dog(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name)
        self.color = color
        self.weight = weight
        print('A dog\'s just arrived')

    def makeNoise(self):
        print(f'{super().name}\'s saying woof...')


class StringVar:
    __value: str

    def __init__(self, value):
        self.__value = value
        print('StringVar variable has been instantiated: ', value)

    def set(self, value): self.__value = value

    def get(self): return self.__value

class Point:
    __x: float
    __y: float

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        print(f'x = {self.__x}\ty = {self.__y}')

    def setX(self, x): self.__x = x
    def getX(self): return self.__x
    def setY(self, y): self.__y = y
    def getY(self): return self.__y

def lab13():
    cat = Cat('Tom', 'Gray', 4)
    cat.makeNoise()

    animal = Animal('V')
    print('Animal\'s name is', animal.name)
    animal.name = 'David'
    animal.eat('apple')
    animal.makeNoise()

    strObj = StringVar('qwerty')
    print(strObj.get())
    strObj.set('abcdef')
    print(strObj.get())

    dog1 = Dog('Charlie', 'White', 10.5)
    dog1.name = 'Winston'
    print(dog1.name)
    dog1.makeNoise()
    dog1.eat('cookie')
    dog2 = Dog('Kot', 'Ginger', 9)
    dog2.name = 'Noah'
    print(dog2.name)
    dog2.makeNoise()
    dog2.eat('p**p')





def lab14():
    import tkinter

    def task1():

        def fahrToCels(fahr):
            return (fahr - 32) * (5 / 9)

        def click():
            resLabel.config(text=fahrToCels(int(entryBox.get())))

        root = tkinter.Tk()
        frame = tkinter.Frame(root).pack()
        root.resizable(width=False, height=False)
        tkinter.Label(text="Temperature in Fahrenheit", padx=5).pack(anchor='n')
        entryBox = tkinter.Entry(frame)
        entryBox.pack(anchor='n')
        resLabel = tkinter.Label(frame)
        resLabel.pack(anchor='n')
        tkinter.Button(frame, text='Print', command=click).pack(pady=5)
        tkinter.Button(frame, text='Quit', command=root.destroy).pack(pady=5)
        root.mainloop()

    def task2():
        import random
        import _io

        def getRuWord():
            ru_words_file = open('ruwords.txt', 'r', encoding='UTF-8')
            return random.choice(ru_words_file.read().split())


        from translate import Translator


        def guess():
            value = int(tries['text'][len(tries['text']) - 1])
            tries['text'] = f'Tries left: {value - 1}'
            if (value == 1):
                tries['text'] = 'You\'ve lost!'
                guessBtn['state'] = tkinter.DISABLED

            translator = Translator(from_lang='ru', to_lang='en')
            ru_text = ru_word['text']
            en_text = translator.translate(ru_text).lower().split()
            en_text = en_text[len(en_text) - 1]
            if entryBox.get() == en_text:
                tries['text'] = 'You win!'
                guessBtn['state'] = tkinter.DISABLED
            return en_text

        def reset():
            tries['text'] = 'Tries left: 3'
            ru_word['text'] = getRuWord()
            guessBtn['state'] = tkinter.ACTIVE
            ru_word['state'] = tkinter.ACTIVE

        def hint():
            print(guess())
            ru_word['state'] = tkinter.DISABLED
            entryBox.delete(0, tkinter.END)
            entryBox.insert(0, guess())

        root = tkinter.Tk()
        root.resizable(width=False, height=False)
        root.geometry('210x150')
        root['background']='#856ff8'

        f_top = tkinter.Frame(root)
        f_bot = tkinter.Frame(root)
        f_top['background']='#856ff8'
        f_bot['background']='#856ff8'

        ru_word = tkinter.Button(f_top, command=hint, width=12, height=1, text=getRuWord(), bg='#5B4CA9')
        entryBox = tkinter.Entry(f_top, width=20, bg='#AFB4FF')

        guessBtn = tkinter.Button(f_bot, width=5, height=1, text='Guess', command=guess, bg='#5B4CA9')
        resetBtn = tkinter.Button(f_bot, width=5, height=1, text='Reset', command=reset, bg='#5B4CA9')
        tries = tkinter.Label(f_bot, width=10, height=1, text=f'Tries left: 3', bg='#5B4CA9')

        f_top.pack(pady=20)
        f_bot.pack(pady=10)
        ru_word.pack(padx=10, pady=5)
        entryBox.pack(padx=10, pady=5)
        guessBtn.pack(side=tkinter.LEFT, padx=10)
        resetBtn.pack(side=tkinter.LEFT, padx=10)
        tries.pack(side=tkinter.LEFT, padx=10)

        root.mainloop()

    def task3():
        from tkinter import ttk
        from tkinter import filedialog

        def calculate():
            try:
                radius = int(radius_entry.get())
                V = (4 / 3) * math.pi * radius ** 3
                res_entry.delete(0, tkinter.END)
                res_entry.insert(0, V)
            except ValueError:
                res_entry.delete(0, tkinter.END)
                res_entry.insert(0, 'ERROR')

        def save():
            files = [('TXT File', '*.txt'),
                     ('HTML File', '*.html')]
            saving_format = select_list.current()
            print(saving_format)
            f = filedialog.asksaveasfile(mode='w', filetypes=[files[saving_format]])
            if f is None:
                return
            res_to_save = res_entry.get()
            f.write(res_to_save)
            f.close()

        root = tkinter.Tk()
        root.geometry('280x220')
        root.resizable(width=False, height=False)
        root['background'] = '#856ff8'
        root.title('Sphere radius')
        root.resizable()

        f_top = tkinter.Frame(root, bg='#856ff8')
        f_mid = tkinter.Frame(root, bg='#856ff8')
        f_bot = tkinter.Frame(root, bg='#856ff8')

        radius_label = tkinter.Label(f_top, text='Set radius:', bg='#AFB4FF')
        radius_entry = tkinter.Entry(f_top)

        res_label = tkinter.Label(f_mid, text='Calculation result:', bg='#AFB4FF')
        res_entry = tkinter.Entry(f_mid)

        calc_btn = tkinter.Button(text='Calculate', command=calculate, bg='#AFB4FF')

        save_btn = tkinter.Button(f_bot, text='Save', command=save, bg='#AFB4FF', width=8)
        select_list = ttk.Combobox(f_bot, values=['.txt', '.html'], background='#AFB4FF', width=10)

        f_top.pack(pady=30)
        f_mid.pack(pady=0)
        calc_btn.pack(pady=20)
        f_bot.pack(pady=0)

        radius_label.pack(side=tkinter.LEFT, padx=30)
        radius_entry.pack(side=tkinter.LEFT)
        res_label.pack(side=tkinter.LEFT, padx=10)
        res_entry.pack(side=tkinter.LEFT)
        save_btn.pack(side=tkinter.LEFT, padx=30)
        select_list.pack(side=tkinter.LEFT)

        root.mainloop()


    task2()

def indtask2var2():

    class SFloat():
        __negative_zero: str
        __whole: int
        __fractional: int

        def __init__(self, whole=0, fractional=0):
            if isinstance(whole, str):
                if (whole[0] == '-' and whole[1] == '0'):
                    self.__negative_zero = '-'
                else:
                    self.__negative_zero = ''
            else: self.__negative_zero = ''
            whole = int(whole)
            fractional = int(fractional)

            if isinstance(whole, int):
                self.__whole = int(whole)
            else:
                raise TypeError('Error: the \'whole\' parameter has wrong type')
            if isinstance(fractional, int):
                self.__fractional = int(str(divmod(float(f'0.{fractional}'), 1)[1])[2:])
                if (fractional < 0):
                    raise ValueError('Error: the \'fractional\' parameter should be greater than 0')
            else:
                raise TypeError('Error: the \'fractional\' parameter has wrong type')

        def SetWhole(self, value):
            if isinstance(value, str):
                if (value[0] == '-' and value[1] == '0'):
                    self.__negative_zero = '-'
                else:
                    self.__negative_zero = ''
            else:
                self.__negative_zero = ''
            whole = int(value)

            if isinstance(whole, int):
                self.__whole = int(whole)
            else:
                raise TypeError('Error: the \'whole\' parameter has wrong type')

        def GetWhole(self): return self.__whole

        def SetFractional(self, value):
            if isinstance(value, int):
                self.__fractional = int(str(divmod(float(f'0.{value}'), 1)[1])[2:])
                if (value < 0):
                    raise ValueError('Error: the \'fractional\' parameter should be greater than 0')
            else:
                raise TypeError('Error: the \'fractional\' parameter has wrong type')

        def GetFractional(self):
            return self.__fractional

        def __float__(self):
            return float(self.__str__())

        def __str__(self):
            return f'{self.__negative_zero}{self.__whole}.{self.__fractional}'

        def __num_len__(self, num):
            if num < 0: num = -num
            if num == 0: return 0
            return 1 + self.__num_len__(num // 10)

        def __add__(self, other):
            integer, fract = divmod(float(str(f'0.{self.__fractional}')) + float(str(f'0.{other.__fractional}')), 1)
            fract = round(fract, max(self.__num_len__(self.__fractional), self.__num_len__(other.__fractional)))
            self.__whole += other.__whole + int(integer)
            self.__fractional = int(str(fract)[2:])
            return self

        def __sub__(self, other):
            temp = round(float(self) - float(other), max(self.__num_len__(self.__fractional), self.__num_len__(other.__fractional)))
            print('temp =', temp)
            w_f = str(temp).split('.')
            self.__whole = int(w_f[0])
            self.__fractional = int(w_f[1])
            return self

        def __mul__(self, other):
            temp = round(float(self) * float(other), max(self.__num_len__(self.__fractional), self.__num_len__(other.__fractional)))
            print(temp)
            w_f = str(temp).split('.')
            self.__whole = int(w_f[0])
            self.__fractional = int(w_f[1])
            return self

    fl = SFloat('4', 5)
    fl2 = SFloat('2', 4)
    print(fl)
    print(fl2)
    print(fl * fl2)


def task15():
    import sqlite3
    from sqlite3 import Error

    def sql_connection():
        try:
            db = sqlite3.connect('pyserver.db')
            return db
        except Error:
            print(Error)

    def sql_table(con, query):
        cursorObj.execute(query)
        con.commit()

    def sql_insert(con, table, fields, values):
        placeholders = ', '.join('?' for i in fields)
        query = f"INSERT INTO {table}({', '.join(i for i in fields)}) VALUES ({placeholders})"
        try:
            cursorObj.execute(f"SELECT * FROM {table}")
            if values not in cursorObj.fetchall():
                cursorObj.execute(query, values)
                con.commit()
            else:
                print('This entry already exists')
                for value in cursorObj.execute("SELECT * FROM test"):
                    print(value)
        except Error:
            print('Entry with such entry ID already exists.\nTable:', table)

    con = sql_connection()
    cursorObj = con.cursor()
    sql_table(con, "CREATE TABLE IF NOT EXISTS test(id integer PRIMARY KEY, name text)")
    sql_insert(con, 'test', ('id', 'name'), (0, 'Alice'))

# demo
if __name__ == "__main__":
    lab15()
