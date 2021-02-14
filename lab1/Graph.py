import matplotlib.pyplot as plt
import numpy as np

# 100 linearly spaced numbers
x = np.linspace(-2,2,100)
e = 2.718281828459045
# the functions
y = x*e**x + x**2 - 1
y1 = 1 - x**2
y2 = x*e**x
# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the function
plt.plot(x,y1, 'r', label='y=x*e^x')
plt.plot(x,y2, 'b', label='y=1-x^2')
plt.legend(loc='upper left')

# show the plot
plt.show()