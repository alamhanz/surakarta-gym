import pygame

from status import Chess


class SurakartaUI:
    def __init__(self, board, grid_size=80, window_size=480):  # Increased size
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
        self.screen.fill((222, 184, 135))

        # Draw grid with thicker lines, highlight first and last row/column
        for i in range(7):
            color = (0, 0, 0)
            if i == 0 or i == 5:
                color = (205, 127, 50)
            if i == 1 or i == 4:
                color = (101, 67, 33)
            if i == 2 or i == 3:
                color = (220, 204, 0)

            pygame.draw.line(
                self.screen,
                color,
                (i * self.grid_size + self.offset, self.offset),
                (i * self.grid_size + self.offset, self.window_size - self.offset),
                5,
            )
            pygame.draw.line(
                self.screen,
                color,
                (self.offset, i * self.grid_size + self.offset),
                (self.window_size - self.offset, i * self.grid_size + self.offset),
                5,
            )

        # Draw 3/4 circles in corners to connect lines
        corner_positions = [
            (self.offset, self.offset),
            (self.window_size - self.offset, self.offset),
            (self.offset, self.window_size - self.offset),
            (self.window_size - self.offset, self.window_size - self.offset),
        ]
        for pos in corner_positions:
            pygame.draw.arc(
                self.screen,
                (101, 67, 33),
                (
                    pos[0] - self.grid_size,
                    pos[1] - self.grid_size,
                    self.grid_size * 2,
                    self.grid_size * 2,
                ),
                0 * 3.14,
                1.5 * 3.14,
                5,
            )

        # Draw pieces at intersections, centered properly
        for y in range(6):
            for x in range(6):
                piece = self.board.get_chess(x, y)
                if piece == Chess.Red:
                    pygame.draw.circle(
                        self.screen,
                        (255, 0, 0),
                        (
                            x * self.grid_size + self.offset,
                            y * self.grid_size + self.offset,
                        ),
                        15,
                    )
                elif piece == Chess.Black:
                    pygame.draw.circle(
                        self.screen,
                        (0, 0, 0),
                        (
                            x * self.grid_size + self.offset,
                            y * self.grid_size + self.offset,
                        ),
                        15,
                    )
        pygame.display.flip()

    def close(self):
        pygame.quit()
