import networkx as nx
from networkx.algorithms import bipartite
from matplotlib import pyplot as plt

#can create a random bipartite/regular graph
#can input a graph to see if it is bipartite or not

class BipartiteCheck():
    def __init__(self):
        self.G = nx.Graph()
        self.a_nodes = []
        self.b_nodes = []
        self.random = None
    
    def create_random_bitartite(self, a_num, b_num ):
        self.a_nodes = ['a'+ str(i) for i in range(a_num)]
        self.b_nodes= ['b' + str(j) for j in range(b_num)]
        
        self.G.add_nodes_from(self.a_nodes, bipartite=0)
        self.G.add_nodes_from(self.b_nodes, bipartite=1)
        
        #edges will be created between every node
        edges_list = []
        for a in self.a_nodes:
            for j in self.b_nodes:
                edge = (a, j)
                edges_list.append(edge)
        
        self.G.add_edges_from(edges_list)
        
        #confirm that the created graph is bipartite
        
        if bipartite.is_bipartite(self.G):
            print('Created a Bipartite Graph')
        return self.G
        
    def draw_bipartite(self):
        nx.draw_networkx(self.G, pos = nx.drawing.layout.bipartite_layout(self.G, self.a_nodes), width = 2)
        plt.show()

    def create_random_graph(self, node_num):
        G = nx.random_regular_graph(node_num)
        self.random = G
        return G

    def checkifbipartite(self, graph):
        if not bipartite.is_bipartite(graph):
            print('Is not a bipartite graph')
        else:
            print('Is Bipartite')
        
