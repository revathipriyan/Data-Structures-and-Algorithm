graph = [[1,2],[2,3],[5],[0],[5],[],[]]

def safeState(graph):
    n = len(graph)
    safe = {}

    def dfs(i):
        if i in safe:
            return safe[i]
        safe[i] = False
        for nei in graph[i]:
            if not dfs(nei):
                return False
        safe[i] = True
        return True
    
    res= []
    for i in range(n):
        if dfs(i):
            res.append(i)

    return res
print(safeState(graph))
