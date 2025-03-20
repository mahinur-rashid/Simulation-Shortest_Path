import pygame
import time
from src.ui.grid import Grid
from src.utils.helpers import generate_maze
from src.algorithms.bfs import bfs
from src.algorithms.dfs import dfs
from src.algorithms.astar import astar
from src.algorithms.dijkstra import dijkstra

# Move constants to global scope
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900  # Increased height for controls
GRID_SIZE = 25
TILE_SIZE = 25
PADDING = 40

def create_button(text, font, color, bg_color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

def get_grid_position(mouse_x, mouse_y):
    # Calculate which quadrant the click is in
    quadrant_width = WINDOW_WIDTH // 2
    quadrant_height = (WINDOW_HEIGHT - 100) // 2  # Adjust for bottom controls
    
    quadrant_x = mouse_x // quadrant_width
    quadrant_y = mouse_y // quadrant_height
    
    if quadrant_y >= 2:  # Click is in the control area
        return None
        
    # Calculate relative position within the grid
    local_x = mouse_x % quadrant_width
    local_y = mouse_y % quadrant_height
    
    # Account for padding and borders
    effective_x = local_x - PADDING
    effective_y = local_y - PADDING
    
    if effective_x < 0 or effective_y < 0:
        return None
        
    grid_x = effective_y // TILE_SIZE
    grid_y = effective_x // TILE_SIZE
    
    if 0 <= grid_x < GRID_SIZE and 0 <= grid_y < GRID_SIZE:
        return (grid_x, grid_y)
    return None

def main():
    pygame.init()
    
    # Create window with better resolution
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pathfinding Algorithms Visualization")
    clock = pygame.time.Clock()
    
    # Font setup
    font = pygame.font.Font(None, 36)
    title_font = pygame.font.Font(None, 48)
    
    # Button setup
    reload_button_text, reload_button_rect = create_button("Reload Maze", font, (255, 255, 255), (100, 100, 100))
    reload_button_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50)
    
    def init_simulation():
        grids = [Grid(GRID_SIZE, GRID_SIZE, TILE_SIZE) for _ in range(4)]
        maze = generate_maze(GRID_SIZE, GRID_SIZE, wall_density=0.25)
        for grid in grids:
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    grid.set_cell(i, j, maze[i][j])
        return grids, maze
    
    grids, maze = init_simulation()
    algorithm_names = ["Breadth-First Search", "Depth-First Search", "A* Algorithm", "Dijkstra's Algorithm"]
    algorithms = [bfs, dfs, astar, dijkstra]
    
    running = True
    start_point = None
    end_point = None
    animation_speed = 60  # Increased animation speed
    
    # Status message
    status_message = "Click to set START point (marked in GREEN)"
    
    while running:
        screen.fill((50, 50, 50))  # Darker background
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                
                # Check if reload button was clicked
                if reload_button_rect.collidepoint(x, y):
                    grids, maze = init_simulation()
                    start_point = None
                    end_point = None
                    status_message = "Click to set START point (marked in GREEN)"
                    continue
                
                grid_pos = get_grid_position(x, y)
                if grid_pos:
                    grid_x, grid_y = grid_pos
                    
                    if maze[grid_x][grid_y] == 0:  # Valid cell
                        if start_point is None:
                            start_point = (grid_x, grid_y)
                            for grid in grids:
                                grid.set_cell(grid_x, grid_y, 2)  # Green for start
                            status_message = "Click to set END point (marked in RED)"
                        elif end_point is None and (grid_x, grid_y) != start_point:
                            end_point = (grid_x, grid_y)
                            for grid in grids:
                                grid.set_cell(grid_x, grid_y, 3)  # Red for end
                            status_message = "Running algorithms..."
                            
                            # Run algorithms
                            for i, (grid, algo) in enumerate(zip(grids, algorithms)):
                                animation_steps = algo(maze, start_point, end_point)
                                for step in animation_steps:
                                    grid.add_to_animation(*step)
                            
                            status_message = "Click RELOAD to start over"

        # Update hover effect
        mouse_x, mouse_y = pygame.mouse.get_pos()
        grid_pos = get_grid_position(mouse_x, mouse_y)
        
        # Draw hover indicator
        if grid_pos and not end_point:
            hover_x, hover_y = grid_pos
            if maze[hover_x][hover_y] == 0:
                for i, grid in enumerate(grids):
                    x_offset = (i % 2) * (WINDOW_WIDTH // 2) + PADDING
                    y_offset = (i // 2) * (WINDOW_HEIGHT // 2) + PADDING
                    hover_rect = pygame.Rect(
                        x_offset + hover_y * TILE_SIZE,
                        y_offset + hover_x * TILE_SIZE,
                        TILE_SIZE,
                        TILE_SIZE
                    )
                    color = (0, 255, 0) if start_point is None else (255, 0, 0)
                    pygame.draw.rect(screen, color, hover_rect, 2)

        # Draw grids with titles and borders
        for i, grid in enumerate(grids):
            x_offset = (i % 2) * (WINDOW_WIDTH // 2) + PADDING
            y_offset = (i // 2) * (WINDOW_HEIGHT // 2) + PADDING
            
            # Draw border with gradient
            border_rect = pygame.Rect(
                x_offset - 5,
                y_offset - 40,
                (WINDOW_WIDTH // 2) - PADDING * 2 + 10,
                (WINDOW_HEIGHT // 2) - PADDING * 2 + 45
            )
            pygame.draw.rect(screen, (80, 80, 80), border_rect, border_radius=10)
            pygame.draw.rect(screen, (100, 100, 100), border_rect, border_radius=10, width=2)
            
            # Draw grid
            surface = pygame.Surface(((WINDOW_WIDTH // 2) - PADDING * 2, (WINDOW_HEIGHT // 2) - PADDING * 2))
            grid.draw_grid(surface)
            screen.blit(surface, (x_offset, y_offset))
            
            # Draw algorithm name with shadow
            shadow_text = title_font.render(algorithm_names[i], True, (0, 0, 0))
            text = title_font.render(algorithm_names[i], True, (255, 255, 255))
            screen.blit(shadow_text, (x_offset + 2, y_offset - 33))
            screen.blit(text, (x_offset, y_offset - 35))
            
            # Animate next step
            grid.animate_step()
        
        # Draw reload button
        pygame.draw.rect(screen, (80, 80, 80), reload_button_rect.inflate(20, 10), border_radius=5)
        pygame.draw.rect(screen, (100, 100, 100), reload_button_rect.inflate(20, 10), border_radius=5, width=2)
        screen.blit(reload_button_text, reload_button_rect)
        
        # Draw status message
        status_text = font.render(status_message, True, (255, 255, 255))
        status_bg = pygame.Rect(0, WINDOW_HEIGHT - 130, WINDOW_WIDTH, 40)
        pygame.draw.rect(screen, (60, 60, 60), status_bg)
        status_rect = status_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 110))
        screen.blit(status_text, status_rect)
        
        pygame.display.flip()
        clock.tick(animation_speed)
    
    pygame.quit()

if __name__ == "__main__":
    main()