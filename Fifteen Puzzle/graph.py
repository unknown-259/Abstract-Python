# assignment: programming assignment 4
# author: Nathan Tran
# date: 05/29/23
# file: graph.py is a program with the Vertex class and the Graph class
# input: item from parameter
# output: return specified items

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.color = 'white'

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        # From Google Colab
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        # From Google Colab
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList.values()

    def addEdge(self,f,t,weight=0):
        # From Google Colab
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
    def breadth_first_search(self, s):
        # From Google Colab
        for v in self.vertList.values():
            v.color = 'white'
        queue = []
        path = [] # not a part of BFS, used to check the order of vertices traversed by BFS
        start = self.vertList[ s]
        start.color = 'gray'
        queue.append(start)
        path.append(start.id)
        while len(queue) != 0:
            v = queue.pop(0)
            for u in v.connectedTo.keys():
                if u.color == 'white':
                    u.color = 'gray'
                    queue.append(u)
                    path.append(u.id)
            v.color = 'black'
        return path # not a part of BFS
    
    def depth_first_search(self):
        # From Google Colab
        for v in self.vertList.values():
            v.color = 'white'
        path = [] # not a part of DFS, used to check the order of vertices traversed by DFS
        for v in self.vertList.values():
            if v.color == 'white':
                self.DFS(v.id, path)
        return path
    
    def DFS(self, vid, path):
        # From Google Colab
        v = self.vertList[ vid]
        v.color = 'gray'
        path.append(v.id)
        for u in v.connectedTo.keys():
            if u.color == 'white':
                self.DFS(u.id, path)
        v.color = 'black'
        return path

# if __name__ == '__main__':

#     g = Graph()
#     for i in range(6):
#         g.addVertex(i)
        
#     g.addEdge(0,1)
#     g.addEdge(0,5)
#     g.addEdge(1,2)
#     g.addEdge(2,3)
#     g.addEdge(3,4)
#     g.addEdge(3,5)
#     g.addEdge(4,0)
#     g.addEdge(5,4)
#     g.addEdge(5,2)

#     for v in g:
#         print(v)

#     assert (g.getVertex(0) in g) == True
#     assert (g.getVertex(6) in g) == False
        
#     print(g.getVertex(0))
#     assert str(g.getVertex(0)) == '0 connectedTo: [1, 5]'

#     print(g.getVertex(5))
#     assert str(g.getVertex(5)) == '5 connectedTo: [4, 2]'

#     path = g.breadth_first_search(0)
#     print('BFS traversal by discovery time (preordering): ', path)
#     assert path == [0, 1, 5, 2, 4, 3]
    
#     path = g.depth_first_search()
#     print('DFS traversal by discovery time (preordering): ', path)
#     assert path == [0, 1, 2, 3, 4, 5]