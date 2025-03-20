import pygame

class Grid:
    def __init__(self, rows, cols, tile_size):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.start = None
        self.end = None
        self.animation_queue = []
        
        # Enhanced colors for better visualization
        self.COLORS = {
            0: (240, 240, 240),   # Empty cell (light gray)
            1: (40, 40, 40),      # Wall (dark gray)
            2: (46, 204, 113),    # Start (green)
            3: (231, 76, 60),     # End (red)
            4: (52, 152, 219),    # Path (blue)
            5: (241, 196, 15),    # Visited (yellow)
            6: (155, 89, 182)     # Currently visiting (purple)
        }

    def set_start(self, row, col):
        self.start = (row, col)
        self.grid[row][col] = 2  # Mark start point

    def set_end(self, row, col):
        self.end = (row, col)
        self.grid[row][col] = 3  # Mark end point

    def reset_grid(self):
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.start = None
        self.end = None

    def set_cell(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = value

    def add_to_animation(self, row, col, value):
        self.animation_queue.append((row, col, value))

    def animate_step(self):
        if self.animation_queue:
            row, col, value = self.animation_queue.pop(0)
            self.set_cell(row, col, value)
            return True
        return False

    def draw_grid(self, surface):
        # Draw background
        surface.fill((200, 200, 200))  # Light gray background
        
        # Draw cells with rounded corners
        for row in range(self.rows):
            for col in range (self.cols):
                color = self.COLORS[self.grid[row][col]]
                rect = pygame.Rect(
                    col * self.tile_size + 1,
                    row * self.tile_size + 1,
                    self.tile_size - 2,
                    self.tile_size - 2
                )
                pygame.draw.rect(surface, color, rect, border_radius=3)