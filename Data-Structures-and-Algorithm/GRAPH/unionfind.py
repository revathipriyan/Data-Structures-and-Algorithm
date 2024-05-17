# this graph algorithm is also called DIsjoint sets
parent=[]
n=7
for i in range(0,n+1):
    size = [1] * (n+1)
    parent.append(i)
print(size,parent) 

def findParent(node):
    if node == parent[node]:
        return node
    return findParent(parent[node])


def unionBySize(a,b):
    p_a = findParent(a)
    p_b = findParent(b)
    if p_a == p_b: return
    if size[p_a] < size[p_b]:
        parent[p_a] = p_b
        size[p_b] += size[p_a]
    else:
        parent[p_b] = p_a
        size[p_a] += size[p_b]

unionBySize(1,2)
unionBySize(2,3)
unionBySize(4,5)
unionBySize(6,7)
unionBySize(5,6)

print(size,parent)

if findParent(3) == findParent(7):
    print("same")
else:
    print("not same")

unionBySize(3,7)

if findParent(3) == findParent(7):
    print("same")

print(size,parent)