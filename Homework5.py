# utility.py를 별도의 파일로 만들지 않고,
# 과제 파일에 포함했습니다.

def printMatrix(d):
    m = len(d)
    n = len(d[0])

    for i in range(0, m):
        for j in range(0, n):
            print(f'{d[i][j]:5d}', end = " ")
        print()

def printMatrixF(d):
    n = len(d[0])

    for i in range(0, n):
        for j in range(0, n):
            print(f'{d[i][j]:5.5f}', end = " ")
        print()

def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)

def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)

def print_postOrder(root):
    if not root:
        return

    print_postOrder(root.l_child)
    print_postOrder(root.r_child)
    print(root.data)


class Node:
    def __init__(self, data):
        self.l_child = None
        self.r_child = None
        self.data = data
        
def tree(key, r, i, j):
    # r : 해당 범위의 root를 알려주는 역할
    # i, j : tree의 범위
    # key : node의 data
    
    k = r[i][j]
    
    if k == 0:
        return
    
    else:
        p = Node(key[k]) # data가 key[k]인 node 생성
        p.l_child = tree(key, r, i, k - 1)
        p.r_child = tree(key, r, k + 1, j)
        return p

# n을 1부터로 작성하고 싶은데, python은 0부터여서 index 0을 비워 둠
# key = [' ','A','B','C','D','E']
# p = [0, 1/15, ]

def optimal_bin_search_tree(key : list, p : list):
    
    n = len(p) - 1 # n = 4

    a = [[0 for j in range(0, n+2)] for i in range(0, n+2)]
    r = [[0 for j in range(0, n+2)] for i in range(0, n+2)]
    # n+2 by n+2 matrix 생성

    for i in range(1, n+1): # 1 ~ n
        a[i][i-1] = 0
        a[i][i] = p[i]
        r[i][i] = i
        r[i][i-1] = 0

    a[n+1][n] = 0
    r[n+1][n] = 0

    for diagonal in range(1, n):
        for i in range(1, n - diagonal + 1):
            j = i + diagonal

            # min(a[i][k-1] + a[k+1][j]) + P(i) + ... + P(j)
            temp = [a[i][k-1] + a[k+1][j] for k in range(i, j+1)]

            a[i][j] = min(temp) + sum(p[i:j+1])
            r[i][j] = temp.index(min(temp)) + i # k : argmin above

    minavg = a[1][n]

    printMatrixF(a)
    print()
    printMatrixF(r)
    
    print('\n')
          
    root = tree(key, r, 1, n)
    print_inOrder(root)
    print()
    print_preOrder(root)

print('<data1>\n')
key = [' ','A','B','C','D','E']
p = [0, 1/15, 2/15, 3/15, 4/15, 5/15]
optimal_bin_search_tree(key, p)

print('\n\n<data2>\n')
key = [' ','A','B','C','D','E','F','G','H']
p = [' ', 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8]
optimal_bin_search_tree(key, p)





print('\n ------------------ 문제 2번 ------------------\n\n')

a = ['G','A','C','T','T','A','C','C']
b = ['C','A','C','G','T','C','C','A','C','C']

# a = ['A','A','C','A','G','T','T','A','C','C']
# b = ['T','A','A','G','G','T','C','A']

m = len(a)
n = len(b)

table = [[0 for j in range(0, n+1)] for i in range(0, m+1)] # m + 1 by n + 1의 table 생성 (cost를 저장)
minindex = [[(0,0) for j in range(0, n+1)] for i in range(0, m+1)] # 해당 원소가 어느 지점에서 "이동해 왔는지"를 저장하는 matrix

for i in range(m-1, -1, -1): # m-1부터 0까지 역순으로 진행
    table[i][n] = table[i+1][n] + 2 # table의 맨 오른쪽 열에 대해 작성

for j in range(n-1, -1, -1):
    table[m][j] = table[m][j+1] + 2 # table의 맨 아래쪽 행에 대해 작성
    
# 구현
'''
1. table 나머지부분 채우기
2. minindex 작성하기
'''

'''
table을 작성하는 과정에서, 대각선 방향으로 진행하다보니 diagonal을 이용해 반복문을 세팅하는 것에 애를 먹어서..
다른 방향으로 작성해 보았습니다.
table의 맨 아래 행부터 채워 올리는 방식, 맨 오른쪽 열부터 왼쪽으로 채워오는 방식이 가능한데,
이중에 맨 오른쪽 행부터 채워 오는 방식을 사용했습니다.
'''
for col in range(n-1, -1, -1): # 각 col에 대해
    for row in range(m-1, -1, -1): # row를 아래부터 올려가며 진행
        table[row][col] = min(table[row+1][col+1] + (a[row] != b[col]), table[row+1][col] + 2, table[row][col+1] + 2)
        # penalty를 따로 구하지 않고, min 구문 안에 포함시킴
        # a[row] == b[col]인 경우에 0, 다른 경우에 1을 리턴


# minindex 행렬을 작성하는 함수
def min_index(i,j):
    
    # 아래쪽이 2 작으면 min_index는 자신의 아래쪽
    if table[i][j] - table[i+1][j] == 2: 
        minindex[i][j] = (i+1, j)
        
        if i+1 < m: # 아래쪽 끝에 도달하지 않은 경우
            min_index(i+1, j) # 함수 재귀호출
            
            
    # 오른쪽이 2 작으면 min_index는 자신의 오른쪽
    elif table[i][j] - table[i][j+1] == 2:
        minindex[i][j] = (i, j+1)
        
        if j < n-1: # 오른쪽 끝에 도달하지 않은 경우
            min_index(i, j+1) # 재귀호출
            
            
    else: # 둘다 아닌 경우 -> 우측 아래 (cost가 0)
        minindex[i][j] = (i+1, j+1)
        
        if i < m-1 and j < n-1: # 오른쪽 아래에 도달하지 않은 경우
            min_index(i+1, j+1) # 재귀호출

min_index(0,0) # 초기조건

printMatrix(table)

x = 0
y = 0

# tx, ty는 x, y의 trace개념. 
while x<m and y<n:
    
    tx, ty = x, y
    print(minindex[x][y])
    
    (x, y) = minindex[x][y]
    
    if x == tx + 1 and y == ty + 1: # x, y가 모두 1씩 커지므로, 양쪽 list에서 염기서열을 하나씩 추가해야 함을 의미
        print(a[tx], " ", b[ty]) # 
        
    elif x == tx and y == ty + 1: # y만 1 증가하므로, b만 염기서열을 추가하고 a는 틈을 생성함
        print(" - ", " ", b[ty])
         
    else: # b만 틈을 생성함
        print(a[tx], " ", " -")
