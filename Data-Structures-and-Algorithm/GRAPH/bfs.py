# BFS SEARCH ON GRAPH 
graph = {
'0':['1','2'],
'1':['0','2','3'],
'2':['0','1','4'],
'3':['1','4'],
'4':['2','3']
}
visited =[]
queue=[]
def bfs(visited, queue, node):
    visited.append(node)
    queue.append(node)

    while queue:
        pointer = queue.pop(0)
        # queue.extend(graph[pointer])
        for i in graph[pointer]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    print(visited)

bfs(visited=visited,queue=queue,node='0')