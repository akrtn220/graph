import matplotlib.pyplot as plt
import numpy as np 

pi=np.pi
e=np.e

x=np.linspace(0,1,1000)

def add(n,t):
    ans=0
    for i in range(1,n+1):
        ans += np.cos(i*pi/2)*np.cos(i*pi*x)*np.power(e,-i*i*pi*pi*t)
    return ans

def sigma(n,t):
    ans=0
    for i in range(1,n+1):
        ans += (1/i)*(1-np.cos(i*pi/2))*np.sin(i*pi*x)*np.power(e,-i*i*pi*pi*t)
    return ans
y1=1+(2*add(60,0.001))
y4=1+(2*add(60,0.128))
y2=1+(2*add(60,0.002))
y3=1+(2*add(60,0.004))
plt.plot(x,y1,label="0.001")
plt.plot(x,y2,label="0.002")
plt.plot(x,y3,label="0.004")
plt.plot(x,y4,label="0.128")

# y1=(20/pi)*sigma(60,0.001)
# plt.plot(x,y1)
# y2=(20/pi)*sigma(60,0.002)
# plt.plot(x,y2)
# y6=(20/pi)*sigma(60,0.004)
# plt.plot(x,y6)

# y8=(20/pi)*sigma(60,0.128)
# plt.plot(x,y8)

# for i in range(1,256):
#     y1=(20/pi)*sigma(60,i*0.001)
#     plt.plot(x,y1)

plt.legend()   
plt.show()