import heapq
from collections import defaultdict
times = [[2,1,1],[2,3,1],[3,4,1]]
n = 4
k = 2

def networkDelay():
    edges = defaultdict(list)
    for u,v,w in times:
        edges[u].append((v,w))
    minheap =[(0,k)]
    visit = set()
    t=0
    while minheap:
        w1,n1 = heapq.heappop(minheap)
        if n1 in visit:
            continue
        visit.add(n1)
        t = max(t,w1)
        for n2, w2 in edges[n1]:
            if n2 not in visit:
                heapq.heappush(minheap,(w1+w2,n2))
    return t if len(visit) == n else -1

a=networkDelay()
print(a)