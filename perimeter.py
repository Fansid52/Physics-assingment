import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import math as mt

fig, ax = plt.subplots()

circle=plt.Circle((0,0), 1,fill=False, color="red", lw=2, label=r'$x^2+y^2=1$')
ax.add_patch(circle)
ax.set_xlim(0,1.1)
ax.set_ylim(0,1.1)

r=1
n=1000
dx=r/n
x=0
p=0
x1=[]
y1=[]
while x<=1:
    xx=x+dx
    if x<1:
        y = mt.sqrt(max(0, 1 - (x**2)))
        x1.append(x)
        y1.append(y)
        yx=mt.sqrt(max(0, 1-(xx**2)))
        dis=mt.sqrt((xx-x)**2+(yx-y)**2)
        p+=dis
    else:
        y=mt.sqrt(1-(x**2))
        x1.append(x)
        y1.append(y)
    x=xx
error=(p-(mt.pi/2))/ (mt.pi/2)*100

ax.plot(x1,y1,lw=1 , marker="o", markeredgecolor="grey", markerfacecolor="none", markersize=6, label=r'$y=\sqrt{1-x^2}$')

fig.suptitle(f"Error = {error:.6f}%")
ax.grid(True, linestyle=':', alpha=1)
ax.legend()
plt.show()
