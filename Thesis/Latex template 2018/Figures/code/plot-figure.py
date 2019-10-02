import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

'''
def reward_velocity(x,a,normal=True):
    if x > a or x < 0:
        return -0.01
    R = -a + x + np.sqrt(a**2-a*x)
    if normal:
        return 4 * R / a
    return R
        
def nearby_reward_linear(x,R,W):
    return -R/W * x + R if (x > 0 and x < W) else 0
a = 20
t = np.arange(-3.0,a+3.0,0.1)
y = np.array([reward_velocity(x,a) for x in t])
plt.figure(figsize=(7, 4))
# ax = plt.subplot(121)
# ax.set_aspect(3)
l = np.arange(0.0,a,0.1)
plt.plot(t,y,l,l*4/3/a)
# plt.xlabel('this is a xlabel\n(with newlines!)')
# plt.ylabel('this is vertical\ntest', multialignment='center')
plt.text(5, 1, '$y = -a+x+\\sqrt{a^2-ax}$ : $a='+str(a)+'$',
        #  rotation=45,
        color='darkblue',
        horizontalalignment='center',
        verticalalignment='top',
        multialignment='center')

plt.text(20, 1.1, r'$y = \frac{x}{\dfrac{3}{4}a}$ : $a='+str(a)+r'$',
        #  rotation=45,
        color='orange',
        horizontalalignment='center',
        verticalalignment='top',
        multialignment='center')
# plt.grid(True)
plt.show()

'''
def action_velocity(vel,increase):
    if increase:
        return vel+5
    else:
        if vel < 5:
            return vel/2
        else:
            return vel - 2

plt.figure(figsize=(7, 4))

vel = np.arange(0,10,0.1)
y1 = np.array([action_velocity(v,True) for v in vel])
y2 = np.array([action_velocity(v,False) for v in vel])
v1 = 0 ; y1_s = np.array([])
v2 = 10; y2_s = np.array([]); y2_ss = np.array([])

while v1 <= 15:
    y1_s = np.append(y1_s, v1)
    v1 = v1 * 0.7 + 0.3 *action_velocity(v1,True)
v1 = 0; y1_ss = np.array([])
while v1 <= 15:
    y1_ss = np.append(y1_ss, v1)
    v1 = action_velocity(v1,True)

while v2 >= 0.5:
    y2_s = np.append(y2_s, v2)
    v2 = v2 * 0.7 + 0.3 *action_velocity(v2,False)
v2 = 10; y2_ss = np.array([])
while v2 >= 0.5:
    y2_ss = np.append(y2_ss, v2)
    v2 = action_velocity(v2,False)


plt.plot(vel,y1,'g', vel,y2,'b')
plt.show()

ax = plt.figure().gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.plot(np.arange(0,len(y1_ss),1),y1_ss,'ro',np.arange(0,len(y1_s),1),y1_s,'g^')
plt.show()

ax = plt.figure().gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.plot(np.arange(0,len(y2_ss),1),y2_ss,'ro',np.arange(0,len(y2_s),1),y2_s,'b^')
plt.show()