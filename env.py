import gymnasium as gym
import numpy as np
from gymnasium import spaces
from gymnasium.envs.registration import register

from board import Action, Board
from interface import SurakartaUI
from status import Chess, Direction, GameStatus


class SurakartaEnv(gym.Env):
    """
    OpenAI Gymnasium environment for the Surakarta game.
    """

    metadata = {"render_modes": ["human", "ui"]}

    def __init__(self, render_mode=None):
        super(SurakartaEnv, self).__init__()
        self.board = Board()
        self.render_mode = render_mode  # Store the render mode
        self.ui = SurakartaUI(self.board) if render_mode == "ui" else None

        # Action space: (piece_x, piece_y, move_direction)
        self.action_space = spaces.MultiDiscrete(
            [6, 6, 8, 2]
        )  # 6x6 board, 8 possible directions

        # Observation space represents the board state
        self.observation_space = spaces.Box(low=0, high=2, shape=(6, 6), dtype=np.int8)

    def reset(self, seed=None, options=None):
        """Resets the game and returns the initial state."""
        super().reset(seed=seed)
        self.board.new_game()
        return self._get_observation(), {}

    def step(self, action):
        """Executes the given action and returns the next state, reward, done, and info."""
        x, y, direction, eat = action  # Extract piece location and move direction
        reward, done = 0, False

        # Check if there is a piece at the selected coordinates
        piece = self.board.get_chess(x, y)
        if piece == Chess.Null:
            reward = -5  # Penalize selecting an empty space
        elif self.board.can_move(x, y, direction):
            # TODO: must add player eat as well if possible
            self.board.player_move(x, y, direction)
            reward = 1  # Reward for a successful move
        else:
            reward = -1  # Penalize invalid moves

        if self.board.status == GameStatus.RedWon:
            reward = 10
            done = True
        elif self.board.status == GameStatus.BlackWon:
            reward = -10
            done = True

        print(self.board.get_can_eat(x, y))

        return self._get_observation(), reward, done, False, {}

    def render(self):
        """Displays the board state in different modes."""
        if self.render_mode == "human":
            print(self.board)
        elif self.render_mode == "ui" and self.ui:
            self.ui.render()

    def close(self):
        if self.ui:
            self.ui.close()

    def _get_observation(self):
        """Returns the board as a numerical observation."""
        obs = np.zeros((6, 6), dtype=np.int8)
        for y in range(6):
            for x in range(6):
                obs[y, x] = self.board.get_chess(x, y)
        return obs


# Automatically register the environment when this module is imported
register(
    id="Surakarta-v0",
    entry_point="env:SurakartaEnv",
    max_episode_steps=100,  # Set the max steps per episode (adjustable)
)

# Ensure the script runs correctly when executed
if __name__ == "__main__":
    env = gym.make("Surakarta-v0", render_mode="human")
    obs, info = env.reset()

    for _ in range(10):
        action = (
            env.action_space.sample()
        )  # Randomly select (piece_x, piece_y, move_direction)
        obs, reward, done, truncated, info = env.step(action)
        env.render()

        if done:
            obs, info = env.reset()

    env.close()
