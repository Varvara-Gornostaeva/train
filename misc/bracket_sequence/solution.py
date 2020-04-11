""""Source https://contest.yandex.ru/contest/8458/problems/D/"""

import sys
#
# iteration one
# def generate_bracket(st: str, open: int, close: int, n: int):
#     if len(st) == 2*n:
#         if open == close:
#             print(st)
#         return
#     generate_bracket(st+"(", open+1, close, n)
#     if close < open:
#         generate_bracket(st+")", open, close+1, n)


def generate_bracket(st: str, open: int, close: int, n: int):
    if open == n and close == n:
        print(st)
        return
    if open < n:
        generate_bracket(st+"(", open+1, close, n)
    if close < open:
        generate_bracket(st+")", open, close+1, n)


n = int(sys.stdin.readline().strip())
generate_bracket("", 0, 0, n)
