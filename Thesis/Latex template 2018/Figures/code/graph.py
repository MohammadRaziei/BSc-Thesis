import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit 


def randn(n, m=0,s =1):
    return (s*np.random.randn(n)+m).tolist()#.astype(np.int).tolist()

# plt.hist(r)
# plt.show()

# print(np.random.randint(low=25))

x = []
# x = x + randn(50,28,4)
# x = x + randn(10,40,8)
# x = x + randn(9,50,8)
# x = x + randn(9,32,5)
# x = x + randn(9,50,8)
# x = x + randn(9,32,5)
# x = x + randn(9,50,5)
# x = x + randn(5,120,20)
# x = x + randn(10,90,10)
# x = x + randn(9,50,10)
# x = x + randn(10,90,15)
# x = x + randn(10,50,15)
# x = x + randn(10,70,15)
# x = x + randn(10,70,5)
# x = x + randn(10,70,10)
# x = x + randn(10,70,5)
# x = x + randn(10,70,10)
# x = x + randn(10,70,2)
# x = x + randn(10,70,3)
# x = x + randn(10,70,1)
# x = x + randn(10,70,5)
# x = x + randn(2,70,10)
# x = x + randn(10,70,3)
# x = x + randn(10,70,1)
# x = x + randn(10,70,2)
# x = x + randn(10,70,5)
# x = x + randn(10,70,3)
# x = x + randn(10,70,3)
# x = x + randn(10,70,3)
# x = x + randn(10,70,3)
# x = x + randn(10,69,5)
# x = x + randn(10,70,2)
# x = x + randn(10,70,2)
# x = x + randn(10,70,2)
# x = x + randn(10,70,2)
# x = x + randn(10,70,1)
# x = x + randn(10,70,1)
# x = x + randn(10,70,1)
# x = x + randn(10,70,1)
# x = x + randn(10,70,0.5)
# x = x + randn(10,70,0.2)
# x = x + randn(10,70,0.2)
# x = x + randn(10,70,0.2)



# def between(x,x1,y1,x2,y2):
#     return (y2-y1)(x-x1) + y1

# def dist(map_list):
#     map_list = map_list / sum(map_list)
#     r = np.random.randint(0,len(map_list))
#     cum = np.cumsum(map_list)


def rand(n,a,b):
    return (a + (b-a) * np.random.rand(n) ).tolist()





x = x + randn(30,-1.32,0.12)
x = x + randn(10,-1,0.2)
x = x + randn(10,-1.2,0.1)
x = x + randn(20,-0.8,0.2)
x = x + randn(10,-0.5,0.1)
x = x + randn(3,-1,0.15)
x = x + randn(9,-1.4,0.1)
x = x + randn(3,-1,0.1)
x = x + randn(9,-0.3,0.15)
x = x + randn(2,-0.8,0.1)
x = x + randn(9,-1.2,0.1)
x = x + randn(2,-0.8,0.1)
x = x + randn(9,-0.4,0.15)
x = x + randn(9,-0.2,0.1)
x = x + randn(9,-0,0.08)
x = x + randn(9,0.15,0.08)
x = x + randn(9,0.2,0.08)
x = x + randn(9,-0.15,0.08)
x = x + randn(9,0.15,0.08)
x = x + randn(9,0.4,0.1)
x = x + randn(9,-0.15,0.08)
x = x + randn(9,0.15,0.08)
x = x + randn(9,0.4,0.1)
x = x + randn(9,-0.05,0.08)
x = x + randn(9,0.2,0.08)
x = x + randn(9,0.4,0.1)
x = x + randn(9,0.7,0.1)
x = x + randn(9,0.8,0.08)
x = x + randn(9,0.9,0.08)
x = x + randn(9,0.95,0.08)
x = x + randn(9,1,0.08)
x = x + randn(9,1.1,0.08)

x = x + randn(9,1.1,0.08)
x = x + randn(9,1.2,0.08)
x = x + randn(9,1.18,0.08)
x = x + randn(9,1.2,0.08)
x = x + randn(9,1.15,0.05)
x = x + randn(9,1.2,0.05)
x = x + randn(9,1.18,0.05)
x = x + randn(9,1.22,0.05)
x = x + randn(9,1.28,0.02)
x = x + randn(9,1.3,0.02)
x = x + randn(9,1.31,0.02)
x = x + randn(9,1.32,0.01)
x = x + randn(9,1.32,0.02)
x = x + randn(9,1.325,0.01)
x = x + randn(9,1.325,0.02)
x = x + randn(9,1.328,0.01)
x = x + randn(9,1.33,0.02)
x = x + randn(9,1.335,0.02)
x = x + randn(9,1.338,0.01)
x = x + randn(9,1.339,0.008)
x = x + randn(9,1.339,0.008)
 












# x = x + randn()
# x = x + randn()
# x = x + randn()
# x = x + randn()
# x = x + randn()
# x = x + randn()
# x = x + randn()
# x = x + randn()
# x = x + randn()
# x = x + randn()
# x = x + randn()
# x = x + randn()
# x = x + randn()
# x = x + randn()
# x = x + randn()


# x = x + randn(9,-5,1)#
# x = x + randn(3,-3,0.5)#
# x = x + rand(9,0,-2)
# x = x + randn(3,-0.5,0.5)#
# x = x + rand(9,-1,0)
# x = x + rand(5,1.2,-1)
# x = x + rand(10,-8,-13)
# x = x + randn(3,-0.1,0.5)
# x = x + randn(3,-0.5,0.5)
# x = x + randn(3,-3,0.5)
# x = x + randn(3,0.1,0.5)
# x = x + randn(5,-5,1)#




# x = x + rand(10,90,10)
# x = x + rand(9,50,10)
# x = x + rand(10,90,15)
# x = x + rand(10,50,15)
# x = x + rand(10,70,15)
# x = x + rand(10,70,5)
# x = x + rand(10,70,10)
# x = x + rand(10,70,5)
# x = x + rand(10,70,10)
# x = x + rand(10,70,2)
# x = x + rand(10,70,3)
# x = x + rand(10,70,1)
# x = x + rand(10,70,5)
# x = x + rand(2,70,10)
# x = x + rand(10,70,3)
# x = x + rand(10,70,1)
# x = x + rand(10,70,2)
# x = x + rand(10,70,5)
# x = x + rand(10,70,3)
# x = x + rand(10,70,3)
# x = x + rand(10,70,3)
# x = x + rand(10,70,3)
# x = x + rand(10,69,5)
# x = x + rand(10,70,2)
# x = x + rand(10,70,2)
# x = x + rand(10,70,2)
# x = x + rand(10,70,2)
# x = x + rand(10,70,1)
# x = x + rand(10,70,1)
# x = x + rand(10,70,1)
# x = x + rand(10,70,1)
# x = x + rand(10,70,0.5)
# x = x + rand(10,70,0.2)
# x = x + rand(10,70,0.2)
# x = x + rand(10,70,0.2)










# x = rand(1000,-12,12)

# plt.hist(x)
# plt.show()
plt.plot(np.arange(0,len(x)),x)
plt.show()





