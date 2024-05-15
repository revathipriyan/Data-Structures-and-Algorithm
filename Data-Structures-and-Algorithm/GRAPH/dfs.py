graph = {
'0':['1','2','3'],
'1':['0'],
'2':['0','4'],
'3':['0','4'],
'4':['2','3']
}

visited = []

def dfs(visisted,graph, node):
    if node not in visisted:
        visited.append(node)
        for i in graph[node]:
            dfs(visisted,graph,i)

dfs(visited,graph,node='0')
print(visited)