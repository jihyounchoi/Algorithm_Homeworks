print('Question 1')
# Question 1

inf = 1000

w = [[0, 15, 4, 11, 5], [inf, 0, inf, 1, inf], [inf, 4, 0, 2, inf], [inf, inf, inf, 0, inf], [inf, 3, inf, 1, 0]]

n = 5

f = set()
touch  = n * [0]
length = n * [0]
save_length = n * [0]
NoC = 0


for i in range(1, n): # v1과 v1과의 거리 정보는 저장할 필요 없으므로, 1부터 시작한다
    length[i] = w[0][i]
    touch[i] = 0

for _ in range(n-1):

    min = inf
    
    for i in range(1, n):
        if 0 <= length[i] and length[i] < min:
            min = length[i]
            vnear = i # vnear : 현재 탐색하지 않은 노드 중 가장 가까운 노드

    e = (touch[vnear], vnear)
    print(e[0], e[1])
    f.add(e)

    for i in range(1, n):
        if length[vnear] + w[vnear][i] < length[i]:
            length[i] = length[vnear] + w[vnear][i]
            touch[i] = vnear
    
    save_length[vnear] = length[vnear]
    length[vnear] = -1

# NoC 계산
# 전체 아크의 개수에서 v1과 연결된 아크의 개수를 빼는 방식으로 구현

# 전체 아크의 개수
for row in w:
    for elem in row:
        if elem != inf and elem != 0:
            NoC += 1

# - v1과 연결된 아크
for elem in w[0]:
    if elem != inf and elem != 0:
        NoC -= 1


# Vertex 출력은 0 ~ 4번으로 설정했습니다
print(f'f set : {f}')
print(f'save_length list : {save_length}')
print(f'NoC : {NoC}')

######################################################

print('\n\nQuestion 2')

# Question 2

# 노드의 개수, 해의 개수를 카운트하기 위한 전역변수 선언
global num_of_nodes, num_of_ans
num_of_nodes = 0 
num_of_ans = 0

def promising(i, col) -> bool:
    k = 0 # 예제코드와 달리 0부터 시작하므로 k도 0으로 선언
    switch = True

    while k < i and switch == True:

        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:
            switch = False

        k += 1

    return switch

def queens(n, i, col):

    if promising(i, col) == True:
        if i == n - 1:

            # n개의 노드를 모두 찾은 경우, 해의 개수 1 추가
            global num_of_ans
            num_of_ans += 1

            # 노드 출력
            print('[', end = '')

            for j in range(0, n-1):
                print(col[j], end = ',')

            print(f'{col[n-1]}]')

        else:
            for j in range(n):
                col[i+1] = j

                global num_of_nodes
                num_of_nodes += 1

                queens(n, i+1, col)

n = 7
col = n * [0]
queens(n, -1, col)

print(f'노드 총 개수 : {num_of_nodes}')
print(f'해의 개수 : {num_of_ans}')
