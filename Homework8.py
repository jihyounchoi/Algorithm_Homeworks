import queue
import copy  # 깊은 복사를 위해 copy 라이브러리를 import하였음

##################################################
# Question1
##################################################

global n, maxProfit, bestset, total_nodes
n = 4
maxProfit = 0
bestset = n * [0]
total_nodes = 1


class Node1:
    def __init__(self, level, weight, profit, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.include = include


def kp_bfs():
    global maxProfit
    global bestset
    global total_nodes
    global n

    q = queue.Queue()
    v1 = Node1(0, 0, 0, n * [0])  # 노드 초기화

    q.put(v1)

    while not q.empty():

        v1 = q.get()

        u1 = Node1(0, 0, 0, v1.include)
        u1.level = v1.level + 1
        u1.weight = v1.weight + w[u1.level - 1]  # index 범위가 0부터 시작함에 따라 level - 1로 탐색
        u1.profit = v1.profit + p[u1.level - 1]
        u1.include[u1.level - 1] = 1

        if u1.weight <= W and u1.profit > maxProfit:
            maxProfit = u1.profit
            bestset = copy.deepcopy(u1.include)
            # include가 수정되는 경우 bestset이 함께 변경되는 것을 막기 위함

        total_nodes += 1
        # 아래의 if문이 실행되는 것이 노드를 탐색하는 것을 의미하므로, total_node에 1을 추가한다

        if comp_bound1(u1) > maxProfit:
            u_copy1 = copy.deepcopy(u1)
            # u1이 변경됨에 따라 q 내부의 u가 함께 변경되는 것을 막기 위하여 깊은 복사를 사용함
            q.put(u_copy1)

        u1.weight = v1.weight
        u1.profit = v1.profit
        u1.include[u1.level - 1] = 0

        total_nodes += 1
        # 아래의 if문이 실행되는 것이 노드를 탐색하는 것을 의미하므로, total_node에 1을 추가한다

        if comp_bound1(u1) > maxProfit:
            u_copy2 = copy.deepcopy(u1)
            # u1이 변경됨에 따라 q 내부의 u가 함께 변경되는 것을 막기 위하여 깊은 복사를 사용함
            q.put(u_copy2)


def comp_bound1(u):

    if u.weight >= W:
        return 0
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight

        while j <= n and totweight + w[j - 1] <= W:
            totweight = totweight + w[j - 1]
            result = result + p[j - 1]
            j += 1

    k = j

    if k <= n:
        result = result + (W - totweight) * p[k - 1] / w[k - 1]

    return result


W = 6
p = [30, 28, 18, 20]
w = [3, 4, 3, 5]

kp_bfs()

print("Question1 ")
print("total nodes to search :", total_nodes)
print("max profit :", maxProfit)
print("best set :", bestset)


maxProfit = 0
bestset = n * [0]
n = 4


##################################################
# Question2
##################################################


class Node2:
    def __init__(self, level, weight, profit, bound, include):
        self.level = level
        self.weight = weight
        self.profit = profit
        self.bound = bound
        self.include = include

    def __lt__(self, other):
        return self.bound < other.bound


def kp_best_fs():
    global maxProfit
    global bestset

    temp = n * [0]
    v2 = Node2(0, 0, 0, 0, temp)
    q = queue.PriorityQueue()

    v2.bound = comp_bound2(v2)

    q.put(v2)

    while not q.empty():

        v2 = q.get()
        u2 = Node2(0, 0, 0, 0, v2.include)

        if v2.bound < maxProfit:
            u2.level = v2.level + 1
            u2.weight = v2.weight + w[u2.level - 1]
            u2.profit = v2.profit - p[u2.level - 1]
            u2.include[u2.level - 1] = 1

            if (
                u2.weight <= W and u2.profit < maxProfit
            ):  # -를 취한 값끼리의 비교이므로, 작은 경우가 best에 해당한다
                bestset = copy.deepcopy(u2.include)
                # u2가 변경됨에 따라 bestset이 함께 변경되는 것을 막기 위하여 깊은 복사를 사용함
                maxProfit = u2.profit

            u2.bound = comp_bound2(u2)

            if u2.bound < maxProfit:  # -를 취한 값끼리의 비교이므로, 작아야 한다.
                u_copy1 = copy.deepcopy(u2)
                # u2가 변경됨에 따라 q 내부의 u가 함께 변경되는 것을 막기 위하여 깊은 복사를 사용함
                q.put(u_copy1)

            u2.weight = v2.weight
            u2.profit = v2.profit
            u2.bound = comp_bound2(u2)
            u2.include[u2.level - 1] = 0

            if u2.bound < maxProfit:  # -를 취한 값끼리의 비교이므로, 작아야 한다.
                u_copy2 = copy.deepcopy(u2)
                q.put(u_copy2)


# 위의 1번 문제와 달리, bound 값을 음수로 리턴하므로 별개의 함수를 사용한다.
def comp_bound2(u):

    if u.weight >= W:
        return 1
    else:
        result = u.profit
        j = u.level + 1
        totweight = u.weight

        while j <= n and totweight + w[j - 1] <= W:
            totweight = totweight + w[j - 1]
            # comp_bound1과 절댓값은 같고 부호만 다른 값을 리턴해야 하므로, result +가 아니라 result -로 구현한다
            result = result - p[j - 1]
            j += 1

    k = j

    if k <= n:
        # 앞과 마찬가지로, result + 가 아니라 result - 를 사용한다
        result = result - (W - totweight) * p[k - 1] / w[k - 1]

    return result


W = 6
p = [30, 28, 18, 20]  # 입력은 양수로 받고, 내부 구현에서만 음수를 취한 값을 사용함
w = [3, 4, 3, 5]

include = [0] * n

kp_best_fs()

print("\nQuestion2")
print("max profit :", -1 * maxProfit)  # 음수로 계산한 값을 양수로 출력하기 위해 -를 붙인다
print("best set :", bestset)
