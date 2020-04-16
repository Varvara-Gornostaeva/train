
def find_smallest(arr: list) -> int:
    """For searching smallest item of massive"""
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# O(n*n)
def select_sort(arr: list):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == "__main__":
    print(select_sort([5, 3, 6, 2, 11]))
