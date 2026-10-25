# Graph with edge costs
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1, 'D': 7},
    'C': {'A': 4, 'B': 1, 'D': 3, 'E': 5},
    'D': {'B': 7, 'C': 3, 'E': 2},
    'E': {'C': 5, 'D': 2}
}

# Heuristic values
h = {'A': 7, 'B': 6, 'C': 4, 'D': 2, 'E': 0}


# Greedy Best-First Search
def greedy(start, goal):
    visited = set()
    queue = [(h[start], start)]
    parent = {start: None}

    while queue:
        queue.sort()
        _, node = queue.pop(0)

        if node == goal:
            break

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                parent[neighbor] = node
                queue.append((h[neighbor], neighbor))

    if node != goal:
        print("Greedy: No path found")
        return

    path = []
    while node:
        path.append(node)
        node = parent[node]

    print("Greedy Path:", path[::-1])


# A* Search
def astar(start, goal):
    queue = [(h[start], start)]
    cost = {start: 0}
    parent = {start: None}
    visited = set()

    while queue:
        queue.sort()
        _, node = queue.pop(0)

        if node in visited:
            continue

        if node == goal:
            break

        visited.add(node)

        for neighbor, weight in graph[node].items():
            new_cost = cost[node] + weight

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                parent[neighbor] = node
                queue.append((new_cost + h[neighbor], neighbor))

    if node != goal:
        print("A*: No path found")
        return

    path = []
    while node:
        path.append(node)
        node = parent[node]

    print("A* Path:", path[::-1])
    print("Total Cost:", cost[goal])


# Main program
start = input("Enter start node (A-E): ").upper()
goal = input("Enter goal node (A-E): ").upper()

if start not in graph or goal not in graph:
    print("Invalid node!")
else:
    greedy(start, goal)
    astar(start, goal)