def hamming(n: int) -> int:
    '''
    Calculate the Hamming numbers
    :param n: Hamming number required
    :return: nth Hamming number
    :example: print(hamming(5000))
    '''
    mas = []
    a2 = 1
    for i in range(1, 50):
        a3 = 1
        for j in range(1, 50):
            a5 = 1
            for k in range(1, 50):
                mas.append(a2 * a3 * a5)
                a5 *= 5
            a3 *= 3
        a2 *= 2
    mas.sort()
    return mas[n-1]


def decompose(n: int) -> int:
    '''
    Decompose input number (if n=11, output: [1, 2, 4, 10], explain: 1**2 + 2**2 + 4**2 + 10**2 == 11**2)
    :param n: Input number to decompose
    :return: Result of decompose
    '''
    summ = 0
    end = [n]
    while end:
        cur = end.pop()
        summ += cur ** 2
        for i in range(cur - 1, 0, -1):
            if summ - (i ** 2) >= 0:
                summ -= i ** 2
                end.append(i)
                if summ == 0:
                    end.reverse()
                    return end
    return None


class RomanNumerals(object):

    @staticmethod
    def to_roman(number):
        '''Str roman to int
        :param number: int like 1616
        :return: roman like 'MDCXVI'
        :example: print(RomanNumerals.from_roman(1616))'''
        dict = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        string = list(str(number))
        lst = []
        roman = ''
        lst.append(int(string[len(string) - 1]))
        string = string[::-1]
        for dec in range(1, 4):
            if len(string) <= 1: break
            if string[dec]: lst.append(int(string[dec]) * (10 ** dec))
        lst = lst[::-1]
        sortkeys = sorted(dict.keys())[::-1]
        for element in lst:
            i = 0
            for sort in sortkeys:
                while element:
                    value = element - sort
                    if value >= 0:
                        roman += dict[sort]
                        element -= sort
                        continue
                    else:
                        value = abs(value)
                        if dict.get(value):
                            roman += dict[value]
                            roman += dict[sort]
                            element -= sort - value
                        elif dict.get(value * 2):
                            roman += dict[value] * 2
                            roman += dict[sort]
                            element -= sort - value * 2
                        else:
                            break
        return roman

    @staticmethod
    def from_roman(roman):
        '''
        Str roman to int
        :param roman: string like 'MDCXVI'
        :return: number int 1616
        :example: print(RomanNumerals.from_roman('MDCXVI'))
        '''
        dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        number = 0
        prev = 0
        for i in range(len(roman) - 1, -1, -1):
            if prev <= dict[roman[i]]:
                number += dict[roman[i]]
                prev = dict[roman[i]]
            else:
                number -= dict[roman[i]]
        return number
