"""Source https://contest.yandex.ru/contest/8458/problems/C/"""


def duplicate_removal():
    file = open("input.txt", "r")
    array_len = int(file.readline().strip())
    previous = -1
    clean = []
    for i in range(array_len):
        item = int(file.readline().strip())
        if item != previous:
            clean.append(item)
        previous = item
    for i in clean:
        print(i)


if __name__ == "__main__":
    duplicate_removal()
