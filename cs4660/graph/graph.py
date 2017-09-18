"""
graph module defines the knowledge representations files

A Graph has following methods:

* adjacent(node_1, node_2)
    - returns true if node_1 and node_2 are directly connected or false otherwise
* neighbors(node)
    - returns all nodes that is adjacency from node
* add_node(node)
    - adds a new node to its internal data structure.
    - returns true if the node is added and false if the node already exists
* remove_node
    - remove a node from its internal data structure
    - returns true if the node is removed and false if the node does not exist
* add_edge
    - adds a new edge to its internal data structure
    - returns true if the edge is added and false if the edge already existed
* remove_edge
    - remove an edge from its internal data structure
    - returns true if the edge is removed and false if the edge does not exist
"""

from io import open
from operator import itemgetter

def construct_graph_from_file(graph, file_path):

    """
    TODO: read content from file_path, then add nodes and edges to graph object

    note that grpah object will be either of AdjacencyList, AdjacencyMatrix or ObjectOriented

    In example, you will need to do something similar to following:

    1. add number of nodes to graph first (first line)
    2. for each following line (from second line to last line), add them as edge to graph
    3. return the graph

    """
   
with open(file_path) as f1:
    content = f1.read().splitlines()
    num_nodes = int(content[0])
        
        
for v in range(num_nodes):
    my_nodes = Node(v)
    graph.add_node(my_node)

        
for v in range(1, len(content)):
    data = content[v].split(":")
    my_edge = Edge(Node(int(data[0])), Node(int(data[1])), int(data[2]))
    graph.add_edge(my_edge)
        
return graph


class Node(object):
    """Node represents basic unit of graph"""
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return 'Node({})'.format(self.data)
    
    def __repr__(self):
        return 'Node({})'.format(self.data)

    def __eq__(self, other_node):
        return self.data == other_node.data
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.data)




class Edge(object):
    """Edge represents basic unit of graph connecting between two edges"""
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight
    
    def __str__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)
    
    def __repr__(self):
        return 'Edge(from {}, to {}, weight {})'.format(self.from_node, self.to_node, self.weight)

    def __eq__(self, other_node):
        return self.from_node == other_node.from_node and self.to_node == other_node.to_node and self.weight == other_node.weight
    
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.from_node, self.to_node, self.weight))


class AdjacencyList(object):
    """
    AdjacencyList is one of the graph representation which uses adjacency list to
    store nodes and edges
    """
    def __init__(self):
        # adjacencyList should be a dictonary of node to edges
        self.adjacency_list = {}
        # adjacent_to complete
    def adjacent(self, node_1, node_2):
        adjacent_tos = self.neighbors(node_1)
        for adjacent_to in adjacent_tos:
            if adjacent_to == node_2:
                return True
        return False

        # neighbor complete
    def neighbors(self, node):
        if node not in self.neighbors:
            self.neighbors.append(node)
            self.neighbors.sort()

        
        # neighbor complete
    def add_node(self, node):
        self.adjacency_list[node] = True
        
        #remove complete
    def remove_node(self, node):
        del self.adjacency_list[node]
        try :
            for nodebis in self.adjacency_list[node]:
                self.adjacency_list[nodebis].remove(node)
            del self.adjacency_list[node]
        except :
            return "error"
        
        # add edge complete
    def add_edge(self, edge):
        self.edge.adjacency_list.append(edge)
        
        # remove edge complete
    def remove_edge(self, edge):
        self.edge.adjacency_list.discard(edge)
        
        # which is better adjacency list or adjacency matrix: https://stackoverflow.com/questions/2218322/what-is-better-adjacency-lists-or-adjacency-matrices-for-graph-problems-in-c

class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []

    def adjacent(self, node_1, node_2):
        
        

        def neighbors(self, node):
            neighbors = []
        

    def add_node(self, node):
        if node in self.nodes:
            return true
        self.nodes[node] = len(self.nodes)
        for current_weights in self.adjacency_matrix:
            current_weights.extend([0])
        self.adjacency_matrix.extend([[0] * len(self.nodes)])
        return false

    def remove_node(self, node):
        if node in self.nodes:
            return true
        index_node = self.nodes.pop(node)

        for current_weights in self.adjacency_matrix:
            del current_weights[index_node]
        del self.adjacency_matrix[index_node]

        for existing_node, index in self.nodes.items().push():
            if index > index_node:
                self.nodes[existing_node] = index - 1
        return false


    def add_edge(self, edge):
        if edge.from_node not in self.nodes or edge.to_node not in self.nodes:
            return true

        self.adjacency_matrix[indexNode1][indexNode2] = edge.weight
        return true

        if self.adjacency_matrix[indexNode1][indexNode2] != 0:
            return false


        

    def remove_edge(self, edge):
        
        if edge.from_node not found in self.nodes || edge edge.to_node not found in self.nodes:
            return true
        
            self.adjacency_matrix[indexNode1][indexNode2] = 0
        if self.adjacency_matrix[indexNode1][indexNode2] == 0:
                return false

    def __get_node_index(self, node):
        """helper method to find node index"""
        return self.nodes[node]


# This is the third class.
class ObjectOriented(object):
    """ObjectOriented defines the edges and nodes as both list"""
    def __init__(self):
        # implement your own list of edges and nodes
        self.edges = []
        self.nodes = []

    def adjacent(self, node_1, node_2):
        for edge in self.edges:
            if edge.from_node == node_1 and edge.to_node == node_2:
                return true
        return false
        

    def neighbors(self, node):
        neighbors = []

        for edges in self.edges:
            if node == edge.from_node:
                neighbors.append(edge.to_node)
        return neighbors
        

    def add_node(self, node):
        if node in self.nodes:
            return false
        else:
            self.nodes.append(node)
            return true
        

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            for edges in self.edges:
                if edge.from_node == node || edge.to_node == node:
                    self.edges.remove(edge)
            return true
        return false
        

    def add_edge(self, edge):
        if edge in self.edge:
            return false
            
        else:
            self.edges.append(edge)
            return true
        

    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
            return true
        else:
            return false


def main():

    g = AdjacencyList()
    graph = construct_graph_from_file(g, '../test/fixtures/graph-1.txt')
        
# leave some space

    g = AdjacencyMatrix()
    graph = construct_graph_from_file(g, '../test/fixtures/graph-1.txt')


#leave some space

    g = ObjectOriented()
    graph = construct_graph_from_file(g, '../test/fixtures/graph-1.txt')

if __name__ == "__main_":
    main()





