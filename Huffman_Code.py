import heapq

global paths
paths = []

class Node:

    def __init__(self, symbol = '', freq = 0, left = None, right = None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def print_tree(root):
    
    quene = []
    quene.append(root)

    while len(quene) != 0 :
        node = quene[0]
        if node.left == None:
            ll = '-'
        else:
            ll = node.left.freq
        if node.right == None:
            rr = '-'
        else:
            rr = node.right.freq
        print('  {n}  \n _|_ \n|   |\n{l}   {r}\n==========='.format(n = node.freq, l = ll, r = rr))
        quene.pop(0)
        if node.left != None:
            quene.append(node.left)
        if node.right != None:
            quene.append(node.right)
    print('\n')

def find_all_paths(root, path : str):

    if root.left == None and root.right == None:
        global paths
        paths.append(path)
        return

    else:        
        if root.left != None:
            path += '0'
            find_all_paths(root.left, path)

        if root.right != None:
            path += '1'
            find_all_paths(root.right, path)




    
b = Node('b', 5)
e = Node('e', 10)
c = Node('c', 12)
a = Node('a', 16)
d = Node('d', 17)
t = Node('t', 25)

pq = [b, e, c, a, d, t]


for i in range(5):
    p = heapq.heappop(pq)
    q = heapq.heappop(pq)

    r = Node(freq = p.freq + q.freq, left = p, right = q)
    
    heapq.heappush(pq, r)

print_tree(pq[0])

find_all_paths(pq[0], '')


print(paths)


        
        

    
    
    













