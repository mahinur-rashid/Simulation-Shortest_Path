import heapq
from src.utils.helpers import is_valid_move, reconstruct_path

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, end):
    g_score = {start: 0}
    f_score = {start: manhattan_distance(start, end)}
    came_from = {start: None}
    open_set = [(f_score[start], start)]
    path = []
    animation_steps = []
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        animation_steps.append((current[0], current[1], 6))  # Currently visiting
        
        if current == end:
            path = reconstruct_path(came_from, end)
            break
            
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x, next_y = current[0] + dx, current[1] + dy
            neighbor = (next_x, next_y)
            
            if is_valid_move(maze, next_x, next_y):
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + manhattan_distance(neighbor, end)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
                    animation_steps.append((next_x, next_y, 5))  # Visited
    
    # Add path to animation
    for pos in path:
        animation_steps.append((pos[0], pos[1], 4))  # Path
        
    return animation_steps