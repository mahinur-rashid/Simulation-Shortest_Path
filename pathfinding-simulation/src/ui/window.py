class Window:
    def __init__(self, width, height):
        import pygame
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pathfinding Simulation")
        self.clock = pygame.time.Clock()
        self.start_point = None
        self.end_point = None

    def get_user_input(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if self.start_point is None:
                        self.start_point = (x // 20, y // 20)  # Assuming tile size is 20
                    elif self.end_point is None:
                        self.end_point = (x // 20, y // 20)
                    else:
                        self.start_point = None
                        self.end_point = None

    def draw(self, grid):
        for row in grid:
            for cell in row:
                color = (255, 255, 255) if cell == 1 else (0, 0, 0)
                pygame.draw.rect(self.screen, color, (cell[0] * 20, cell[1] * 20, 20, 20))
        if self.start_point:
            pygame.draw.rect(self.screen, (0, 255, 0), (self.start_point[0] * 20, self.start_point[1] * 20, 20, 20))
        if self.end_point:
            pygame.draw.rect(self.screen, (255, 0, 0), (self.end_point[0] * 20, self.end_point[1] * 20, 20, 20))
        pygame.display.flip()

    def run(self, grid):
        import pygame
        pygame.init()
        while True:
            self.get_user_input()
            self.draw(grid)
            self.clock.tick(60)  # Limit to 60 frames per second

    def quit(self):
        import pygame
        pygame.quit()