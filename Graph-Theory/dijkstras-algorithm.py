from collections import defaultdict
from min_heap import MinHeap

def better_track_exists(min_track, best_tracks):
    last_v = min_track['path'][-1]
    return last_v in best_tracks and best_tracks[last_v]['w'] <= min_track['w']
def at_destination(min_track, v_end): 
    return min_track['path'][-1] == v_end

# for simplification, the graph will be undirected
class UndirectedGraph:
    def __init__(self):
        # dict of list of dicts: {..., 'v_name': [{'v1': , 'v2': , 'w': }, ...]}
        self.vertex_edges = defaultdict(list)
    
    # parameters: names of verticies
    def add_edge(self, v1, v2, weight=1):
        self.vertex_edges[v1].append({'v1': v1, 'v2': v2, 'w': weight})
        self.vertex_edges[v2].append({'v1': v2, 'v2': v1, 'w': weight})

    # parameters: names of verticies
    def shortest_path(self, v_start, v_end):
        # item structure: {'w': 11, 'path': ['va', 'vb', ...]}
        priority_queue = MinHeap(criterion='w')
        # structure: {..., 'v_name': {'w': 11, 'path': ['va', 'vb',...] }}
        best_tracks = {}
        
        curr_track = {'path': [v_start], 'w': 0, 'v': v_start}
        while True:
            for edge in self.vertex_edges[curr_track['v']]:
                new_track = {
                    'w': curr_track['w'] + edge['w'],
                    'path': curr_track['path'] + [edge['v2']]
                }
                priority_queue.insert(new_track)
            
            assert priority_queue.is_empty() == False
            min_track = priority_queue.getMin()
            
            while better_track_exists(min_track, best_tracks):
                min_track = priority_queue.getMin()
            
            if at_destination(min_track, v_end):
                return min_track
            
            best_tracks[min_track['path'][-1]] = min_track            
            curr_track = min_track.copy()
            curr_track['v'] = min_track['path'][-1]


if __name__ == '__main__':
    graph = UndirectedGraph()
    
    graph.add_edge('v0', 'v1', 1)
    graph.add_edge('v0', 'v5', 3)
    graph.add_edge('v0', 'v4', 5)
    graph.add_edge('v1', 'v2', 8)
    graph.add_edge('v1', 'v4', 4)
    graph.add_edge('v1', 'v5', 1)
    graph.add_edge('v1', 'v3', 7)
    graph.add_edge('v2', 'v3', 2)
    graph.add_edge('v2', 'v4', 3)
    graph.add_edge('v4', 'v3', 5)
    graph.add_edge('v5', 'v4', 2)

    print(graph.shortest_path('v0', 'v2'))
