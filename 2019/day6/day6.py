import networkx as nx


def get_data(filename):
    with open(filename, 'r') as f:
        lst = [x for x in f.read().split('\n')]
        return lst


def to_pairs(lst):
    lst2 = [x.split(')') for x in lst]
    return lst2[:-1]


def create_graph(lst):
    G = nx.Graph()
    for x in lst:
        G.add_node(x[0])
        G.add_node(x[1])
        G.add_edge(x[0], x[1])

    return G


def total_orbits(G):
    s = 0
    for i in G.nodes:
        s += len(nx.shortest_path(G, "COM", i)) - 1
    return s


def you_to_santa(G):
    s = len(nx.shortest_path(G, "YOU", "SAN")) - 3
    return s
