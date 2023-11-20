import seaborn as sns
import matplotlib.pyplot as plt
iris_data = sns.load_dataset("iris")
sns.histplot(data=iris_data, x="petal_length", bins=10, kde=True)
plt.show()
