#AMIN SARKHOSH
#AMIRHOSSEIN RAZAVI
from collections import deque
def in_graph():
    graph=dict()
    while(1):
        b=[]
        y=input("Enter the node: ")
        x=int(input("How many nodes is it connected to?"))
        for i in range (0,x):
            b.append(input("Nodes connected to %s : "%y ))
        graph[y]=b
        if input("Are there any other nodes?")=="n":
            break
    for k, v in graph.items():
        print(k, v)
    return graph

def bfs(start, goal, graph):
    queue = deque([start])
    visited = {start: None}

    while queue:
        cur_node = queue.popleft()
        if cur_node == goal:
            break

        next_nodes = graph[cur_node]
        for next_node in next_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited[next_node] = cur_node
    return visited
g=in_graph()
start = input("enter start node:")
goal = input("enter goal node:")
visited = bfs(start, goal, g)
cur_node = goal
print(f'\npath from {start} to {goal}: \n {goal} ', end='')
while cur_node != start:
    cur_node = visited[cur_node]
    print(f'---> {cur_node} ', end='')

