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

def search(position, visited):
    if tree2[-1][position] not in visited:
        node = tree2[-1][position]
        visited.append(node)
    for x in range(len(tree2[position])):
        if tree2[position][x] and tree2[-1][x] not in visited:
            visited = search(x, list(visited))
    return visited

visited = search(0, [])

print(visited)
output = [words[i] for i in visited]
print(output)

