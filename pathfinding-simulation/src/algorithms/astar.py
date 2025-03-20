import heapq
from src.utils.helpers import is_valid_move, reconstruct_path

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, end):
    g_score = {start: 0}
    f_score = {start: manhattan_distance(start, end)}
    came_from = {start: None}
    open_set = [(f_score[start], start)]
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == end:
            return reconstruct_path(came_from, end)
            
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
                    
    return []  # No path found