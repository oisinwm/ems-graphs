import random
import math


def base26name(num):
    alpha = "ABCDEFGHIJKLMNOPQRTSUVWXYZ"
    ans = ""
    if num in [0, 1]:
        return alpha[num]
    else:
        maxi = math.floor(math.log(num, 26))
        for power in range(maxi, -1, -1):
            ind = num % (26 ** power)
            ans += alpha[ind]
            num -= ind * (26 ** power)
    return ans[::-1]


nodes = int(input("How many nodes: "))
edges = int(input("How many edges: "))
graph_type = input("Graph type (undirected | directed): ")
weights = input("Graph weights (unweighted | weighted): ")

node_set = [base26name(i) for i in range(0, nodes)]
connections = []

while len(connections) != edges:
    node_a = random.choice(node_set)
    node_b = random.choice(node_set)
    connection = [node_a, node_b]
    if weights == "unweighted":
        if graph_type == "undirected":
            if tuple(connection) not in connections and tuple(connection[::-1]) not in connections:
                connections.append(tuple(connection))
        else:
            if tuple(connection) not in connections:
                connections.append(tuple(connection))
    else:
        # Not yet implemented
        if graph_type == "undirected":
            if tuple(connection) not in connections and tuple(connection[::-1]) not in connections:
                connections.append(tuple(connection))
        else:
            if tuple(connection) not in connections:
                connections.append(tuple(connection))


print(node_set)
print(connections)
