

# m = [[0 for c in range(6)] for r in range(6)]
# for row in m:
#     print(row)

graph = [[0, 1, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0]]

edge_lst = []
neig_lst = {}

print("Oriented Graph:", end="\n\t")
for row in graph:
    for col in row:
        print(col, end=" ")
    print("\n", end="\t")
print()

for r in range(len(graph)):
    for c in range(r+1, len(graph[r])):
        # print(graph[r][c], end=" ")

        if graph[r][c]:
            # if not r in neigh:
            edge_lst.append([r, c])

            if r in neig_lst:
                neig_lst[r] += [c]
            else:
                neig_lst[r] = [c]

    # print("\n", end="\t")

print("Edges:", end="\n\t")
print(edge_lst)
print()

print("Neighbours:", end="\n\t")
print(neig_lst)

# for edge in edge_lst:
#     print(edge)
#
#     # if edge[0] in neig_lst:
#     #     neig_lst[edge[0]] += [edge[1]]
#     # else:
#     #     neig_lst[edge[0]] = [edge[1]]
