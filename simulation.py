import pygame
import random
import heapq
from collections import deque

# Constants
tile_size = 20
cols, rows = 30, 30
width, height = cols * tile_size, rows * tile_size

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128, 0, 128)

def generate_maze():
    maze = [[1 if random.random() > 0.3 else 0 for _ in range(cols)] for _ in range(rows)]
    maze[0][0] = 1  # Start point
    maze[rows - 1][cols - 1] = 1  # End point
    return maze

# BFS Algorithm
def bfs(maze):
    queue = deque([(0, 0)])
    came_from = {(0, 0): None}
    while queue:
        x, y = queue.popleft()
        if (x, y) == (rows - 1, cols - 1):
            return reconstruct_path(came_from, (x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1 and (nx, ny) not in came_from:
                queue.append((nx, ny))
                came_from[(nx, ny)] = (x, y)
    return []

# Function to reconstruct path
def reconstruct_path(came_from, end):
    path = []
    while end is not None:
        path.append(end)
        end = came_from[end]
    return path[::-1]

# Main visualization function
def visualize():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    maze = generate_maze()
    path = bfs(maze)
    
    running = True
    while running:
        screen.fill(WHITE)
        for y in range(rows):
            for x in range(cols):
                color = BLACK if maze[y][x] == 0 else WHITE
                pygame.draw.rect(screen, color, (x * tile_size, y * tile_size, tile_size, tile_size))
        
        for (x, y) in path:
            pygame.draw.rect(screen, BLUE, (y * tile_size, x * tile_size, tile_size, tile_size))
        
        pygame.display.flip()
        clock.tick(10)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    pygame.quit()

if __name__ == "__main__":
    visualize()
