import string


def pre_order(tree, visited, current):
    visited.append(tree[current][0])
    if tree[current][1] != None:
        visited = pre_order(tree, visited, tree[current][1])

    if tree[current][2] != None:
        visited = pre_order(tree, visited, tree[current][2])
    return visited


def in_order(tree, visited, current):
    if tree[current][1] != None:
        visited = in_order(tree, visited, tree[current][1])
    visited.append(tree[current][0])
    if tree[current][2] != None:
        visited = in_order(tree, visited, tree[current][2])
    return visited


def post_order(tree, visited, current):
    if tree[current][1] != None:
        visited = post_order(tree, visited, tree[current][1])
    if tree[current][2] != None:
        visited = post_order(tree, visited, tree[current][2])
    visited.append(tree[current][0])
    return visited


input_list = ["Daniel", "Charles", "George", "Belinda", "Cheryl", "Fred", ]
matrix = []


for node in input_list:
    if matrix == []:
        matrix.append([node, None, None])
    else:
        target = 0
        while target != None:
            if node < matrix[target][0]:
                #left
                prev = target
                target = matrix[target][1]
                direction = 1
            else:
                #right
                prev = target
                target = matrix[target][2]
                direction = 2
        matrix.append([node, None, None])
        matrix[prev][direction] = len(matrix) - 1


print(matrix)
print()
print(pre_order(matrix, [], 0))
print(in_order(matrix, [], 0))
print(post_order(matrix, [], 0))
