n = 6
headID = 2
manager = [2,2,-1,2,2,2]
informTime = [0,0,1,0,0,0]
from collections import defaultdict
dct=defaultdict(list)
for i in range(n):
    dct[manager[i]].append(i)
    
lst=[0]*n
mx=0
queue=[headID]
while queue:
    x=queue.pop(0)
    for j in dct[x]:
        lst[j]=(informTime[x]+lst[x])
        mx=max(mx,lst[j])
        queue.append(j)
print(mx)