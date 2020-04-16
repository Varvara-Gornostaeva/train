

def find_id_slow():
    file = open("input.txt", "r")
    n = int(file.readline().strip())
    arr = list(map(int, file.readline().split()))
    for i in range(1, n+1):
        # VERY SLOW
        if i not in arr:
            print(i, end=' ')


# O(2*n)
def find_id():
    file = open("input.txt", "r")
    n = int(file.readline().strip())
    arr_full = [0]*(n+1)
    arr = list(map(int, file.readline().split()))
    for i in arr:
        arr_full[i] += 1
    del arr
    for i in range(1, n+1):
        if not arr_full[i]:
            print(i, end=' ')


if __name__ == "__main__":
    find_id()
