

graph = {
    "S": [("A", 1), ("B", 4)],
    "A": [("C", 2)],
    "B": [("G", 5)],
    "C": [("G", 3)],
    "G": []
}
h = {"S": 5, "A": 4, "B": 4, "C": 2, "G": 0}
frontier = [(5, 0, "S", ["S"])]
expanded = []
while frontier:
    frontier.sort()
    f, cost, node, path = frontier.pop(0)
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
