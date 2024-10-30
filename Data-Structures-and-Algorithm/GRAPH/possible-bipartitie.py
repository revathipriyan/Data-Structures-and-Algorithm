from collections import defaultdict

def bipartite(edges, color):
    
    curr = dislikes[0][0]
    # curr_color = 1
    queue = [curr]
    # color[1] = curr_color
    visit = set()

    while queue:
        print("yes")
        key = queue.pop()
        curr = key
        visit.add(key)
        curr_color = color[key]
        if color[key] == -1:
            color[key] = 1
            curr_color = 1
        for each_dislike in edges[key]:
            if color[each_dislike] == -1:
                color[each_dislike] = 1 - curr_color
            else:
                if color[each_dislike] != 1-curr_color:
                    return False
            if each_dislike not in visit:
                queue.append(each_dislike)
                
        visit.add(key)
        if len(visit) != n and not queue:
            new_key = color[1:].index(-1) + 1
            queue.append(new_key)
            visit.add(new_key)


    return True

        







if __name__ == "__main__":
    n = 10
    dislikes = [[5,9],[5,10],[5,6],[5,7],[1,5],[4,5],[2,5],[5,8],[3,5]]
    edges = defaultdict(list)

    for x,y in dislikes:
        edges[x].append(y)
        edges[y].append(x)

    color  =   [-1] * (n  + 2)
    if bipartite(edges, color):
        print("BIPARTITE GRAPH")
    else:
        print("NOT A BIPARTITE GRAPH")

    
        
