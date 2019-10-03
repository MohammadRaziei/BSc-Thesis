def _next_observation(self):
	self.render_()
	obs = np.zeros((1,36),dtype=np.float)
	car = self.agent
	theta = car['Sensors'][0]['data']['theta']
	Range = car['Sensors'][0]['data']['Range']

	for i in range(len(theta)):
		t = int((theta[i] + 180 )/10)
		r = Range[i]
		if obs[0,t] != 0:
			obs[0,t] > r
			continue
		obs[0,t] = r
	extra = [car['data']["Velocity"], car['data']["Position"]["y"]]
	self.__obs__ = np.append(obs, extra)
	return self.__obs__ 