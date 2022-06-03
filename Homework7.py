# sum of subsets
print('Question1\n')

global W_1, n_1, total_node_1 # 2번 문제와 변수명이 겹치는 관계로 _1 네이밍을 추가하였음
W_1 = 15
n_1 = 5
total_node_1 = 0

def promising(i, weight, total):
    condition1 = weight + total >= W_1
    condition2 = weight == W_1 or weight + w[i+1] <= W_1
    # 가장 마지막 원소까지 온 경우에는 인덱스 범위를 초과함

    return (condition1 and condition2)

def s_s(i, weight, total, include):

    if i == n_1-1: # indexing error을 피하기 위해 if문을 사용함
        
        if weight == W_1:
            print('Answer :', include[:i+1])
            return
        
        else:
            return

    if promising(i, weight, total):
        include[i+1] = 1

        global total_node_1
        total_node_1 += 1

        s_s(i+1, weight + w[i+1], total - w[i+1], include)
        include[i+1] = 0

        total_node_1 += 1
        s_s(i+1, weight, total-w[i+1], include)

w = [1, 2, 3, 4, 15]

print("items = ", w, ", W = ", W_1)
include = n_1 * [0]
total = 0

for k in w:
    total += k

s_s(-1, 0, total, include)
    
print('total nodes :', total_node_1)

##############################################
print('\n\nQuestion2\n')
##############################################
# m-coloring

global n_2, m, total_node_2
n_2 = 5
m = 3
total_node_2 = 0

def color(i, vcolor):
    global n_2, m, total_node_2

    if promising(i):
        if i == n_2 - 1:
            print(vcolor[:n_2])
        else:
            for c in range(1, m+1):
                vcolor[i+1] = c
                total_node_2 += 1
                color(i+1, vcolor)

def promising(i):
    switch = True
    j = 0
    while j<i and switch:
        if W[i][j] and vcolor[i] == vcolor[j]:
            switch = False
        j += 1
    
    return switch

W = [[0,1,1,0,1],[1,0,1,1,0],[1,1,0,1,0],[0,1,1,0,1],[1,0,0,1,0]]
vcolor = n_2 * [0]
color(-1, vcolor)

print('total created nodes :', total_node_2)
# m = 1, m = 2인 경우에는 해를 찾을 수 없고, m = 3부터 해가 발생한다
