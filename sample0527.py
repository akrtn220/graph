#定常状態
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

pi=np.pi

x=np.linspace(0,1,1000)
y=np.linspace(0,1,10)
X, Y = np.meshgrid(x, y)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.xlabel('x')
plt.ylabel('y')
ax.set_zlabel("u(x,y)")


def sigma1(n):
    ans=0
    for k in range(1,n+1):
        ans += ((np.power(-1,k)-1)/(k*np.sinh(k*pi)))*np.sinh(k*pi*(X-1))*np.sin(k*pi*Y)
    return ans

Z=sigma1(100)*(20/pi)

ax.scatter3D(np.ravel(X),np.ravel(Y),np.ravel(Z))
ax.invert_yaxis()
plt.show()