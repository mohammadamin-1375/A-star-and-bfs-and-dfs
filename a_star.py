#AMIN SARKHOSH
#AMIRHOSSEIN RAZAVI
from collections import deque

class Graph:

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list
        global H
        H=dict()
        x=int(input("How many node do you have?"))
        for i in range(0,x):
            print("Enter nodes :")
            H[input("")]=1

    def get_neighbors(self, v):
        return self.adjacency_list[v]


    def h(self, n):
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):

        open_list = set([start_node])
        closed_list = set([])


        g = {}

        g[start_node] = 0

   
        parents = {}
        for v in open_list:
            if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                n = v

        if n == None:
            print('Path does not exist!')
            return None

        if n == stop_node:
            reconst_path = []

            while parents[n] != n:
                reconst_path.append(n)
                n = parents[n]
                
            reconst_path.append(start_node)

            reconst_path.reverse()

            print('Path found: {}'.format(reconst_path))
            return reconst_path


        for (m, weight) in self.get_neighbors(n):

            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + weight

            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)
        open_list.remove(n)
        closed_list.add(n)

        print('Path does not exist!')
        return None
def in_graph():
    graph=dict()
    while(1):
        b=[]
        y=input("Enter the node: ")
        x=int(input("How many nodes is it connected to?"))
        for i in range (0,x):
            node=[input("Nodes connected to %s : "%y ),int(input("Enter the route weight :"))]
            node=tuple(node)
            b.append(node)
        graph[y]=b
        if input("Are there any other nodes?")=="n":
            break
    for k, v in graph.items():
        print(k, v)
    return graph

graph2=Graph(in_graph())
graph2.a_star_algorithm(input("enter node start : "),input('Enter node targets :  '))
