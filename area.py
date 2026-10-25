import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import math as mt

fig, ax = plt.subplots()

circle=plt.Circle((0,0), 1,fill=False, color="red", lw=2, label=r'$x^2+y^2=1$')
ax.add_patch(circle)
ax.set_xlim(0,1.1)
ax.set_ylim(0,1.1)

y=0
n=2000
r=1
dx=dy=r/n
area=0

while y<1-dy:
    x=0
    while x<1-dx:
        x1=x+dx
        y1=y+dy
        if x1**2+y1**2<=1:
            area+=dx*dy
        x+=dx
        #Have to code for grid
    y+=dy
error=(area-(mt.pi/4))/(mt.pi/4)*100
fig.suptitle(f"Error = {error:.6f}%")
plt.show()
