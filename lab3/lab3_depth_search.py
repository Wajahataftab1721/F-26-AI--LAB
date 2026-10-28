
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}
def dls(node, goal, limit, path):
    if node == goal:
        return "FOUND", path
    if limit == 0:
        if graph[node]:
            return "CUTOFF", None
        return "FAILURE", None
    cutoff = False
    for next_node in graph[node]:
        if next_node not in path:
            status, found_path = dls(
                next_node, goal, limit - 1, path + [next_node]
            )
            if status == "FOUND":
                return "FOUND", found_path
            if status == "CUTOFF":
                cutoff = True
    if cutoff:
        return "CUTOFF", None
    return "FAILURE", None
for limit in range(1, 5):
    status, path = dls("A", "G", limit, ["A"])
    print("Depth Limit:", limit)
    print("Status:", status)
    print("Path:", path if path else "Not found")
    print()
