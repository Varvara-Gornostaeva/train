"""Source https://contest.yandex.ru/contest/8458/problems/F/"""


def merge_sorted_list_simple(file):
    k = int(file.readline().strip())
    l_union = []
    for i in range(k):
        ll = list(map(int, file.readline().split()))
        l_union = l_union + ll[1:]
        del ll
    l_union.sort()
    for item in l_union:
        print(item, end=' ')


def merge_sorted_list(file):
    k = int(file.readline().strip())
    l_union = [0]*101

    for i in range(k):
        ll = list(map(int, file.readline().split()))
        for item in ll[1:]:
            l_union[item] += 1
        del ll

    for i in range(101):
        if l_union[i]:
            print(' '.join([str(i)] * l_union[i]), end=' ')


def merge_sorted_list_universal(file):
    k = int(file.readline().strip())
    l_union = []*k

    for i in range(k):
        ll = list(map(int, file.readline().split()))
        l_union = [0] * len(ll)
        for item in ll[1:]:
            l_union[item] += 1
        del ll

    for i in range(101):
        if l_union[i]:
            print(' '.join([str(i)] * l_union[i]), end=' ')


if __name__ == "__main__":
    file = open("input.txt", "r")
    merge_sorted_list(file)