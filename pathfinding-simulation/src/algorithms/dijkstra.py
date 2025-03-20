import heapq
from src.utils.helpers import is_valid_move, reconstruct_path

def dijkstra(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    distances = {start: 0}
    visited = {start: None}
    pq = [(0, start)]
    path = []
    animation_steps = []
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        animation_steps.append((current[0], current[1], 6))  # Currently visiting
        
        if current == end:
            path = reconstruct_path(visited, end)
            break
            
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x, next_y = current[0] + dx, current[1] + dy
            next_pos = (next_x, next_y)
            
            if is_valid_move(maze, next_x, next_y):
                new_dist = current_dist + 1
                
                if next_pos not in distances or new_dist < distances[next_pos]:
                    distances[next_pos] = new_dist
                    visited[next_pos] = current
                    heapq.heappush(pq, (new_dist, next_pos))
                    animation_steps.append((next_x, next_y, 5))  # Visited
    
    # Add path to animation
    for pos in path:
        animation_steps.append((pos[0], pos[1], 4))  # Path
        
    return animation_steps