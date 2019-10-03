def calc_reward(self):
	lanewidth = self.enviroment.road.laneWidth
	vel_sim = self.agent['data']['Velocity']
	vel_cmd = self.__action__[1]
	Vel = 0.8 * vel_sim + 0.2 * vel_cmd

	Longitudinal_reward = reward_velocity(Vel,28) *1.5
	Collision_reward = -25 if self.collision['Occurred'] else 0
	Violation_reward = -0.75 * (np.abs(self.__action__[0] - self.__action_old__[0])/lanewidth)
	Nearby_reward = nearby_reward_linear(self.__obs__[12],-2.5,1.5) +\
					nearby_reward_linear(self.__obs__[23],-2.5,1.5)
	reward_T = Longitudinal_reward + Collision_reward +\
	              Violation_reward + Nearby_reward
	return reward_T