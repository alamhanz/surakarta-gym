import pygame

from status import Chess


class SurakartaUI:
    def __init__(
        self, board, grid_size=60, window_width=700, window_height=700
    ):  # Reduced grid size
        self.board = board
        self.grid_size = grid_size
        self.window_width = window_width
        self.window_height = window_height
        self.board_size = (
            5 * self.grid_size
        )  # Board dimensions for 6x6 grid with 6 lines
        self.offset_x = int(
            (self.window_width - self.board_size) / 2
        )  # Adjusted centering
        self.offset_y = int(
            (self.window_height - self.board_size) / 2
        )  # Adjusted centering
        self.ui_initialized = False

    def init_ui(self):
        if not self.ui_initialized:
            pygame.init()
            self.screen = pygame.display.set_mode(
                (self.window_width, self.window_height)
            )
            pygame.display.set_caption("Surakarta Game")
            self.ui_initialized = True

    def render(self):
        """Renders the board using Pygame with a centered grid where pieces are placed at intersections."""
        self.init_ui()
        self.screen.fill((222, 184, 135))
        set_width = 6
        arc_offset = 6.5
        rot_offset = 0.02
        color_line1 = (205, 127, 50)
        color_line2 = (101, 67, 33)
        color_line3 = (220, 204, 0)

        # Draw 6 grid lines instead of 7
        for i in range(6):
            color = (0, 0, 0)
            if i == 0 or i == 5:
                color = color_line1
            if i == 1 or i == 4:
                color = color_line2
            if i == 2 or i == 3:
                color = color_line3

            pygame.draw.line(
                self.screen,
                color,
                (self.offset_x + i * self.grid_size, self.offset_y),
                (self.offset_x + i * self.grid_size, self.offset_y + self.board_size),
                set_width,
            )
            pygame.draw.line(
                self.screen,
                color,
                (self.offset_x, self.offset_y + i * self.grid_size),
                (self.offset_x + self.board_size, self.offset_y + i * self.grid_size),
                set_width,
            )

        # Draw 3/4 circles in corners to connect lines
        corner_positions = [
            (self.offset_x, self.offset_y),
            (self.offset_x + self.board_size, self.offset_y),
            (self.offset_x, self.offset_y + self.board_size),
            (
                self.offset_x + self.board_size,
                self.offset_y + self.board_size,
            ),
        ]

        rotation_pair = [(0, 1.5), (1.5, 3), (0.5, 2), (1, 2.5)]

        for pos, rot in zip(corner_positions, rotation_pair):
            start_rot = rot[0] - rot_offset
            end_rot = rot[1] + rot_offset
            pygame.draw.arc(
                self.screen,
                color_line2,
                (
                    pos[0] - self.grid_size - (arc_offset // 2),
                    pos[1] - self.grid_size - (arc_offset // 2),
                    self.grid_size * 2 + arc_offset,
                    self.grid_size * 2 + arc_offset,
                ),
                start_rot * 3.14,
                end_rot * 3.14,
                set_width,
            )

            pygame.draw.arc(
                self.screen,
                color_line3,
                (
                    pos[0] - 2 * self.grid_size - (arc_offset // 2),
                    pos[1] - 2 * self.grid_size - (arc_offset // 2),
                    self.grid_size * 4 + arc_offset,
                    self.grid_size * 4 + arc_offset,
                ),
                start_rot * 3.14,
                end_rot * 3.14,
                set_width,
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
                            self.offset_x + x * self.grid_size,
                            self.offset_y + y * self.grid_size,
                        ),
                        15,
                    )
                elif piece == Chess.Black:
                    pygame.draw.circle(
                        self.screen,
                        (0, 0, 0),
                        (
                            self.offset_x + x * self.grid_size,
                            self.offset_y + y * self.grid_size,
                        ),
                        15,
                    )
        pygame.display.flip()

    def close(self):
        pygame.quit()
