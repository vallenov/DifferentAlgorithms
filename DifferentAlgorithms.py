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


def snail(snail: list) -> list:
    '''
    Convert array from [[ 1,  2,  3, 4],
                                    [12, 13, 14, 5],
                                    [11, 16, 15, 6],
                                    [10,  9,  8, 7]]
    to [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    :param snail: array NxN [[], [], []]
    :return: array []
    '''
    count = len(snail[0])-1
    i = 0
    j = count
    end = snail[0]
    value = 0
    alg = ['d', 'l', 'u', 'r']
    dic = {'d': (1,0), 'l': (0,-1), 'u': (-1,0), 'r': (0,1)}
    while count > 0:
        for iteration in range(count):
            i += dic[alg[value]][0]
            j += dic[alg[value]][1]
            end.append(snail[i][j])
        if value % 2: count -= 1
        value = (value+1) % 4
    return end


def smallest_possible_sum(seq: list) -> int:
    '''
    Find smallect possible sum of the input list
    Solution steps:
    [6, 9, 21] #-> x[2] = 21 - 9
    [6, 9, 12] #-> X[2] = 12 - 9
    [6, 9, 6] #-> X[2] = 9 - 6
    [6, 3, 6] #-> X[1] = 6 - 3
    [6, 3, 3] #-> X[2] = 6 - 3
    [3, 3, 3] #-> X[1] = 3 - 3 stop return sum([3, 3, 3])

    :param seq: input list
    :return: smallest possible sum
    '''
    def rec(seq):
        if len(seq) == 1: return sum(seq)
        l = len(seq)
        lst = []
        value = max(seq)
        if seq.count(seq[0]) == l: return seq[0]
        for num in range(l - 1):
            if seq[num] < seq[num + 1]:
                value = seq[num + 1] % seq[num]
                if value == 0: value = seq[num]
            elif seq[num] > seq[num + 1]:
                value = seq[num] % seq[num + 1]
                if value == 0: value = seq[num + 1]
            lst.append(value)
        return rec(lst)
    l = len(seq)
    if l <= 10:
        return rec(seq) * l
    else:
        return rec(seq[:20]) * l
