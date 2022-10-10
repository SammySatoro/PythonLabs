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

# demo
if __name__ == "__main__":
    indtask2var2()
