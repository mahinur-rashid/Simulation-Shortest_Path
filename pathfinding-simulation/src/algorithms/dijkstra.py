import heapq
from src.utils.helpers import is_valid_move, reconstruct_path

def dijkstra(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    distances = {start: 0}
    visited = {start: None}
    pq = [(0, start)]
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current == end:
            return reconstruct_path(visited, end)
            
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_x, next_y = current[0] + dx, current[1] + dy
            next_pos = (next_x, next_y)
            
            if is_valid_move(maze, next_x, next_y):
                new_dist = current_dist + 1
                
                if next_pos not in distances or new_dist < distances[next_pos]:
                    distances[next_pos] = new_dist
                    visited[next_pos] = current
                    heapq.heappush(pq, (new_dist, next_pos))
                    
    return []  # No path found