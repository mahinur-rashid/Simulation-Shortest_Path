from src.utils.helpers import is_valid_move, reconstruct_path

def dfs(maze, start, end):
    stack = [start]
    visited = {start: None}
    
    while stack:
        current = stack.pop()
        if current == end:
            return reconstruct_path(visited, end)
            
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
            next_x, next_y = current[0] + dx, current[1] + dy
            next_pos = (next_x, next_y)
            
            if is_valid_move(maze, next_x, next_y) and next_pos not in visited:
                stack.append(next_pos)
                visited[next_pos] = current
                
    return []  # No path found