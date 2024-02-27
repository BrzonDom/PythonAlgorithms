class FindRoute:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent


def Traverse(node):
    result = []

    while node != None:
        result.append(node.name)
        node = node.parent

    return result


def Route(graph, start, goal):

    queue = [FindRoute(start)]
    known = {}
    known[start] = True

    while len(queue) > 0:
        actual = queue.pop(0)
        print(actual.name)

        if actual.name == goal:
            path = Traverse(actual)
            return path[::-1]

        if not actual.name in graph:
            continue

        for neighbor in graph[actual.name]:

            print("\t", neighbor)
            if not neighbor in known:
                known[neighbor] = True
                queue.append(FindRoute(neighbor, actual))

    return []


Graph = {}
Graph[0] = [1, 2, 5]
Graph[1] = [0, 2]
Graph[2] = [0, 1, 3]
Graph[3] = [2]

print(Graph)
print()

Path = Route(Graph, 0, 3)
print(Path)