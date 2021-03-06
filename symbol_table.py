import queue
# Very simple implementation using a binary search tree
# Assumes that keys are strings
class MapStr:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.left = None
            self.right = None

    def __init__(self):
        self.first = None
        self.length = 0

    def put_(self, key, val, node=None):
        if self.first is None:
            self.first = self.Node(key, val)
            self.length = 1
            return

        # Create Node if does not exist
        if node is None:
            node = self.Node(key, val)
            self.length += 1
            return
        
        # Update Node if exists
        if key == node.key:
            node.val = val
            return
        
        # Traverse binary-tree
        if key < node.key:
            if node.left is None:
                node.left = self.Node(key, val)
                self.length += 1
                return
            self.put_(key, val, node.left)
        else:
            if node.right is None:
                node.right = self.Node(key, val)
                self.length += 1
                return
            self.put_(key, val, node.right)

    def put(self, key, val):
        self.put_(key, val, self.first)
        
    def get(self, key, node=None, depth=0):
        if depth == 0:
            return self.get(key, self.first, 1)
        # KeyError
        if node is None:
            raise KeyError
        
        if key == node.key:
            return node.val
        
        if key < node.key:
            return self.get(key, node.left, 1)
        else:
            return self.get(key, node.right, 1)
    
    def __contains__(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def get_items(self, node, q=None):
        if node == None:
            return []

        if node.left is not None:
            self.get_items(node.left, q)
        
        q.put((node.key, node.val))

        if node.right is not None:
            self.get_items(node.right, q)     
        
    def __iter__(self):
        q = queue.Queue()
        self.get_items(self.first, q=q)
        items = []
        while not q.empty():
            items.append(q.get())
        
        for tup in items:
            yield tup
    
    def __len__(self):
        return self.length
    
# Tests
if __name__ == '__main__':
    str_map = MapStr()
    
    str_map.put('one', 7)
    str_map.put('car', 42)
    str_map.put('auto', 69)
    str_map.put('auto', 666)
    str_map.put('zebra', 3.14)
    str_map.put('yard', 64)

    assert str_map.get('car') == 42
    assert str_map.get('one') == 7
    assert str_map.get('auto') == 666

    assert ('one' in str_map) == True
    assert ('two' in str_map) == False
    assert len(str_map) == 5

    # Must be sorted alphabetically
    for key, val in str_map:
        print(key, val)