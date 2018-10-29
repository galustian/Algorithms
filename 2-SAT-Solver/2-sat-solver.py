from collections import defaultdict
from math import log2, ceil
import numpy as np


class DirectedGraph:
    def __init__(self):
        self.num_edges = 0
        self.graph = defaultdict(list)
        self.vertices = set()

    def add_edge(self, from_=None, to_=None):
        self.graph[from_].append(to_)
        self.num_edges += 1
        self.vertices.add(from_)
        self.vertices.add(to_)
        self.vertices.add(neg(from_))
        self.vertices.add(neg(to_))
    
    # returns dict of dicts
    def compute_reachability_matrix(self):
        vertices_list = list(self.vertices)
        reachable_rows = []
        for v1 in vertices_list:
            row = []
            for v2 in vertices_list:
                if v1 in self.graph and v2 in self.graph[v1]: row.append(1)
                else: row.append(0)
            
            reachable_rows.append(row)

        reachability_matrix = np.array(reachable_rows, dtype='int64')
        reachability_matrix += np.identity(len(reachability_matrix), dtype='int64')

        for i in range(ceil(log2(self.num_edges))):
            reachability_matrix = reachability_matrix @ reachability_matrix
        
        # convert reachability_matrix to dict of dicts
        reachability = {}

        for i in range(len(vertices_list)):
            vertex_1 = vertices_list[i]
            reachability[vertex_1] = {}
            for j in range(len(vertices_list)):
                vertex_2 = vertices_list[j]
                reachability[vertex_1][vertex_2] = reachability_matrix[i][j]

        return reachability


def neg(x):
    if x[0] == 'n': return x[1:]
    return 'n' + x


def all_set(verticies_list, vertex_vals):
    for vertex in verticies_list:
        if vertex not in vertex_vals: return False
    return True

def all_true(verticies_list, vertex_vals):
    for vertex in verticies_list:
        if vertex in vertex_vals and vertex_vals[vertex] == False:
            return False
    return True

def unit_clause_propagation(graph, vertex_vals, curr_true_vertex):
    if curr_true_vertex in vertex_vals and vertex_vals[curr_true_vertex] == False:
        return False
    
    vertex_vals[curr_true_vertex] = True
    vertex_vals[neg(curr_true_vertex)] = False
    
    # all vertex implications already set
    if all_set(graph.graph[curr_true_vertex], vertex_vals):
        if all_true(graph.graph[curr_true_vertex], vertex_vals):
            return True        
        return False
    
    for impl_vertex in graph.graph[curr_true_vertex]:
        # if contradiction: return False
        if impl_vertex in vertex_vals and vertex_vals[impl_vertex] == False:
            return False
        
        vertex_vals[impl_vertex] = True
        vertex_vals[neg(impl_vertex)] = False
    
    for impl_vertex in graph.graph[curr_true_vertex]:
        return unit_clause_propagation(graph, vertex_vals, impl_vertex)


# param. format: [('1', '2'), ('1', 'n3'), ('n1', '4')]
# equivalent to: (x1 or x2) and (x1 or not x3) and (not x1 or x4)
# returns values for boolean variables: {'1': True, 'n1': False, '4': False, ...}
# returns None if contradiction
def sat_2_solver(clause_tuples_list):
    # create graph
    graph = DirectedGraph()
    for clause in clause_tuples_list:
        graph.add_edge(neg(clause[0]), clause[1])
        graph.add_edge(neg(clause[1]), clause[0])

    reachability = graph.compute_reachability_matrix()

    # {'1': True, 'n1': False, '4': False, ...}
    vertex_vals = {}
    
    for vertex in reachability:
        if vertex in vertex_vals: continue
        
        if reachability[vertex][neg(vertex)] != 0:            
            if unit_clause_propagation(graph, vertex_vals, neg(vertex)) == False: return None
        elif reachability[neg(vertex)][vertex] != 0:
            if unit_clause_propagation(graph, vertex_vals, vertex) == False: return None
        else:
            if unit_clause_propagation(graph, vertex_vals, neg(vertex)) == False: return None

    return vertex_vals

if __name__ == '__main__':
    boolean_expression_satisfiable1 = [('1', 'n2'), ('n1', '3'), ('2', '1')]
    boolean_expression_satisfiable2 = [('1', 'n2'), ('n1', 'n3'), ('2', '3'), ('1', '2')]
    boolean_expression_not_satisfiable = [('1', 'n2'), ('n1', 'n3'), ('2', '3'), ('1', '2'), ('n2', '3')]
    print("Satisfiable:", sat_2_solver(boolean_expression_satisfiable1))
    print("Satisfiable:", sat_2_solver(boolean_expression_satisfiable2))
    print("Not Satisfiable:", sat_2_solver(boolean_expression_not_satisfiable))