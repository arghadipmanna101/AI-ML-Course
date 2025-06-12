import matplotlib.pyplot as plt
labels=['A','B','C','D']
sizes=[30,20,35,15]
color=['gold','yellowgreen','lightcoral','lightskyblue']
explod=[0.2,0,0,0]

plt.pie(sizes,explode=explod,labels=labels,colors=color,autopct="%1.1f%%",shadow=True)
plt.show()