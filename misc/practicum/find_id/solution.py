

def find_id_slow():
    file = open("input.txt", "r")
    n = int(file.readline().strip())
    arr = list(map(int, file.readline().split()))
    for i in range(1, n+1):
        # VERY SLOW
        if i not in arr:
            print(i, end=' ')


if __name__ == "__main__":
    find_id_slow()