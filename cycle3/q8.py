import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
iris_data = pd.read_csv('iris.csv')
sns.set(style="whitegrid")
pairplot = sns.pairplot(iris_data, hue="variety", markers=["o", "s", "D"], kind="reg")
plt.show()
