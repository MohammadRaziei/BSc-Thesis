import gym, gym_prescan

from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines import DQN

save_load = "deepq_prescan"
env_dict = {
    'id':       'prescan-without-matlabengine-v0',
    'verbose':  True,
    'host':     '172.21.217.140',
    # 'delay':    1,
    'nget':       150 
}

env = gym.make(**env_dict)
env = DummyVecEnv([lambda: env])
model = DQN(MlpPolicy, env, verbose=1, gamma=0.8, prioritized_replay=True)
print('Model created!')
try:
    model.learn(total_timesteps=50000)
except:
    print('Error!')
model.save(save_load)