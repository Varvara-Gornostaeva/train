"""https://contest.yandex.ru/contest/8458/problems/E/"""
from collections import Counter, defaultdict


def is_anagram_counter(a, b):
    if len(a) != len(b):
        print(0)
        return
    ca = Counter(a)
    cb = Counter(b)
    diff = ca-cb
    print(1 if len(diff) == 0 else 0)

def is_anagram_counter_custom(a, b):
    if len(a) != len(b):
        print(0)
        return
    ca = dictFromStrings(a)
    cb = dictFromStrings(b)
    diff = ca.items() - cb.items()
    print(1 if len(diff) == 0 else 0)


def dictFromStrings(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return d


def is_anagram_while(first, second):
    l1, l2 = list(first), list(second)
    while l1:
        li = l1.pop()
        if li in l2:
            l2.remove(li)
        else:
            print(0)
            return
    print(1 if not l2 else 0)


if __name__ == "__main__":
    file = open("input.txt", "r")
    first = str(file.readline().strip())
    second = str(file.readline().strip())
    is_anagram_counter_custom(first, second)
    is_anagram_counter(first, second)
    is_anagram_while(first, second)

