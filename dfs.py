class Stack:
    def __init__(self):
        self.s = []
        
    def push(self,x):
        self.s.append(x)

    def pop(self):
        if self.isempty():
            print("stack is empty!")
            return None
        return self.s.pop()

    def isempty(self):
        if len(self.s) == 0:
            return True
        return False

def find_neighbors(current, maze, visited):
    a, b = current
    neighbors = []
    
    rows = len(maze)
    cols = len(maze[0])
    
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for dr, dc in directions:
        next_r = a + dr
        next_c = b + dc
        
        if 0 <= next_r < rows and 0 <= next_c < cols:
            if maze[next_r][next_c] is not None and maze[next_r][next_c] != 1:
                if (next_r,next_c) not in visited:
                    neighbors.append((next_r, next_c))
                
    return neighbors

def bfs():
    S = Stack()
    
    maze=[[0,1,0,0],
          [0,1,1,0],
          [0,0,0,0],
          [1,1,1,0]]
    
    current = ()
    start = (0,0)
    goal = (3,3)       
    
    S.push(start)
    visited = set()
    parent = {start: None}  # Track parent of each node
    
    while not S.isempty():
        current = S.pop()
        visited.add(current)
        
        if current == goal: 
            break
            
        neighbors = find_neighbors(current, maze, visited)
        
        if neighbors is not None:
            while len(neighbors) > 0:
                next_node = neighbors.pop(0)
                if next_node not in visited:
                    S.push(next_node)
                    parent[next_node] = current  # Store parent relationship
    
    # Reconstruct path from start to goal
    path = []
    if goal in parent:  # If goal was reached
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()  # Reverse to get path from start to goal
    else:
        print("Path not found\n")
    
    return path, maze # Added just to pass your list out of the function

def print_path_matrix(maze, path):
    rows = len(maze)
    cols = len(maze[0])
    
    # Loop through every row in the maze
    for r in range(rows):
        for c in range(cols):
            # If this position is in our path, print '*'
            if (r, c) in path:
                print("*", end=" ")
            else:
                # Otherwise, print the original maze value (0 or 1)
                print(maze[r][c], end=" ")
        print()

# Run everything
result_path, maze = bfs()
print_path_matrix(maze, result_path)

