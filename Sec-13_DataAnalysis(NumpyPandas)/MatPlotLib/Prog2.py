import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=[1,4,9,16,25]
y2=[1,2,3,4,5]

plt.figure(figsize=(9,5))

plt.subplot(1,2,1)
plt.plot(x,y1,color='green')
plt.title("Plot 1")

plt.subplot(1,2,2)
plt.plot(x,y2,color='green')
plt.title("Plot 2")


plt.subplot(2,2,3)
plt.plot(y1,y2,color='green')
plt.title("Plot 3")
plt.show()