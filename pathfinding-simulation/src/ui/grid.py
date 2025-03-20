import pygame

class Grid:
    def __init__(self, rows, cols, tile_size):
        self.rows = rows
        self.cols = cols
        self.tile_size = tile_size
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]
        self.start = None
        self.end = None
        
        # Define colors
        self.COLORS = {
            0: (255, 255, 255),  # Empty cell (white)
            1: (0, 0, 0),        # Wall (black)
            2: (0, 255, 0),      # Start (green)
            3: (255, 0, 0),      # End (red)
            4: (0, 0, 255),      # Path (blue)
            5: (255, 255, 0)     # Visited (yellow)
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

    def draw_grid(self, surface):
        surface.fill((128, 128, 128))  # Gray background
        for row in range(self.rows):
            for col in range(self.cols):
                color = self.COLORS[self.grid[row][col]]
                pygame.draw.rect(surface, color, 
                               (col * self.tile_size, row * self.tile_size, 
                                self.tile_size - 1, self.tile_size - 1))

    def update_path(self, path, visited=None):
        if visited:
            for pos in visited:
                if pos != self.start and pos != self.end:
                    self.set_cell(pos[0], pos[1], 5)
        if path:
            for pos in path:
                if pos != self.start and pos != self.end:
                    self.set_cell(pos[0], pos[1], 4)