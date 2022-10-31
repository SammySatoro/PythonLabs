def indtask2var2():

    class SFloat():
        __negative_zero: str
        __whole: int or str
        __fractional: int or str

        def __init__(self, whole=0, fractional='0'):
            if isinstance(whole, str):
                if (whole[0] == '-' and whole[1] == '0'):
                    self.__negative_zero = '-'
                else:
                    self.__negative_zero = ''
            else: self.__negative_zero = ''
            whole = int(whole)
            fractional = fractional

            if isinstance(whole, int):
                self.__whole = int(whole)
            else:
                raise TypeError('Error: the \'whole\' parameter has wrong type')
            if isinstance(fractional, int) or isinstance(fractional, str):
                self.__fractional = fractional
                if (float(fractional) < 0):
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
            if isinstance(value, int) or isinstance(value, str):
                self.__fractional = value
                if (float(value) < 0):
                    raise ValueError('Error: the \'fractional\' parameter should be greater than 0')
            else:
                raise TypeError('Error: the \'fractional\' parameter has wrong type')

        def GetFractional(self):
            return self.__fractional

        def __float__(self):
            return float(self.__str__())

        def __str__(self):
            return f'{self.__negative_zero}{self.__whole}.{self.__fractional}'

        def __add__(self, other):
            res = float(str(self)) + float(str(other))
            separ = str(res).split('.')
            self.__whole = int(separ[0])
            self.__fractional = separ[1]
            return self

        def __sub__(self, other):
            res = float(str(self)) - float(str(other))
            separ = str(res).split('.')
            self.__whole = int(separ[0])
            self.__fractional = separ[1]
            return self

        def __mul__(self, other):
            res = float(str(self)) * float(str(other))
            separ = str(res).split('.')
            self.__whole = int(separ[0])
            self.__fractional = separ[1]
            return self

    fl = SFloat(4, 42)
    fl2 = SFloat('2', 43)
    print('fl =', fl)

    print(fl + fl2, "   ", 4.42 + 2.43)
    print(SFloat(10, 100) + SFloat(10, 900), "   ", 10.100 + 10.900)
    print(SFloat(10, '0123') + SFloat(10, '0127'), "   ", 10.0123 + 10.0127)
    print(SFloat(-10, '0123') - SFloat(10, '0127'), "   ", -10.0123 - 10.0127)
    print(SFloat('-10', '05') * SFloat(10, 12), "   ", -10.05 * 10.12)

    fl.SetFractional(55)
    print(fl)
    fl.SetWhole('10')
    print(fl)

    print(f'{fl.GetWhole()}.{fl.GetFractional()}')
