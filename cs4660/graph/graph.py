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

    # watch video for code to build graphs
    # https://www.youtube.com/watch?v=HDUzBEG1GlA&t=196s
   
    with open(file_path) as f1:
        content = f1.read().splitlines()
        num_nodes = int(content[0])
        
        
    for v in range(num_nodes):
        my_nodes = Node(v)
        graph.add_node(my_nodes)

        
    for v1 in range(1, len(content)):
        values = content[v].split(":")
        my_edge = Edge(Node(int(values[0])), Node(int(values[1])), int(values[2]))
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



# This is the edge object. It makes up the edge of the graph. 
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
        # link two nodes in a graph
    """def adjacent(self, node_1, node_2):
        adjacent_tos = self.neighbors(node_1)
        for adjacent_to in adjacent_tos:
            if adjacent_to == node_2:
                return True
        return False
"""
    def adjacent(self, node_1, node_2):
        # link two nodes
        """if node_1 not in self.adjacency_list or node_2 not in self.adjacency_list:
            return False
        elif node_1 in self.adjacency_list[node_2] and node_2 in self.adjacency_list[node_1]:
            return False
        else:
            self.adjacency_list[node_1].append(node_2)
            self.adjacency_list[node_2].append(node_1)
            return True 
        """
        adjacent_neighbors = self.neighbors(node_1)
        for neighbor in adjacent_neighbors:
            if neighbor == node_2:
                return True
        return False 
        # end method adjacent, complete



        # neighbor complete
    def neighbors(self, node):
        """if node not in self.neighbors:
            self.neighbors.append(node)
            self.neighbors.sort()
        return []"""
        if node not in self.adjacency_list:
            return []
        else:
            return list(map((lamda edge: edge.to_node), self.adjacency_list[node]))
        # end method neighbors, complete


        
        # neighbor complete
    def add_node(self, node):
        """self.adjacency_list[node] = True"""
        # Add a node to the graph if not already present
        if node in self.adjacency_list:
            return False
        else:
            self.adjacency_list[node] = []
            return True



        #remove complete
    def remove_node(self, node):
        """del self.adjacency_list[node]
        try :
            for nodebis in self.adjacency_list[node]:
                self.adjacency_list[nodebis].remove(node)
            del self.adjacency_list[node]
        except :
            return "error"
        """
        if node not in self.adjacency_list:
            return False
        else:
            for v in self.adjacency_list:
                if node in self.adjacency_list[v]:
                    self.adjacency_list[v].remove(node)
            del self.adjacency_list[node]
            return True 

        # add edge complete
    def add_edge(self, edge):
        if edge.from_node not in self.adjacency_list or edge.to_node not in self.adjacency_list:
            return False

        my_edges = self.adjacency_list[edge.from_node]
        for my_edge in my_edges:
            if edge == my_edge:
                return False
        
        my_edges.append(edge)
        return True
        
        # remove edge complete
    def remove_edge(self, edge):
        """self.edge.adjacency_list.discard(edge)"""
        
        # which is better adjacency list or adjacency matrix: https://stackoverflow.com/questions/2218322/what-is-better-adjacency-lists-or-adjacency-matrices-for-graph-problems-in-c
        """if edge.from_node in self.adjacency_list:
            return False
        if edge.to_node in self.adjacency_list[edge.from_node]:
            self.adjacency_list[edge.from_node].remove(edge.to_node)
            return True
        """
        # cleaner this way
        adj_edge_to_remove = self.adjacency_list[edge.from_node]
        if edge not in adj_edge_to_remove:
            return False
        adj_edge_to_remove.remove(edge)
        return True




class AdjacencyMatrix(object):
    def __init__(self):
        # adjacency_matrix should be a two dimensions array of numbers that
        # represents how one node connects to another
        self.adjacency_matrix = []
        # in additional to the matrix, you will also need to store a list of Nodes
        # as separate list of nodes
        self.nodes = []
        # complete
    def adjacent(self, node_1, node_2):
        """if node_1 not in self.nodes or node_2 not in self.nodes:
            return False
        if self.adjacency_matrix[node_1.data][node_2.data] != 0:
            return True
        """
        for edge in self.adjacency_matrix[self.__get_node_index(node_1)]:
            if edge.to_node == node_2:
                return True
            else:
                return False
    # end adjacent method, compelte. 

    # complete
    def neighbors(self, node):
        neighbors = []
        for edge in self.adjacency_matrix[self.__get_node_index(node)]:
            neighbors.append(edge.to_node)
        return neighbors
        """for v in range(len(self.adjacency_matrix[node_1.data][node_2.data])):
            if self.adjacency_matrix[node.data][v] != 0:
                neighbors.append(Node(v))
        return neighbors
        """
        #neighbors method complete


    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.adjacency_matrix.append([])
            self.nodes.append(node)
            return True
        # add node method complete. 
        """
        my_temp = self.adjacency_matrix = [[0 for v in range(node.data+1)] for w in range(node.data+1)]
        my_length = len(self.adjacency_matrix) if len(my_temp) > len(self.adjacency_matrix) else len(my_temp)
        
        for v in range(my_length):
            for q in range(my_length):
                if my_temp[v][q] != 0:
                    self.adjacency_matrix[v][q] = my_temp[v][q]
        return True
        """

    def remove_node(self, node):
        """if node in self.nodes:
            return True
        index_node = self.nodes.pop(node)

        for current_weights in self.adjacency_matrix:
            del current_weights[index_node]
        del self.adjacency_matrix[index_node]

        for existing_node, index in self.nodes.items().pop(node):
            if index > index_node:
                self.nodes[existing_node] = index - 1
        return False
        """
        if node not in self.nodes:
            return False
        else:
            self.nodes.remove(node)
            for v, edges in range(len(self.adjacency_matrix)):
                for edge in edges:
                    if edge.to_node == node or edge.from_node == node:
                        self.adjacency_matrix[v].remove(edge)
            return True

            #remove_node method complete. 

    def add_edge(self, edge):
        if edge not in self.adjacency_matrix[self.__get_node_index(edge.from_node)]:
            self.adjacency_matrix[self.__get_node_index(edge.from_node)].append(edge)
            return True
        else:
            return False 
        # add_edge method complete. 

            """.from_node not in self.nodes or edge.to_node not in self.nodes:
            return False

        if self.adjacency_matrix[edge.from_node.data][edge.to_node.data] == edge.weight:
            return True

        if self.adjacency_matrix[edge.from_node.data][edge.to_node.data] != 0:
            return False
         """

    def remove_edge(self, edge):        
        """if edgefrom_node not in self.nodes or edge.to_node not in self.nodes:
            return True
        if self.adjacency_matrix[edge.from_node.data][edge.to_node.data] == 0:
            return False
        if self.adjacency_matrix[edge.from_node.data][edge.to_node.data] == 0:
            return True
            """
        if edge not in self.adjacency_matrix[self.__get_node_index(edge.from_node)]:
            return False
        else:
            self.adjacency_matrix[self.__get_node_index(edge.from_node)].remove(edge)
            return True 

        # remove_edge method complete 

    def __get_node_index(self, node):
        """helper method to find node index"""
        return self.nodes.index(node)


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
                return True
        return False
    #adjacent method complete

    def neighbors(self, node):
        neighbor = []

        for edge in self.edges:
            if edge.to_node not in neighbor and edge.from_node == node:
                neighbors.append(edge.to_node)
        return neighbor

    #neighbors method complete
        

    def add_node(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            return True
      #add_nodes method complete  
      
    def remove_node(self, node):
        if node in self.nodes:
            return False 
            self.nodes.remove(node)
            for edge in self.edges:
                if edge.from_node == node or edge.to_node == node:
                    self.edges.remove(edge)
            return True
     # remove_node complete
        

    def add_edge(self, edge):
        if edge in self.edges:
            return False
            
        else:
            self.edges.append(edge)
            return True
        #add_edges method complete

    def remove_edge(self, edge):
        if edge not in self.edges:
            return False 
        else:
            self.edges.remove(edge)
            return True
        
    #remove edges method complete

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





