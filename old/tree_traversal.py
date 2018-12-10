from dictionary import words


tree = [[0, 1, 0, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        ["A", "B", "C", "D", "E"]]

tree2 = [[0,0,0,0,0,0,1],
         [0,0,1,1,0,0,0],
         [0,1,0,1,0,0,0],
         [0,1,1,0,1,0,1],
         [0,0,0,1,0,1,1],
         [0,0,0,0,1,0,1],
         [1,0,0,1,1,1,0],
         ["A", "B", "C", "D", "E", "F", "G"]]


def search(tree, position=0, visited=[]):
    if tree[-1][position] not in visited:
        node = tree[-1][position]
        visited.append(node)
    for x in range(len(tree[position])):
        if tree[position][x] and tree[-1][x] not in visited:
            visited = search(tree, x, list(visited))
    return visited


def breadth(tree, position=0, visited=[], queue=[]):
    for x in range(len(tree[position])):
        if tree[position][x] and tree[-1][x] not in visited and x not in queue:
            queue.append(x)
    visited.append(tree[-1][position])
    if queue != []:
        visited = breadth(tree, queue[0], visited, queue[1:])
    return visited


def breadth2(tree):
    visited = []
    queue = [0]
    while queue != []:
        pos = queue[0]
        visited.append(tree[-1][pos])
        for x in range(len(tree[0])):
            if tree[pos][x] and tree[-1][x] not in visited and x not in queue:
                queue.append(x)
        visited.append(queue[0])
        print(queue)
        queue.pop()
    return visited


visited_depth = search(tree)
print(visited_depth)

output = [words[i] for i in visited_depth]
print(" ".join(output))

visited_breadth  = breadth(tree)
print(visited_breadth)

output = [words[i] for i in visited_breadth]
print(" ".join(output))
