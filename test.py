import time

import gymnasium as gym

from env import SurakartaEnv

env = gym.make("Surakarta-v0", render_mode="ui")  # or "ui"
obs, info = env.reset()

action = env.action_space.sample()  # Take random actions
action = [0, 1, 8]
obs, reward, done, truncated, info = env.step(action)
print(action)
print(obs, reward, done, truncated, info)
# print(env.action_space)
env.render()

time.sleep(600)
# for _ in range(10):
#     action = env.action_space.sample()  # Take random actions
#     obs, reward, done, truncated, info = env.step(action)

#     env.render()

#     if done:
#         obs, info = env.reset()

# env.close()
