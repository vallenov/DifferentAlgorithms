def hamming(n):
    '''
    Calculate the Hamming numbers
    :params:

    :return: nth Hamming number

    :example: print(hamming(5000))
    '''
    a2 = 1
    a3 = 1
    a5 = 1
    mas = []
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