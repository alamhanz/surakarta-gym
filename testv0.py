import time

import gymnasium as gym

from env import SurakartaEnv

env = gym.make("Surakarta-v0", render_mode="human")  # or "ui"
obs, info = env.reset()

# action = env.action_space.sample()  # Take random actions
action = [[0, 4, 3], [5, 1, 2]]

for a in action:
    obs, reward, done, truncated, info = env.step(a)
    # print(action)
# 5,1,2 -- 5,2,3
nac = "5,1,2"
while True:
    env.render()
    action = input("what is next?")
    action = [int(i) for i in action.split(",")]

    if nac == "5,1,2":
        nac = "5,2,3"
    else:
        nac = "5,1,2"
    action0 = [int(i) for i in nac.split(",")]
    obs, reward, done, truncated, info = env.step(action)
    print(reward)
    obs, reward, done, truncated, info = env.step(action0)
    print("** -- **")


time.sleep(600)
# for _ in range(10):
#     action = env.action_space.sample()  # Take random actions
#     obs, reward, done, truncated, info = env.step(action)

#     env.render()

#     if done:
#         obs, info = env.reset()

# env.close()


# up = 1,3
# down = 2
# left = 4
# right = 8

# rightUp = 9
# rightDown = 10
# LeftUp = 5,7
# LeftDown = 6
