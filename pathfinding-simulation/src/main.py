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
    
    # Enhanced constants
    WINDOW_WIDTH = 1600
    WINDOW_HEIGHT = 800
    GRID_SIZE = 25
    TILE_SIZE = 25
    PADDING = 40
    
    # Create window with better resolution
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pathfinding Algorithms Visualization")
    clock = pygame.time.Clock()
    
    # Create grids with spacing
    grids = [Grid(GRID_SIZE, GRID_SIZE, TILE_SIZE) for _ in range(4)]
    algorithm_names = ["Breadth-First Search", "Depth-First Search", "A* Algorithm", "Dijkstra's Algorithm"]
    algorithms = [bfs, dfs, astar, dijkstra]
    
    # Generate maze with lower wall density
    maze = generate_maze(GRID_SIZE, GRID_SIZE, wall_density=0.25)
    for grid in grids:
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                grid.set_cell(i, j, maze[i][j])
    
    # Font setup
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 48)
    
    running = True
    start_point = None
    end_point = None
    animation_speed = 30  # Controls visualization speed
    
    while running:
        screen.fill((70, 70, 70))  # Dark background
        
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
                                animation_steps = algo(maze, start_point, end_point)
                                for step in animation_steps:
                                    grid.add_to_animation(*step)
                                
                            start_point = None
                            end_point = None
        
        # Draw grids with titles and borders
        for i, grid in enumerate(grids):
            # Calculate grid position
            x_offset = (i % 2) * (WINDOW_WIDTH // 2) + PADDING
            y_offset = (i // 2) * (WINDOW_HEIGHT // 2) + PADDING
            
            # Draw border
            border_rect = pygame.Rect(
                x_offset - 5,
                y_offset - 40,
                (WINDOW_WIDTH // 2) - PADDING * 2 + 10,
                (WINDOW_HEIGHT // 2) - PADDING * 2 + 45
            )
            pygame.draw.rect(screen, (100, 100, 100), border_rect, border_radius=10)
            
            # Create and draw grid surface
            surface = pygame.Surface(((WINDOW_WIDTH // 2) - PADDING * 2, (WINDOW_HEIGHT // 2) - PADDING * 2))
            grid.draw_grid(surface)
            screen.blit(surface, (x_offset, y_offset))
            
            # Draw algorithm name
            text = title_font.render(algorithm_names[i], True, (255, 255, 255))
            screen.blit(text, (x_offset, y_offset - 35))
            
            # Animate next step
            grid.animate_step()
        
        pygame.display.flip()
        clock.tick(animation_speed)
    
    pygame.quit()

if __name__ == "__main__":
    main()