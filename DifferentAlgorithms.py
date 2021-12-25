from typing import List


def hamming(n: int) -> int:
    """
    Calculate the Hamming numbers
    :param n: Hamming number required
    :return: nth Hamming number
    :example: print(hamming(5000))
    """
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


def decompose(n: int) -> int or None:
    """
    Decompose input number (if n=11, output: [1, 2, 4, 10], explain: 1**2 + 2**2 + 4**2 + 10**2 == 11**2)
    :param n: Input number to decompose
    :return: Result of decompose
    """
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
    def to_roman(number: int) -> str:
        """
        Str roman to int
        :param number: int like 1616
        :return: roman like 'MDCXVI'
        :example: print(RomanNumerals.from_roman(1616))
        """
        di = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
        string = list(str(number))
        lst = []
        roman = ''
        lst.append(int(string[len(string) - 1]))
        string = string[::-1]
        for dec in range(1, 4):
            if len(string) <= 1:
                break
            if string[dec]:
                lst.append(int(string[dec]) * (10 ** dec))
        lst = lst[::-1]
        sortkeys = sorted(di.keys())[::-1]
        for element in lst:
            for sort in sortkeys:
                while element:
                    value = element - sort
                    if value >= 0:
                        roman += di[sort]
                        element -= sort
                        continue
                    else:
                        value = abs(value)
                        if di.get(value):
                            roman += di[value]
                            roman += di[sort]
                            element -= sort - value
                        elif di.get(value * 2):
                            roman += di[value] * 2
                            roman += di[sort]
                            element -= sort - value * 2
                        else:
                            break
        return roman

    @staticmethod
    def from_roman(roman: str) -> int:
        """
        Str roman to int
        :param roman: string like 'MDCXVI'
        :return: number int 1616
        :example: print(RomanNumerals.from_roman('MDCXVI'))
        """
        di = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        number = 0
        prev = 0
        for i in range(len(roman) - 1, -1, -1):
            if prev <= di[roman[i]]:
                number += di[roman[i]]
                prev = di[roman[i]]
            else:
                number -= di[roman[i]]
        return number


def resnail(snail: List[List]) -> List[int]:
    """
    Convert array from [[ 1,  2,  3, 4],
                                    [12, 13, 14, 5],
                                    [11, 16, 15, 6],
                                    [10,  9,  8, 7]]
    to [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    :param snail: array NxN [[], [], []]
    :return: array []
    """
    count = len(snail[0])-1
    i = 0
    j = count
    end = snail[0]
    value = 0
    alg = ['d', 'l', 'u', 'r']
    dic = {'d': (1, 0), 'l': (0, -1), 'u': (-1, 0), 'r': (0, 1)}
    while count > 0:
        for iteration in range(count):
            i += dic[alg[value]][0]
            j += dic[alg[value]][1]
            end.append(snail[i][j])
        if value % 2:
            count -= 1
        value = (value+1) % 4
    return end

def smallest_possible_sum(s: List[int]) -> int:
    """
    Find smallect possible sum of the input list
    Solution steps:
    [6, 9, 21] #-> x[2] = 21 - 9
    [6, 9, 12] #-> X[2] = 12 - 9
    [6, 9, 6] #-> X[2] = 9 - 6
    [6, 3, 6] #-> X[1] = 6 - 3
    [6, 3, 3] #-> X[2] = 6 - 3
    [3, 3, 3] #-> X[1] = 3 - 3 stop return sum([3, 3, 3])

    :param s: input list
    :return: smallest possible sum
    """
    def rec(seq: List[int]) -> int:
        if len(seq) == 1:
            return sum(seq)
        lenn = len(seq)
        lst = []
        value = max(seq)
        if seq.count(seq[0]) == lenn:
            return seq[0]
        for num in range(lenn - 1):
            if seq[num] < seq[num + 1]:
                value = seq[num + 1] % seq[num]
                if value == 0:
                    value = seq[num]
            elif seq[num] > seq[num + 1]:
                value = seq[num] % seq[num + 1]
                if value == 0:
                    value = seq[num + 1]
            lst.append(value)
        return rec(lst)
    length = len(s)
    if length <= 10:
        return rec(s) * length
    else:
        return rec(s[:20]) * length


def dirredir(arr: List[str]) -> List[str]:
    """
    Direction redirection (removes unnecessary steps)
    :param arr: list of direction
    :return: final path
    :example: ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"] returns ['WEST']
    """
    i = 0
    while i < len(arr) - 1:
        if arr[i] != arr[i + 1] and len(arr[i]) == len(arr[i + 1]):
            arr = arr[:i] + arr[i + 2:]
            i = 0
            continue
        i += 1
    return arr


def is_interesting(num: int, ap: List[int]) -> int:
    """
    Сheck numerical for interestingness
    If num is palindrome (345543, 676)
    or incrementing (45678, 123)
    or decrementing (87654)
    or  followed by all zeros (1000, 400000)
    return 2 (Yes)
    :param num: current number
    :param ap: list of needed numbers
    :return: 0 or 1 or 2 (No, Almost, Yes)
    """
    def is_pol(n: int) -> bool:
        if n < 100:
            return False
        n = str(n)
        start = n[:int((len(n) / 2))]
        if len(n) % 2 == 0:
            finish = n[int(len(n) / 2):]
        else:
            finish = n[int((len(n) / 2) + 1):]
        if start == finish[::-1]:
            return True
        else:
            return False

    def is_incdec(n: int) -> bool:
        if n < 110:
            return False
        n = str(n)
        if n[0] == "0":
            return False
        if n[0] > n[1]:
            n = n[::-1]
        for i in range(len(n) - 1):
            if (int(n[i]) + 1) % 10 == int(n[i + 1]):
                continue
            else:
                return False
        return True

    def is_straight(n: int) -> bool:
        if n < 100:
            return False
        n = str(n)
        if n[0] != "0" and n.count("0") == len(n) - 1:
            return True
        else:
            return False

    if num in ap:
        return 2
    if is_pol(num) or is_straight(num) or is_incdec(num):
        return 2
    if num + 1 in ap or num + 2 in ap:
        return 1
    if is_pol(num + 1) \
            or is_pol(num + 2) \
            or is_straight(num + 1) \
            or is_straight(num + 2) \
            or is_incdec(num + 1) \
            or is_incdec(num + 2):
        return 1
    return 0


def josephus(items: List[int], k: int) -> List[int]:
    """
    Sort input list. Get every k item
    items = [1, 2, 3, 4, 5], k = 3
    [1, 2, 4, 5] -> [2, 4, 5] -> [2, 4] -> [4]
    result = [3, 1, 5, 2, 4]
    :param items: input list
    :param k: sort steps
    :return: sorted list
    """
    if k == 1:
        return items
    i = 0
    cnt = 1
    path = []
    while items is []:
        if i >= len(items):
            i = 0
        if cnt == k:
            print(items)
            if i >= len(items)-1:
                path.append(items.pop(i))
                i = 0
            else:
                path.append(items.pop(i))
            cnt = 1
        cnt += 1
        i += 1
    return path


def pick_peaks(arr: List[int]) -> dict:
    """
    Find list peaks
    [1,2,3,1,2,2,5,2] -> {'pos': [2, 6], 'peaks': [3, 5]}
    :param arr: input list
    :return: dict like {'pos': [], 'peaks': []}
    """
    result = {"pos": [], "peaks": []}
    up = False
    cur = 0
    for elem in range(len(arr)-1):
        if arr[elem] < arr[elem+1]:
            up = True
            cur = elem
        elif arr[elem] > arr[elem+1]:
            if up is True:
                result["pos"].append(cur+1)
                result["peaks"].append(arr[cur+1])
            up = False
    return result


def tic_tac_toe_check(board: List[list]) -> int:
    """
    Tic-Tac-Toe checker (3x3)
    :param board: the current state of the board
    [[0, 1, 2],
     [0, 1, 2],
     [1, 0, 2]]
    :return: -1: the game is not over
              0: game over. result is draw
              1: game over. 1 player win
              2: game over. 2 player win
    """
    def check_win(field, player):
        if ''.join([str(field[0][0]), str(field[1][1]), str(field[2][2])]).count(str(player)) == 3:
            return 1
        if ''.join([str(field[0][2]), str(field[1][1]), str(field[2][0])]).count(str(player)) == 3:
            return 1
        for row in range(len(field)):
            if str(field[row]).count(str(player)) == 3:
                return 1
        for col in range(len(field)):
            if str([field[i][col] for i in range(len(field))]).count(str(player)) == 3:
                return 1
        return 0
    if check_win(board, 1):
        return 1
    elif check_win(board, 2):
        return 2
    elif "0" not in ''.join([str(i) for i in board]):
        return 0
    else:
        return -1


def count_zeros(n):
    """
    Count the number of zeros in the end of factorial "n"
    zeros(100) == 24
    :params n: т factorial number
    :return: count the number of zeros
    """
    return sum([n // (5 ** i) for i in range(1,15)])

