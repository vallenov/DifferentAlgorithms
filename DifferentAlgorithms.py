from typing import List
import re


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
    :params n: n factorial number
    :return: count the number of zeros
    """
    return sum([n // (5 ** i) for i in range(1, 15)])


def generate_hashtag(s: str) -> str or None:
    """
    Turn string to hashtag
    How are you? -> #HowAreYou?
    :param s: input string
    :return: hashtag or None if string is empty or length >= 140
    """
    if s == '' or len(s) > 139:
        return None
    return '#' + ''.join(list(s.strip().title().replace(" ", "")))


def peak_height(m: List[str]) -> int:
    """
    Get peak height
    ['^^^^^^       ',
     ' ^^^^^^^^    ',
     '  ^^^^^^^    ',
     '  ^^^^^      ',
     '  ^^^^^^^^^^^',
     '  ^^^^^^     ',
     '  ^^^^       ']

     =====>

     ['111111     ',
      '12222111   ',
      '1233211    ',
      '12321      ',
      '12332111111',
      '122211     ',
      '1111       ']

      == 3

    :param m: scheme of mountain
    :return: peak height
    """
    def check(mat):
        for i in range(len(mat)):
            if "^" in ''.join(mat[i]):
                return False
        return True

    def size_up(matrix):
        nmatrix = list()
        nmatrix.append("0" * (len(matrix[0]) + 2))
        for i in range(len(matrix)):
            nmatrix.append("0" + matrix[i] + "0")
        nmatrix.append("0" * (len(matrix[0]) + 2))
        return nmatrix
    if m == [] or check(m) is True:
        return 0
    m = [re.sub(" ", "0", m[i]) for i in range(len(m))]
    m = size_up(m)
    m = [list(i) for i in m]
    cnt = 0
    ex = False
    while ex is not True:
        for i in range(1, len(m) - 1):
            for j in range(1, len(m[0]) - 1):
                if (m[i][j] == "^") and (
                        str(cnt) in ''.join(m[i - 1][j]) + ''.join(m[i][j - 1:j + 2]) + ''.join(m[i + 1][j])):
                    m[i][j] = str(cnt + 1)
        if check(m):
            ex = True
        cnt += 1
    return cnt


def increment_string(string: str) -> str:
    """
    Increment string
    string -> string1
    string0 -> string1
    string9 -> string10
    string0000 -> string0001
    :param string: input string
    :return: incremented string
    """
    try:
        num = int(''.join(re.findall(r'\d*$', string)))
    except ValueError:
        return string + "1"
    else:
        length = len(''.join(re.findall(r'\d*$', string)))
    return string[:string.rfind(''.join(re.findall(r'\d*$', string)))] + str(int(num + 1)).rjust(length, "0")


def make_readable(seconds: int) -> str:
    """
    Translate int to str like hh:mm:ss
    2345 sec => 00:39:05
    :param seconds: sec
    :return: hh:mm:ss
    """
    tm = [seconds // 3600, (seconds - ((seconds // 3600) * 3600)) // 60, seconds % 60]
    ntm = []
    for i in range(len(tm)):
        if tm[i] < 10:
            ntm.append("0" + str(tm[i]))
            continue
        ntm.append(str(tm[i]))
    return "{}".format(':'.join(ntm))


class PaginationHelper:
    """
    The constructor takes in an array of items and a integer indicating
    how many items fit within a single page
    """
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        """
        Returns the number of items within the entire collection
        """
        return len(self.collection)

    def page_count(self):
        """
        Returns the number of pages
        :param:
        :return:
        """
        return (len(self.collection) // self.items_per_page) + 1

    def page_item_count(self, page_index):
        """
        Returns the number of items on the current page. page_index is zero based
        his method should return -1 for page_index values that are out of range
        :param page_index: index of page
        :return: count of items on the page
        """
        if page_index < self.page_count() - 1:
            return self.items_per_page
        elif page_index > self.page_count() - 1:
            return -1
        else:
            return len(self.collection) % self.items_per_page

    def page_index(self, item_index):
        """
        Determines what page an item is on. Zero based indexes.
        his method should return -1 for item_index values that are out of range
        :param item_index: item index
        :return: number of page
        """
        if item_index >= len(self.collection):
            return -1
        elif item_index < 0:
            return -1
        else:
            return item_index // self.items_per_page


def find_even_index(arr):
    """
    Find an index N where the sum of the integers to the left of N is equal to the sum of the integers to the
    right of N.
    If not exist, return -1
    :param arr: input list
    :return: index
    """
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            return i
    return -1


def dig_pow(n: int, p: int) -> int:
    """
    Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
    Fnd a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p
    is equal to k * n
    (89, 1) should return 1 since 8¹ + 9² = 89 = 89 * 1
    (92, 1) should return -1 since there is no k such as 9¹ + 2² equals 92 * k
    (695, 2) should return 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2
    (46288, 3) should return 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
    :param n: input number
    :param p: pow start
    :return: integer
    """
    lst = list(str(n))
    lst = [int(j) for j in lst]
    for i in range(len(lst)):
        lst[i] **= p
        p += 1
    summ = sum(lst)
    dub = n
    if n > summ:
        return -1
    else:
        count = 1
        while 1:
            if dub > summ:
                return -1
            elif dub == summ:
                return count
            count += 1
            dub = n * count


def queue_time(c: list, n: int) -> int:
    """
    Calculate the total time required for all the customers to check out
    [3,4,10,2,5,6,9,1,1,4,5], 3
    3, 2, 6, 5   => 16
    4, 5, 9      => 18 (!)
    10, 1, 1, 4  => 16
    :param c: list of customers
    :param n: count of queues
    :return: total time
    """
    count = 0
    if len(c) < 1:
        return 0
    if n >= len(c):
        return max(c)
    while sum(c[:n]) > 0:
        for i in range(n):
            if c[i] <= 0:
                continue
            c[i] -= 1
            if (c[i] == 0) and (len(c) > n):
                c[i] = c.pop(n)
        count += 1
    return count


def tribonacci(signature, n):
    """
    Like fibonacci, but the next number based on the 3 numbers to the left
    [1,2,3], 10 => [1, 2, 3, 6, 11, 20, 37, 68, 125, 230]
    :params signature: start numbers
    :params n: count of iterations
    :return: list of tribonacci numbers
    """
    if n == 0:
        return []
    elif n == 1:
        return [1]
    if len(signature) >= n:
        return signature
    else:
        signature.append(sum(signature[-3:]))
        return tribonacci(signature, n)


def valid_parentheses(string):
    """
    Check parentheses
    example: '(())' -> True, '' -> False
    :param string: like '(())' or '))(()'
    :return: boolean
    """
    lst = list(string)
    count = 0
    for i in range(len(lst)):
        if lst[i] == "(":
            count += 1
        if lst[i] == ")":
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False


def row_sum_odd_numbers(n):
    """
    Find summ of:
                 1
              3     5
           7     9    11
       13    15    17    19
    21    23    25    27    29

    1 -->  1
    2 --> 3 + 5 = 8
    :param n: count of rows
    :return: sum of nth row
    """
    buf = 1
    up = 2
    if n == 1:
        return 1
    for i in range(n-1):
        buf += up
        up = up + 2
    count = buf
    for j in range(n-1):
        buf += 2
        count += buf
    return count


def twosum(nums: List[int], target: int) -> List[int] or None:
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target
    :param nums: input list
    :param target: upper bound
    :return: [the numbers] which sum == target
    """
    for j in range(len(nums)):
        for k in range(len(nums)):
            if j == k:
                continue
            if nums[j] + nums[k] == target:
                return [j, k]
    return None


class ListNode:
    """
    Like a list node
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addtwonumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    ListNode's sum

    ListNode1 = 2 -> 4 -> 3
    ListNode1 = 5 -> 6 -> 4
    Result = 7 -> 0 -> 8
    fin = addtwonumbers(l1, l2)

    :param l1: first ListNode
    :param l2: second ListNode
    :return: ListNode
    """
    dec = 0
    finlist = ListNode()
    l1over = 0
    l2over = 0
    head = finlist

    while True:
        if not l1:
            l1over = 1
            l1buf = 0
        else:
            l1buf = l1.val
        if not l2:
            l2over = 1
            l2buf = 0
        else:
            l2buf = l2.val
        if l1over and l2over:
            break
        if l1buf + l2buf + dec > 9:
            finlist.next = ListNode((l1buf + l2buf + dec) % 10)
            dec = 1
        else:
            finlist.next = ListNode(l1buf + l2buf + dec)
            dec = 0
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        finlist = finlist.next
    if dec:
        finlist.next = ListNode(dec)
    finlist = head
    return finlist.next


def create_listnode(lst: list) -> ListNode:
    """
    Convern regular list to custom list

    l = create_listnode([2,4,3])

    while l:
        print(l.val)
        l = l.next

    :param lst: input list
    :return: ListNode
    """
    head = None
    ln = None
    for val in lst:
        if head is None:
            ln = ListNode(val)
            head = ln
        else:
            ln.next = ListNode(val)
            ln = ln.next
    return head


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Get the median of the two sorted lists
    :param nums1: first sorted list
    :param nums2: second sorted list
    :return: the median
    """
    lst = []
    lst.extend(nums1)
    lst.extend(nums2)
    lst.sort()
    if len(lst) % 2 != 0:
        return float(lst[int((len(lst) - 1) / 2)])
    else:
        return float(lst[int(len(lst) / 2) - 1] + lst[int(len(lst) / 2)]) / 2


def is_palindrome(x: int) -> bool:
    """
    Check if a string is a palindrome
    :param x: input string
    :return: True or False
    """
    return True if str(x) == str(x)[::-1] else False


def longest_common_prefix(strs: List[str]) -> str:
    """
    Find the longest common prefix string amongst an array of strings
    strs = ["strong","storm","steal"] -> "st"
    :param strs: input array of strings
    :return: longest common prefix
    """
    pref = ''
    count = 0
    minlenght = len(min(strs))
    if minlenght == 0:
        return ''
    if len(strs) == 1:
        return strs[0]
    for i in range(len(strs[0])):
        buf = str(strs[0][count])
        for j in range(len(strs)):
            if strs[j] == '':
                return ''
            if str(strs[j][count]) != buf:
                return pref
        pref += buf
        count += 1
        if count == minlenght:
            return pref


def valid_all_parentheses(s: str) -> bool:
    """
    Check parentheses
    example: '(){}' -> True, '[[)' -> False
    :param s: input string
    :return: boolean
    """
    dics = {'[': ']', '(': ')', '{': '}', ']': '[', ')': '(', '}': '{'}
    dicin = ['[', '(', '{']
    lst = []
    for i in s:
        if i in dicin:
            lst.append(i)
        else:
            if not len(lst):
                return False
            if dics[lst[len(lst) - 1]] != i:
                return False
            else:
                lst.pop()
    return False if len(lst) else True


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merge two ListNode objects
    For test you may use create_listnode()

    l1 = create_listnode([2,4,3])
    l2 = create_listnode([1,5,6])
    =
    ListNode(1 -> 2 -> 4 -> 3 -> 5 -> 6)

    :param l1: first object
    :param l2: second object
    :return: merged ListNode object
    """
    fin = None
    head = None
    while l1 or l2:
        if l1 and l2:
            min_num = l1.val if l1.val < l2.val else l2.val
            max_num = l1.val if l1.val > l2.val else l2.val
            if not head:
                fin = ListNode(min_num)
                head = fin
            else:
                fin.next = ListNode(min_num)
                fin = fin.next
            if l1.next and l1.next.val < max_num:
                l1 = l1.next
                continue
            if l2.next and l2.next.val < max_num:
                l2 = l2.next
                continue

            fin.next = ListNode(max_num)
            fin = fin.next

            l1 = l1.next
            l2 = l2.next
            continue
        if not l1:
            while l2:
                if not head:
                    fin = ListNode(l2.val)
                    head = fin
                else:
                    fin.next = ListNode(l2.val)
                    fin = fin.next
                l2 = l2.next
        if not l2:
            while l1:
                if not head:
                    fin = ListNode(l1.val)
                    head = fin
                else:
                    fin.next = ListNode(l1.val)
                    fin = fin.next
                l1 = l1.next
    fin = head
    return fin


def remove_duplicates(nums: List[int]) -> int:
    """
    Return len of unique elements
    Use the same var "nums"
    :param nums: input sorted list
    :return: len
    """
    lst = []
    count = 0
    for i in nums:
        if i not in lst:
            lst.append(i)
            nums.insert(count, i)
            count += 1
    return len(lst)


def remove_element(nums: List[int], val: int) -> int:
    """
    Remove all numbers == val and return len of edited list
    Use the same var "nums"
    :param nums: input list
    :param val: deleted value
    :return: len
    """
    i = 0
    if not nums:
        return 0
    while i != len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    return len(nums)

