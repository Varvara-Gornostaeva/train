""""Source https://contest.yandex.ru/contest/8458/problems/D/"""

import sys


def generate_bracket(suffix: str, op: int, cl: int, n: int):
    if op == n and cl == n:
        print(suffix)
        return
    if op < n:
        generate_bracket(suffix+"(", op+1, cl, n)
    if cl < op:
        generate_bracket(suffix+")", op, cl+1, n)


if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    generate_bracket("", 0, 0, n)

