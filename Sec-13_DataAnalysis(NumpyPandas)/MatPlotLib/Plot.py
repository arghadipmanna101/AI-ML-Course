import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[6,5,2,65,140]
plt.plot(x,y,color='red',linestyle='--',marker='o',linewidth=5,markersize=20)
plt.grid(True)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Basic Line Plot')
plt.show()