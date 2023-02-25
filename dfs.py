#AMIN SARKHOSH
#AMIRHOSSEIN RAZAVI
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


visited = set()

def dfs(visited, graph, node):  
    if node not in visited :
        print (node)
        visited.add(node)        
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    
graph=in_graph()
print("Following is the Depth-First Search")
start = input("enter start node:")
dfs(visited, graph, start)
