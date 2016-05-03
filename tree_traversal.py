import time
import collections

__author__ = 'Josua Lopez-Binder'
__contact__ = 'joshlobinder@gmail.com'

class Node(object):
    def __init__(self,name):
        self.name = name

    def neighbors(self,adjacency_list):
        return adjacency_list[self]

    def __str__(self):
        return str(self.name)

    def __repr__(self):
        return str(self.name)

nElements = 8
nodes = [Node(i) for i in range(nElements)]
graph = {
    nodes[0]: [nodes[1],nodes[2]],
    nodes[1]: [nodes[0],nodes[3],nodes[4]],
    nodes[2]: [nodes[0],nodes[5],nodes[6]],
    nodes[3]: [nodes[1],nodes[7]],
    nodes[4]: [],
    nodes[5]: [],
    nodes[6]: [],
    nodes[7]: [],
}
'''
              0
           1     2
         3  4    5 6 
        7
'''

def timed(function):
    def wrapped(graph,nodes):
        start_time = time.clock()
        function(graph,nodes)
        return time.clock() - start_time
    return wrapped

depthOrder = []
@timed
def depth_first_traverse(graph,nodes):
    fakeNode = Node(-1)
    depth_first_search_visit(graph,nodes[1],fakeNode)

def depth_first_search_visit(graph,node,prevNode):
    depthOrder.append(node)
    for neighbor in node.neighbors(graph):
        if neighbor != prevNode:
            depth_first_search_visit(graph,neighbor,node)

breadthOrder = []
@timed
def breadth_first_traverse(graph,nodes):
    breadth_first_visit(graph,nodes[1])

def breadth_first_visit(graph,node):
    visited = []
    queue = collections.deque([node])
    while True:
        try:
            u = queue.popleft()
            breadthOrder.append(u)
        except IndexError:
            break
        visited.append(u)
        for neighbor in u.neighbors(graph):
            if neighbor not in visited:
                queue.append(neighbor)

if __name__ == "__main__":
    print "Depth First Traversal"
    time_taken = depth_first_traverse(graph,nodes)
    print depthOrder 
    print "time to traverse: {}".format(time_taken)

    print "Breadth First Traversal"
    time_taken = breadth_first_traverse(graph,nodes)
    print breadthOrder 
    print "time to traverse: {}".format(time_taken)





