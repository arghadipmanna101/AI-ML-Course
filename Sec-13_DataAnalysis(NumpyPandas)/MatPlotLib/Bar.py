import matplotlib.pyplot as plt
categories=['A','B','C','D','E']
values=[5,4,2,6,9]

plt.bar(categories,values,color='purple')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')
plt.show()