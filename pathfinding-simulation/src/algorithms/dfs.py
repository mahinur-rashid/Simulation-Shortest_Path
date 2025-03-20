from src.utils.helpers import is_valid_move, reconstruct_path

def dfs(maze, start, end):
    stack = [start]
    visited = {start: None}
    path = []
    animation_steps = []
    
    while stack:
        current = stack.pop()
        animation_steps.append((current[0], current[1], 6))  # Currently visiting
        
        if current == end:
            path = reconstruct_path(visited, end)
            break
            
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x, next_y = current[0] + dx, current[1] + dy
            next_pos = (next_x, next_y)
            
            if is_valid_move(maze, next_x, next_y) and next_pos not in visited:
                stack.append(next_pos)
                visited[next_pos] = current
                animation_steps.append((next_x, next_y, 5))  # Visited
    
    # Add path to animation
    for pos in path:
        animation_steps.append((pos[0], pos[1], 4))  # Path
        
    return animation_steps