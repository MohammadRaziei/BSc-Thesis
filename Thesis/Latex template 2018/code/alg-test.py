model = DQN.load(save_load)
obs = env.reset()
while True:
    print('-----------TEST----------')
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()