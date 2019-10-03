import gym, gym_prescan

env_dict = {
    'id':       'prescan-without-matlabengine-v0',
    'host':     '172.21.217.140',
    'verbose':  True,
    'nget':     152
}
env = gym.make(**env_dict)

for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
env.close()