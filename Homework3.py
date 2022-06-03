import random


# Question 1

# 비교횟수를 카운트하기 위한 global 변수 선언
global compare_times
compare_times = 0

# global 변수인 compare_times 변수를 리턴한 후, 해당 변수를 초기화한다.
def compare_info(): 

    global compare_times

    result = compare_times
    compare_times = 0

    return result


def quicksort(S : list, low : int, high : int):

    if high > low:
        pivot = partition(S, low, high) # pivot = pivot index
        quicksort(S, low, pivot - 1)
        quicksort(S, pivot + 1, high)

    return S


def partition(S : list, low : int, high : int):
    
    piv_item = S[low]
    j = low

    for i in range(low + 1, high + 1): # low + 1 ~ high

        # 아래 if 절의 결과와 관련없이 compare_times 변수는 1 더해지므로 if 절 바로 전에 해당 코드가 위치한다.
        global compare_times
        compare_times += 1
        
        if S[i] < piv_item: # pivot의 item보다 작은 item을 발견하면,

            j += 1 # j를 한 칸 전진시킨 후

            # i와 j의 원소를 교환
            S[i], S[j] = S[j], S[i]

    pivot = j # pivot index의 위치를 (대소상의) 중앙으로 옮김

    # exchange S[low] and S[pivot]
    S[low], S[pivot] = S[pivot], S[low]

    return pivot

# 각 원소가 1 ~ size 사이의 값을 가지는,
# 동시에 하나의 data는 size 만큼의 원소를 가지는,
# 이러한 조건을 만족시키는 data list가 100개 모인 "dataset" 을 생성한다.
# dataset : list[list], length(dataset) = 100
def create_dataset(size):
    datasets : list = []

    for i in range(100):

        data = []

        for j in range(size):
            num = random.randrange(size + 1)
            data.append(num)

        datasets.append(data)

    return datasets

# Main Function

sizes : list = [100, 200, 300, 400] # size : 100, 200, 300, 400
result : list = [0, 0, 0, 0] # 각 사이즈별 평균 비교횟수를 저장할 result list

for (i, size) in enumerate(sizes): # 0, 100 / 1, 200 / 2, 300 / 3, 400

    total_compare_time = 0

    datasets = create_dataset(size) # datasets : list[list] 생성

    for data in datasets:
        quicksort(data, 0, len(data) - 1) # 각 data list에 대해 quicksort 수행

        c_time = compare_info() # compare time 정보 불러옴 (compare_info 함수를 호출하였으므로 compare_times 전역변수는 초기화)

        total_compare_time += c_time

    avg_compare_time = total_compare_time / 100 # 전체 비교 횟수 / 데이터의 갯수

    result[i] = avg_compare_time # result list에 결과값을 추가함

print(f'왼쪽부터 차례로 n = 100, 200, 300, 400입니다\n : {result}')

'''
왼쪽부터 차례로 n = 100, 200, 300, 400입니다
 : [649.11, 1594.84, 2577.86, 3646.85]
'''
# Question 1 end.


# Question 2

def prod(left : int, right : int): # 3 * 4 -> left : 3, right : 4

    max_digit = max(len(str(left)), len(str(right))) # left, right중 긴 숫자의 길이(자릿수)를 max_digit에 할당함

    if left == 0 or right == 0: # 두 숫자중에 하나라도 0이면 0
        return 0
    elif max_digit <= 2: # 최대 자릿수가 2자리 이하면 recursion 종료. 그냥 곱하여 리턴
        return left * right
    else:
        m = max_digit // 2 # 2로 나눈 몫. ex) 7 // 2 = 3.

        # 각각 left/right_quotient(몫), left/right_remainder(나머지)
        l_quot = left // pow(10, m) 
        l_rem  = left % pow(10, m)
        r_quot = right // pow(10, m) 
        r_rem  = right % pow(10, m)

        # prod 함수를 4번 재귀호출.
        return prod(l_quot, r_quot) * pow(10, 2*m)         + (prod(l_quot, r_rem) + prod(l_rem, r_quot)) * pow(10, m)         + prod(l_rem, r_rem)


# 작성한 코드가 잘 동작하는지 확인하는 샘플코드입니다.
# 10만 ~ 100만 사이의 숫자 두 개를 랜덤생성하여 곱한 결과를 함수를 통해 곱한 결과와 비교합니다.

a = random.randrange(100000,1000000)
b = random.randrange(100000,1000000)

answer = a * b
your_answer = prod(a, b)

print(f'Answer : {answer} / Your Answer : {your_answer}')

if answer == your_answer:
    print(' ----- function works well :) -----')
else:
    print(' ----- try to fig some bugs :( -----')

'''
예상 출력

Answer : 489883089150 / Your Answer : 489883089150
 ----- function works well :) -----

'''

