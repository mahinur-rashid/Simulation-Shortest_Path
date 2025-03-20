import pygame
import time
from src.ui.grid import Grid
from src.utils.helpers import generate_maze
from src.algorithms.bfs import bfs
from src.algorithms.dfs import dfs
from src.algorithms.astar import astar
from src.algorithms.dijkstra import dijkstra

def main():
    pygame.init()
    
    # Constants
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 600
    GRID_SIZE = 30
    TILE_SIZE = 20
    
    # Create window and screen
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pathfinding Algorithms Visualization")
    clock = pygame.time.Clock()
    
    # Create grids
    grids = [Grid(GRID_SIZE, GRID_SIZE, TILE_SIZE) for _ in range(4)]
    algorithm_names = ["BFS", "DFS", "A*", "Dijkstra"]
    algorithms = [bfs, dfs, astar, dijkstra]
    
    # Generate maze
    maze = generate_maze(GRID_SIZE, GRID_SIZE)
    for grid in grids:
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                grid.set_cell(i, j, maze[i][j])
    
    running = True
    start_point = None
    end_point = None
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                grid_x = y // TILE_SIZE
                grid_y = (x % (WINDOW_WIDTH // 4)) // TILE_SIZE
                
                if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
                    if maze[grid_x][grid_y] == 0:  # Valid cell
                        if start_point is None:
                            start_point = (grid_x, grid_y)
                            for grid in grids:
                                grid.set_cell(grid_x, grid_y, 2)
                        elif end_point is None:
                            end_point = (grid_x, grid_y)
                            for grid in grids:
                                grid.set_cell(grid_x, grid_y, 3)
                            
                            # Run algorithms
                            for i, (grid, algo) in enumerate(zip(grids, algorithms)):
                                path = algo(maze, start_point, end_point)
                                grid.update_path(path)
                                
                            start_point = None
                            end_point = None
        
        # Draw grids
        screen.fill((128, 128, 128))
        for i, grid in enumerate(grids):
            # Create surface for each grid
            surface = pygame.Surface((WINDOW_WIDTH // 4, WINDOW_HEIGHT))
            grid.draw_grid(surface)
            
            # Draw algorithm name
            font = pygame.font.Font(None, 36)
            text = font.render(algorithm_names[i], True, (255, 255, 255))
            surface.blit(text, (10, 10))
            
            # Draw grid surface
            screen.blit(surface, (i * (WINDOW_WIDTH // 4), 0))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()