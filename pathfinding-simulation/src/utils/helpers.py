import random

def is_valid_move(maze, x, y):
    """Check if a move is valid within the maze."""
    return (0 <= x < len(maze) and 
            0 <= y < len(maze[0]) and 
            maze[x][y] != 1)  # 1 represents wall

def reconstruct_path(came_from, current):
    """Reconstruct path from the came_from dictionary."""
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    return path[::-1]

def generate_maze(rows, cols, wall_density=0.3):
    """Generate a random maze with given dimensions."""
    maze = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if random.random() < wall_density:
                maze[i][j] = 1
    return maze