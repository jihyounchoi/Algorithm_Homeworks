import math
import copy

class Heap:
    
    def __init__(self, data):
        self.data = data
        self.size = len(self.data) - 1 
    # heap size를 하나 줄여야 한다. 인덱스는 1부터, 인덱스의 2* 연산이 가능하도록
    # 따라서 data 리스트의 첫 원소는 공통적으로 0으로 설정하고, 1번 인덱스부터 저장한다
    
    def add_elt(self, elt):
        self.data.append(elt)
        self.sift_up(self.size)


    def sift_up(self, i):
        while i >= 2:
            self.sift_down(i // 2)
            i = i // 2

    def sift_down(self, i): # i : index
        
        siftkey = self.data[i] # i번째 data의 값 (고정값)
        parent = i # i
        spotfound = False
        
        while 2 * parent <= self.size and not spotfound: 
            # 2 * parent <= size란, 현재 parent의 위치가 가장 하단부가 아님을 의미한다.
            
            if 2 * parent < self.size and self.data[2 * parent] < self.data[2 * parent + 1]:
                # 자식 노드가 존재하고, 오른쪽 자식 노드가 왼쪽 자식 노드보다 큰 경우
                largerchild = 2 * parent + 1
                
            else: # 왼쪽 자식 노드가 오른쪽 자식 노드보다 큰 경우
                largerchild = 2 * parent
            
            if siftkey < self.data[largerchild]: # 자식 노드가 더 큰 경우, 바꾼다
                
                # 중요) 굳이 swap하지 않아도, 아래 부분의 siftkey를 parent 인덱스에 대입하는 구문을 통해 최종적으로 swap이 가능하다
                self.data[parent] = self.data[largerchild] # 값과
                parent = largerchild # 인덱스를 각각 바꾼다
                
            else: # 바꿀 필요가 없는 경우
                spotfound = True # 위치 고정. 완료
                
        self.data[parent] = siftkey
        
    
    # 데이터가 입력되는 순서대로 heap을 매번 구성하는 방식으로 구현
    def make_heap1(self):
        for i in range(1, self.size + 1):
            self.sift_up(i)

    # 모든 데이터를 트리에 넣은 상태에서 heap을 구성하는 방식으로 구현
    def make_heap2(self):
        for i in range(self.size // 2, 0, -1):
            self.sift_down(i)

    def root(self):
        
        if self.size > 0:
            keyout = self.data[1]
            self.data[1] = self.data[self.size]
            self.size = self.size - 1

            self.sift_down(1)
            return keyout
        
        return


    def remove_keys(self):
        for i in range(self.size, 0, -1):
            self.data[i] = self.root() # root를 추출하여 역순으로 저장하므로, 결국 오름차순 정렬이 된다

def heap_sort(a):
    a.remove_keys()
    return a.data[::-1] # 내림차순으로 정렬하기 위해 순서를 반대로 뒤집어 출력

a = [0, 11, 14, 2, 7, 6, 3, 9, 5]

a1 = copy.deepcopy(a)
a2 = copy.deepcopy(a) # separate a1, a2

b1 = Heap(a1)
b2 = Heap(a2)

b1.make_heap1()
b2.make_heap2()

print('make heap by method 1 (b1):', b1.data)
print('make heap by method 2 (b2):', b2.data)

b1.add_elt(50)
b2.add_elt(50)

print('\n')
print('b1 data after adding element 50 :', b1.data)
print('b2 data after adding element 50 :', b2.data)

s1 = heap_sort(b1)
s2 = heap_sort(b2)

print('\nb1 result of heapsort\n', s1)
print('\nb2 result of heapsort\n', s2)
