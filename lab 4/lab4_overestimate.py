

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}
h = {"S": 5, "A": 4, "B": 4, "C": 10, "G": 0}
frontier = [(5, 0, "S", ["S"])]
expanded = []
while frontier:
    best = 0
    i = 1
    while i < len(frontier):
        if frontier[i][0] < frontier[best][0]:
            best = i
        i += 1
    f, cost, node, path = frontier.pop(best)
    if node == "G":
        print("Path:", path)
        print("Cost:", cost)
        print("Processed nodes:", expanded + ["G"])
        print("Expansion count:", len(expanded))
        break
    expanded.append(node)
    for next_node, edge_cost in graph[node]:
        new_cost = cost + edge_cost
        new_f = new_cost + h[next_node]
        new_path = path + [next_node]
        frontier.append((new_f, new_cost, next_node, new_path))
