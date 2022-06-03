import random
import time
import copy

def insertion_sort(list_input):
    for end in range(1, len(list_input)):
        for i in range(end, 0, -1):
            if list_input[i - 1] > list_input[i]:
                list_input[i - 1], list_input[i] = list_input[i], list_input[i - 1] # swap value

def quick_sort(list_input):
    if len(list_input) <= 1:
        return list_input

    center_elem = list_input[len(list_input) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []

    for num in list_input:
        if num < center_elem:
            lesser_arr.append(num)
        elif num > center_elem:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr) # implement quicksort recursively

def random_list_initializer(list_length):
    result : list = []
    for i in range(list_length):
        each_num = random.randrange(1, 1001)
        result.append(each_num)
    return result

def sorting_timer(list_size):

    print(f'n = {list_size}')

    list_insertionsort : list = random_list_initializer(list_size)
    list_quicksort = copy.deepcopy(list_insertionsort) # deepcopy list

    start = time.time()
    insertion_sort(list_insertionsort)
    end = time.time()

    interval_insertionsort : int = end - start

    start = time.time()
    quick_sort(list_quicksort)
    end = time.time()

    interval_quicksort : int = end - start

    print(f'insertionsort : {interval_insertionsort}, quicksort : {interval_quicksort}\n')

sorting_timer(5000)
sorting_timer(10000)
