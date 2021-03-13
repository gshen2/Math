import matplotlib.pyplot as plt
import numpy as np

'''
r=1

t = np.linspace(0, 2*np.pi, 100)
x = r*np.cos(t)
y = r*np.sin(t)

plt.axis('equal')
plt.grid()
plt.plot(x,y)
plt.show()
'''

circle = plt.Circle((0,0), radius=1, color='lightgrey')
line = plt.Line2D((0,0), (0,1))

ax = plt.gca()
ax.add_patch(circle)
ax.add_line(line)

plt.axis('scaled')
plt.show()