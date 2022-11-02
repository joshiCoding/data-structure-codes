parent = []
rank = []

def initialize(n):
    for i in range(n):
        parent.append(i)
        rank.append(0)

# Simple Union-find operation
def find(x):
    if parent[x] == x : return x
    return find(parent[x])

def union(x,y):
    x = find(x)
    y = find(y)
    if (x == y): return
    parent[y] = x 

# union-find by rank and path compression
def find(x):
    if parent[x] == x : return x
    res = find(parent[x])
    parent[x] = res
    return res
def union(x,y):
    if rank[x] > rank[y]: parent[y] = x
    elif rank[x] < rank[y] : parent[x] = y
    else: 
        parent[y] = x
        rank[y] +=1


initialize(10)
union(0,1)
union(1,2)
union(1,3)
union(3,4)
union(4,5)
union(5,6)
union(7,8)
union(8,9)
print(parent)
print(find(9))