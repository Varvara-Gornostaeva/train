"""Source https://contest.yandex.ru/contest/8458/problems/C/"""

file = open("input.txt", "r")
len_mass = int(file.readline().strip())
previous = -1
clean = []
for i in range(len_mass):
    item = int(file.readline().strip())
    if item != previous:
        clean.append(item)
    previous = item
for i in clean:
    print(i)


# solution for context
import sys
len_mass = int(sys.stdin.readline().strip())
previous = -1
clean = []
for i in range(len_mass):
    item = sys.stdin.readline().strip()
    if item != previous:
        clean.append(item)
    previous = item

for i in clean:
    print(i)