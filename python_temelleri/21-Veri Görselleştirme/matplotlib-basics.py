import matplotlib.pyplot as plt
import numpy as np

"""
x = [1,2,3,4]

y = [1,4,9,16]
plt.plot(x,y,"o--r",linewidth="2")

plt.axis([0,6,0,20])
plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel("y label")
"""


"""
x= np.linspace(0,2,100)

plt.plot(x, x, label="linear",color="blue")
plt.plot(x, x**2, label="quadratic",color="red")
plt.plot(x, x**3, label="cubic",color="black")

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("simple plot")

plt.legend()
plt.show()

"""
'''
x= np.linspace(0,2,100)
fig,axs= plt.subplots(3)

axs[0].plot(x, x,color="red")
axs[0].set_title("linear")

axs[1].plot(x, x**2,color="green")
axs[1].set_title("quadratic")  

axs[2].plot(x, x**3,color="yellow")
axs[2].set_title("cubic")
plt.tight_layout()
'''

'''
x= np.linspace(0,2,100)
fig,axs= plt.subplots(2,2)
fig.suptitle("Grafik Başlığı")

axs[0,0].plot(x, x,color="red")
axs[0,1].plot(x, x**2,color="green")
axs[1,0].plot(x, x**3,color="yellow")
axs[1,1].plot(x, x**4,color="blue")
'''

import pandas as pd

df = pd.read_csv("nba.csv")
df = df.drop(["Number"],axis=1).groupby("Team").mean()
df.head().plot(subplots=True)
plt.legend()
plt.show()
