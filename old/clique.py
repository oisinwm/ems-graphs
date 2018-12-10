def create_matrix(size):
    return [[0 for x in range(size)] for y in range(size)]


def prune(graph_in, nodes_in):
    del_list = []
    for n in range(len(graph_in)):
        if sum(graph_in[n]) <= 1:
            del_list.append(nodes_in[n])
    for node in del_list:
        x = nodes.index(node)
        del graph_in[x]
        del nodes_in[x]
        for row in graph_in:
            del row[x]
    return graph, nodes


def expand(clique_list):
    result = []
    if len(max(clique_list, key=len)) == 3:
        return result
    else:
        for x in clique_list:
            if len(x) > 3:
                for i in x:
                    y = set(x)
                    y.remove(i)
                    if y not in result:
                        result.append(y)

        return result + expand(result)


def read_to_matrix(filename):
    with open(filename, "r") as file:
        rawGraph = file.readlines()

    if "undirected" not in rawGraph[0]:
        raise NotImplemented("directed graphs not yet implemented")

    #Windows Line Endings?
    rawGraph.pop(1)
    
    nodes = rawGraph[1].replace("\n", "").split(", ")
    connections = rawGraph[2].replace("\n", "")
    
    connections = eval(connections)
    graph = create_matrix(len(nodes))

    for edge in connections:
        x = nodes.index(edge[0])
        y = nodes.index(edge[1])
        graph[y][x] = 1
        graph[x][y] = 1

    return graph, nodes


def traverse(graph, nodes):
    cliques = []
    for i in range(len(nodes)):
        visited = []
        current = nodes[i]

        connections = [nodes[x] for x in range(len(graph[nodes.index(current)])) if graph[nodes.index(current)][x] not in [0, float("inf")]]
        connected_set = set(connections)
        clique = connected_set.union(set([current]))
        visited.append(current)

        for current in connections:
            connections = [nodes[x] for x in range(len(graph[nodes.index(current)])) if graph[nodes.index(current)][x] not in [0, float("inf")]]
            clique = clique.intersection(set(connections).union([current]))
            visited.append(current)
            if clique == set(visited):
                if clique not in cliques and len(clique) >= 3:
                    cliques.append(clique)

    #Final answer, all cliques len > 2
    return cliques + expand(cliques)


if __name__ == "__main__":
    graph, nodes = read_to_matrix("graph2.txt")

    before = nodes
    graph, after = prune(graph, before)
    while before != after:
        before = nodes
        graph, after = prune(graph, before)
    nodes = after

    cliques = traverse(graph, nodes)

    print(cliques)

