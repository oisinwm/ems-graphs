class Graph:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], str):
            # In this case create a graph object from a given filename
            
            with open(args[0], "r") as sourceFile:
                rawGraph = sourceFile.readlines()

                # Windows Line Endings?
                #rawGraph.pop(1)
                # I guess remove this if not on windows
                
                nodes = rawGraph[1].replace("\n", "").split(", ")
                connections = rawGraph[2].replace("\n", "")
                
                connections = eval(connections) # This line is not so good, maybe change file format
                size = len(nodes)
                graph = [[0 for x in range(size)] for y in range(size)]

                if "undirected" in rawGraph[0]:
                    self._type = "undirected"
                    for edge in connections:
                        x = nodes.index(edge[0])
                        y = nodes.index(edge[1])
                        graph[y][x] = 1
                        graph[x][y] = 1

                elif "directed" in rawGraph[0]:
                    self._type = "directed"
                    for edge in connections:
                        x = nodes.index(edge[0])
                        y = nodes.index(edge[1])
                        graph[y][x] = 1

                else:
                    raise TypeError(f"Unknown graph type {rawGraph[0]}")

                self._nodes = nodes
                self._matrix = graph
            
        elif len(args) == 3:
            # In this case create a graph object from a type, list of nodes and list of connections
            # Since this is being done from code not a file, validation is required

            # Check graph type
            if args[0] in ["undirected", "directed"]:
                self._type = args[0]
            else:
                raise TypeError(f"Unknown graph type {args[0]}")

            # Check graph nodes
            if isinstance(args[1], list) and all(map(lambda x: isinstance(x, str), args[1])):
                self._nodes = args[1]
            else:
                raise TypeError(f"Invalid type in node names {args[1]}")

            # Check graph connections
            if isinstance(args[2], list) and all(map(lambda x: isinstance(x, tuple), args[2])):
                if all(map(lambda x: isinstance(x[0], str) and isinstance(x[1], str), args[2])):
                    connections = args[2]
                else:
                    raise TypeError(f"Invalid type in node connections {args[1]}")

                size = len(self._nodes)
                graph = [[0 for x in range(size)] for y in range(size)]

                if self._type == "undirected":
                    for edge in connections:
                        x = self._nodes.index(edge[0])
                        y = self._nodes.index(edge[1])
                        graph[y][x] = 1
                        graph[x][y] = 1
                else:
                    for edge in connections:
                        x = self._nodes.index(edge[0])
                        y = self._nodes.index(edge[1])
                        graph[x][y] = 1

            else:
                raise TypeError(f"Invalid type in node connections {args[1]}")
        else:
            # In this case create an empty graph object
            self._type = "directed"
            self._nodes = []
            self._matrix = []
        
    def __add__(self):
        raise NotADirectoryError

    def add_node(self, node):
        self._nodes += [str(node)]

        newMatrix = [i + [0] for i in self._matrix]
        newMatrix += [0 for i in range(len(newMatrix)+1)]
        self._matrix = newMatrix

    def del_node(self, node):
        raise NotADirectoryError

    def add_edge(self, edge):
        raise NotADirectoryError

    def del_edge(self, edge):
        raise NotADirectoryError

    def get_nodes(self):
        return self._nodes

    def get_edges(self):
        connections = []

        for x in range(len(self._matrix)):
            for y in range(len(self._matrix)):
                if self._matrix[y][x]:
                    connections.append((self._nodes[y], self._nodes[x]))

        return connections

    def write(self, filename):
        connections = []

        for x in range(len(self._matrix)):
            for y in range(len(self._matrix)):
                if self._matrix[y][x]:
                    connections.append((self._nodes[y], self._nodes[x]))

        with open(filename, "w") as file:
            file.write(str(self._type))
            file.write(", ".join(self._nodes))
            file.write(str(connections))


if __name__ == "__main__":
    a = Graph()
    b = Graph("undirected", ["A", "B"], [("A", "B")])
    c = Graph("../test_graphs/graph2.txt")

