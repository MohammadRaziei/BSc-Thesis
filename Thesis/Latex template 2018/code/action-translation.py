def action_translate(self,action):
	lanewidth = self.enviroment.road.laneWidth
	self.__action_old__ = self.__action__
	vel = self.agent['data']['Velocity']
	offset = self.__action__[0]

	if action == 0 :
		offset = -lanewidth
	if action == 1 :
		offset = 0 
	if action == 2 :
		offset = lanewidth
	if action == 3 :
		vel = action_velocity(vel,True)
	if action == 4 :
		vel = action_velocity(vel,False)

	self.__action__ = [offset,vel]

	return self.__action__