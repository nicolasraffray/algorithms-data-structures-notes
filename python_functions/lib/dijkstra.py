graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}


def dijkstra(graph, start, end):
    print(graph)
    costs = {}
    parents = {}
    unseen_nodes = graph
    infinity = float('inf')
    final_path = []

    for node in unseen_nodes:
        costs[node] = infinity
    costs[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node == None:
                min_node = node
            elif costs[node] < costs[min_node]:
                print("Here is the cost: ", costs[node])
                min_node = node

        for child, weight in graph[min_node].items():
            if weight + costs[min_node] < costs[child]:
                costs[child] = weight + costs[min_node]
                parents[child] = min_node
        unseen_nodes.pop(min_node)
    # print(parents)
    # print(costs)
    current_node = end
    while current_node != start:
        try:
            final_path.insert(0, current_node)
            current_node = parents[current_node]
        except KeyError:
            print('path cannot be reached')
            break
    final_path.insert(0, start)
    return final_path


path = dijkstra(graph, 'start', 'fin')
print(path)
