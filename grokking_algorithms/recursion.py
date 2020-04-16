def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)


def sum_recursive(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_recursive(arr[1:])


def count_arr(arr):
    if len(arr) == 0:
        return 0
    return 1 + count_arr(arr[1:])


def max_arr(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_arr(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


def quick_sort_debug(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        sort_less = quick_sort(less)
        sort_greater = quick_sort(greater)
        result = sort_less + [pivot] + sort_greater
        return result


# O(n*log n) - wrong - O(n*n)m
def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# O(n)
if __name__ == "__main__":
    # countdown(5),
    # print(sum_recursive([4, 5, 6]))
    # print(count_arr([4, 5, 6, 8, 10, 1]))
    # print(max_arr([4, 1, 6]))
    print(quick_sort([10, 5, 2, 3]))
