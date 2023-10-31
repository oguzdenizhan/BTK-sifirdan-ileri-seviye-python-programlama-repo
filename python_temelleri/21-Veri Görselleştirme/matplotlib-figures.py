import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(-10,9,20)
y = x**3
z = x**2
"""
figure = plt.figure()
axes_cube = figure.add_axes([0.1,0.1,0.9,0.9])

axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("X axis")
axes_cube.set_ylabel("Y axis")
axes_cube.set_title("Cube")


axes_square = figure.add_axes([0.15,0.7,0.25,0.25])

axes_square.plot(x,z,"r")
axes_square.set_xlabel("X axis")
axes_square.set_ylabel("Y axis")
axes_square.set_title("Square")

"""

"""
figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label ="square")
axes.plot(x,y,label= "cube")

plt.legend(loc=4)
"""

fig,axes= plt.subplots(nrows=2,ncols=1,figsize=(8,8))

axes[0].plot(x,y)
axes[0].set_title("Cube")

axes[1].plot(x,z)
axes[1].set_title("Square")

plt.tight_layout()
# fig.savefig("figure1.png")
fig.savefig("figure1.pdf")

plt.show()
