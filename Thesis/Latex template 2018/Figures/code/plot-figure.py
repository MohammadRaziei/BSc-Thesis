import matplotlib.pyplot as plt
# import pylab
import numpy as np

def reward_velocity(x,a,normal=True):
    '''
    a     : avalable
    0.75a : max at x
    0.25a : max at R
    '''
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
# plt.plot(t,y)
# plt.xlabel('$y = -a+x+\\sqrt{a^2-ax}$\n', fontsize=14, color='red')
# plt.text(15, 5, 'this is yet another test',
#         #  rotation=45,
#          horizontalalignment='center',
#          verticalalignment='top',
#         #  multialignment='center'
#          )
# plt.show()
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
