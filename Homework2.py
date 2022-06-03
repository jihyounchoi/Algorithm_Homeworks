import random

# 문제1. 이분검색 재귀적 구현
'''
SortedList라는 클래스와, 전역 함수인 quick_sort, random_num_initializer, random_sorted_list_initializer을 구현하였고,
이를 통해 1000회의 테스트를 진행하였다.
test를 진행하는 함수인 recursion_time_tester는 SortedList class의 메소드로 구현되어 있다.
'''

class SortedList:

    # SortedList Class Member
    # sorted_list : list which is already sorted
    # recursion_count : count recursion time
    # length : length of self.sorted_list

    def __init__(self, sorted_list : list):
        self.sorted_list = sorted_list
        self.recursion_count : int = 0
        self.length = len(sorted_list)
    
    def recursion_counter(self): 
        # return self.recursion_count, and initialize it to zero.
        result = self.recursion_count
        self.recursion_count = 0 # initialize
        return result

    def binsearch(self, target : int) -> int:
        # binsearch contains recursive_binary_search, which searches target recursively

        def recursive_binary_search(left : int, right : int): # left, right : left and right boundary index each.

            self.recursion_count += 1 # proceed recursion count for each function call

            if left <= right:
                mid = (left + right) // 2

                if self.sorted_list[mid] < target:
                    return recursive_binary_search(mid + 1, right)
                elif self.sorted_list[mid] > target:
                    return recursive_binary_search(left, mid - 1)
                else:
                    return mid
            else:
                return -1

        # initial function call from leftend to rightend (end of the list)
        return recursive_binary_search(0, len(self.sorted_list) - 1) 


    def recursion_time_tester(self, to_repeat : int = 1000):
        # 멤버 함수인 binsearch와 recursion_counter를 이용하여, 1000회의 테스트를 진행한 후 결과를 나타내는 함수이다.
        # test comparison time, default repeat time -> 1000

        print(f'initialize test ... length of the list : {self.length}, repeat time : {to_repeat}')

        sum_of_each_recursion_count = 0 # count variable : added each recursion time

        for i in range(to_repeat):
            num_to_search = random_num_initializer(self.length) 
            # randomly create number to search between 1 to the length of the sorted_list

            self.binsearch(num_to_search)
            # call binsearch function

            sum_of_each_recursion_count += self.recursion_counter()

        print(f'... test successfully finished. average comparison time : {sum_of_each_recursion_count / to_repeat}\n')
        # print average comparison time by calculating "sum of each recursion time / repeat time(1000)"

def quick_sort(nums): # same as latest homework : quicksort

    if len(nums) <= 1:
        return nums

    center_elem = nums[len(nums) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []

    for num in nums:
        if num < center_elem:
            lesser_arr.append(num)
        elif num > center_elem:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr) # implement quicksort recursively


def random_num_initializer(range): # create single random integer between 1 ~ range
    result = random.randrange(1, range + 1)
    return result

def random_sorted_list_initializer(n): 
    # create sorted list by using random_num_initializer function
    # each number in sorted list is between 1 ~ n, and length of sorted list is also n

    result : list = []
    for i in range(n):
        each_num = random_num_initializer(n)
        result.append(each_num)

    result = quick_sort(result) # sorting process
    return result # return sorted list

list_128 = SortedList(random_sorted_list_initializer(128))
list_256 = SortedList(random_sorted_list_initializer(256))
list_512 = SortedList(random_sorted_list_initializer(512))
print(list_128.recursion_time_tester())
print(list_256.recursion_time_tester())
print(list_512.recursion_time_tester())

''' 예상 출력
initialize test ... length of the list : 128, repeat time : 1000
... test successfully finished. average comparison time : 6.588


initialize test ... length of the list : 256, repeat time : 1000
... test successfully finished. average comparison time : 7.46


initialize test ... length of the list : 512, repeat time : 1000
... test successfully finished. average comparison time : 8.45

이분검색 알고리즘의 최악의 경우, 분석 횟수는 lg(n)+1이 된다. 이는 list의 크기가 128인 경우 8, 256인 경우 9, 512인 경우 10에 해당하는데,
test에서는 매번 랜덤한 list와 랜덤한 target을 생성하므로 최악의 경우보다는 약간 적은 비교횟수로 탐색이 진행됨을 알 수 있다.
(평균적으로 1.5회 가량 차이가 존재함)
'''

# 문제 2

# declare memory_usage variable which contains current memory usage
global memory_usage
memory_usage = 0 # initialized by zero

# 강의자료의 keytype U -> left_list, keytype V -> right_list, keytype S -> merged_list로 변수명을 바꾸었습니다
# int h, m에 대해서는 len() 함수를 이용하여 따로 parameter를 받지 않았습니다

def merge(left_list, right_list, merged_list): # 두 list의 원소를 비내림차순으로 새로운 list에 할당하는 함
    index_left, index_right, index_merged = 0, 0, 0
    
    while index_left < len(left_list) and index_right < len(right_list):
        # 두 list의 index가 list 길이를 초과하지 않는 경우.
        
        if left_list[index_left] < right_list[index_right]:
            merged_list[index_merged] = left_list[index_left]
            index_left += 1
            index_merged += 1
        else:
            merged_list[index_merged] = right_list[index_right]
            index_right += 1
            index_merged += 1
    
    if index_left >= len(left_list): # left_list의 원소가 모두 merged_list로 이동한 경우
        while index_right != len(right_list): # right_list의 원소를 모두 merged_list로 이동
            merged_list[index_merged] = right_list[index_right]
            index_right += 1
            index_merged += 1
    else: # 위의 if절과 반대의 경우 -> 반대로 시행
        while index_left != len(left_list):
            merged_list[index_merged] = left_list[index_left]
            index_left += 1
            index_merged += 1 

def mergesort(input_list):
    
    if len(input_list) > 1:   
        center_index = len(input_list) // 2 # center index of input_list
        left_list = input_list[:center_index] # left half of the list
        right_list = input_list[center_index:] # right half of the list

        # 나뉘어진 2개의 리스트 (left, right_list)의 크기만큼을 전역변수 memory_usage에 추가함.
        # 이 값은 재귀호출이 끝난 후 다시 minus 될 예정.
        # 이를 통해 program 실행 중의 메모리 사용량을 볼 수 있다.
        global memory_usage
        memory_usage += len(left_list)
        memory_usage += len(right_list)
        print(f'memory usage now : {memory_usage}')

        mergesort(left_list)
        mergesort(right_list) # call mergesort recursively
        
        merge(left_list, right_list, input_list)

    
    memory_usage -= len(input_list)

    return

numbers = [8, 3, 15, 2, 9, 1, 5, 7, 4, 16, 10, 11, 12, 13, 6, 14] # test input
mergesort(numbers) # call mergesort

# sorting이 완료된 numbers 출력 전에 각 호출마다의 메모리 사용량 정보가 출력될 예정
print(f'sorted numbers : {numbers}')

''' 예상 출력
memory usage now : 16
memory usage now : 24
memory usage now : 28
memory usage now : 30 # 최대 메모리 사용량 : 30
memory usage now : 28
memory usage now : 24
memory usage now : 26
memory usage now : 24
memory usage now : 16
memory usage now : 20
memory usage now : 22
memory usage now : 20
memory usage now : 16
memory usage now : 18
memory usage now : 16
sorted numbers : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

따라서 이 예시에서 추가적인 저장공간의 크기는 8*2 + 4*2 + 2*2 + 1*2 = 30이 됨을 알 수 있다.
'''


















