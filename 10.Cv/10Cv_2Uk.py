"""
Načtení grafu ze souboru

    Mějme orientovaný graf, který má uzly očíslované od 1 do N. Hrany v tomto grafu jsou zadány v souboru, který na jedné řádce obsahuje definici jedné hrany, tedy dvě čísla:

        první číslo je číslo uzlu ze kterého vede hrana
        druhé číslo je číslo uzlu do kterého vede tato hrana

    Napište program path.py, který z příkazové řádky načte jméno souboru s definicí hran a číslo startovního uzlu a číslo koncového uzlu. Program vytiskne jednu z nejkratších cest ze startovního uzlu do cílového uzlu.

    Program otestujte na tomto souboru:

        1 2
        1 9
        2 3
        2 6
        3 4
        3 8
        4 6
        4 1
        5 4
        5 8
        6 8
        6 9
        7 4
        7 5
        8 7
        8 3
        9 5
        9 1

    Výsledek pro cestu z uzlu 2 do uzlu 5 je:

        2 6 9 5
"""

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

        if actual.name == goal:
            path = Traverse(actual)
            return path[::-1]
        if not actual.name in graph:
            continue
        for neighbor in graph[actual.name]:
            if not neighbor in known:
                known[neighbor] = True
                queue.append(FindRoute(neighbor, actual))

    return []


Graph = {}
Graph[1] = [2, 9]
Graph[2] = [3, 6]
Graph[3] = [4, 8]
Graph[4] = [1, 6]
Graph[5] = [4, 8]
Graph[6] = [8, 9]
Graph[7] = [4, 5]
Graph[8] = [3, 7]
Graph[9] = [1, 5]

print()
for i, line in enumerate(Graph):

    print(f"\t{i+1}: {Graph[line]}")

print("\n")

print(Route(Graph, 2, 5))

numList = ["one", "two", "three", "four", "five"]

numDict = {}

# numDict[1] = [numList[0]]
# numDict[1] += [numList[1]]
# numDict[2] = numList[2]

# print(numDict)

# print()
# for i, num in enumerate(numList):
#     numDict[i] = num
#
# print(numDict)
