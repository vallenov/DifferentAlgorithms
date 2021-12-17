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
