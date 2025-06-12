import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")
sns.lineplot(x='size',y='total_bill',data=tips)
plt.title("Line plot of total bill by size")
plt.show()