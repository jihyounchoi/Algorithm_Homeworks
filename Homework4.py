#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Utility:
    def print_matrix(d):
        m = len(d)
        n = len(d[0])
        
        for i in range(0, m):
            for j in range(0, n):
                print(f'{d[i][j]:4d}', end = " ")
            print()
            
    def print_matrixF(d):
        n = len(d[0])
        
        for i in range(0, n):
            for j in range(0, n):
                print(f'{d[i][j]:5.2f}', end = " ")
            print()
            
    def print_inorder(root):
        if not root:
            return
        print_inorder(root, l_child)
        print(root.data)
        print_inorder(root.r_child)
        
    def print_preorder(root):
        if not root:
            return
        print(root.data)
        print_preorder(root.l_child)
        print_preorder(root.r_child)
        
    def print_postorder(root):
        if not root:
            return
        
        print_postorder(root.l_child)
        print_postorder(root.r_child)
        print(root.data)


# In[2]:


'''
P matrix의 출력 부분에서, matrix를 A1 ~ A6이 아니라 A0 ~ A5로 설정하였습니다.
따라서 출력 부분에서 첫번째 row가 모두 1이 아니라 모두 0으로 되어 있습니다.
다른 값들도 모두 실습 때의 예상 출력 결과보다 1 작습니다.

order 함수에서의 재귀적 출력 시에는 A{i} 대신 A{i+1}를 사용하여 A1부터 표기되도록 하였습니다.
'''

def order(P : list, i, j):
    if i == j:
        print(f'A{i+1}', end = '')
    else:
        k = P[i][j];
        print('(', end = '')
        order(P, i, k)
        order(P, k + 1, j)
        print(')', end = '')

d = [5, 2, 3, 4, 6, 7, 8]
n = 6

M = [[0 for j in range(n)] for i in range(n)]
P = [[0 for j in range(n)] for i in range(n)]

for i in range(0, n):
    M[i][i] = 0

for diagonal in range(1, n):
    for i in range(0, n - diagonal):
        j = i + diagonal
        
        temp = [M[i][k] + M[k+1][j] + d[i]*d[k+1]*d[j+1] for k in range(i, j)] 
        # 리스트 표현식을 통해 min을 찾기 위한 후보 리스트
        
        M[i][j] = min(temp)
        P[i][j] = temp.index(M[i][j]) + i
        # ex) i = 3, temp[2]이 최소인 경우 : P[i][j] = 5

Utility.print_matrix(M)
print()
Utility.print_matrix(P)
order(P, 0, 5)

