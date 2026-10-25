class Queue:
    def __init__(self):
        self.q = []
        
    def inq(self,x):
        self.q.insert(0,x)

    def dq(self):
        if self.isempty():
            print("Queue is empty!")
            return None
        return self.q.pop()

    def isempty(self):
        if len(self.q) == 0:
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
    Q = Queue()
    
    maze=[[0,0,0,0],
          [0,1,1,0],
          [0,0,0,0],
          [1,1,1,0]]
    
    current = ()
    start = (0,0)
    goal = (3,3)       
    
    Q.inq(start)
    visited = set()
    parent = {start: None}  # Track parent of each node
    
    while not Q.isempty():
        current = Q.dq()
        visited.add(current)
        
        if current == goal: 
            break
            
        neighbors = find_neighbors(current, maze, visited)
        
        if neighbors is not None:
            while len(neighbors) > 0:
                next_node = neighbors.pop(0)
                if next_node not in visited:
                    Q.inq(next_node)
                    parent[next_node] = current  # Store parent relationship
    
    # Reconstruct path from start to goal
    path = []
    if goal in parent:  # If goal was reached
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()  # Reverse to get path from start to goal
    
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
        print() # Print a new line after each row is done

# Run everything
result_path, maze = bfs()
print_path_matrix(maze, result_path)

