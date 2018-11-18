# kruskal's algorithm finds the minimum spanning tree of a graph in polynomial time
class UndirectedGraph:
    def __init__(self):
        self.edges = []
        self.vertices = set()
    
    def add_edge(self, x1, x2, weight=1):
        self.edges.append((weight, x1, x2))
        self.vertices.add(x1)
        self.vertices.add(x2)

    def get_minimum_spanning_tree(self):
        mst = UndirectedGraph()
        self.edges.sort()

        for edge in self.edges:
            if len(mst.vertices) == len(self.vertices): break
            if edge[1] in mst.vertices and edge[2] in mst.vertices: continue            
            
            mst.add_edge(edge[1], edge[2], weight=edge[0])
        
        return mst
    
    def __str__(self):
        string = ''
        for edge in self.edges:
            string += '(V1: {}, V2: {}, Weight: {}) '.format(edge[1], edge[2], edge[0])
        return string

if __name__ == '__main__':
    graph = UndirectedGraph()
    
    graph.add_edge(1, 7, 1)
    graph.add_edge(2, 7, 3)
    graph.add_edge(3, 7, 4)
    graph.add_edge(4, 7, 1)
    graph.add_edge(5, 7, 3)
    graph.add_edge(6, 7, 1)

    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 3, 5)
    graph.add_edge(3, 4, 2)
    graph.add_edge(4, 5, 2)
    graph.add_edge(5, 6, 4)

    mst = graph.get_minimum_spanning_tree()
    print(mst)
