import pygame

from status import Chess


class SurakartaUI:
    def __init__(self, board, grid_size=50, window_size=300):
        self.board = board
        self.grid_size = grid_size
        self.window_size = window_size
        self.offset = grid_size // 2  # Center everything within the grid
        self.ui_initialized = False

    def init_ui(self):
        if not self.ui_initialized:
            pygame.init()
            self.screen = pygame.display.set_mode((self.window_size, self.window_size))
            pygame.display.set_caption("Surakarta Game")
            self.ui_initialized = True

    def render(self):
        """Renders the board using Pygame with a centered grid where pieces are placed at intersections."""
        self.init_ui()
        self.screen.fill((255, 255, 255))

        # Draw grid with thicker lines
        for i in range(7):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (i * self.grid_size + self.offset, self.offset),
                (i * self.grid_size + self.offset, self.window_size - self.offset),
                3,
            )
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (self.offset, i * self.grid_size + self.offset),
                (self.window_size - self.offset, i * self.grid_size + self.offset),
                3,
            )

        # Draw pieces at intersections, centered properly
        for y in range(6):
            for x in range(6):
                color = (200, 200, 200)
                if self.board.get_chess(x, y) == Chess.Red:
                    color = (255, 0, 0)
                elif self.board.get_chess(x, y) == Chess.Black:
                    color = (0, 0, 0)
                pygame.draw.circle(
                    self.screen,
                    color,
                    (
                        x * self.grid_size + self.offset,
                        y * self.grid_size + self.offset,
                    ),
                    10,
                )
        pygame.display.flip()

    def close(self):
        pygame.quit()
