import math

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

#Задание 7 Страны и города. Дан список стран и городов каждой страны.
#Затем даны названия городов. Для каждого города укажите, в какой стране он
#находится.
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
                
# Задание 19 Проверяем правильность написания. Автоматическая
# проверка орфографии не помешала бы многим из нас. В данном задании мы
# напишем простую программу, сверяющую слова из текстового файла со
# словарем. Неправильно написанными будем считать все слова, которых не
# нашлось в словаре.               
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


# demo
if __name__ == "__main__":
    lab12task19()
