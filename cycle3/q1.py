import matplotlib.pyplot as plt
year=[2001,2002,2003,2004,2005,2006,2007]
car_value=[24000,22500,19700,17500,14500,10000,5800]
plt.figure(figsize=(8,4))
plt.subplot(1,1,1)
plt.plot(year,car_value,color='red',linestyle='-.',label='Car Value')
plt.scatter(year,car_value,color='green',marker='*',s=20,label='Data Point')
plt.xlabel('Year')
plt.ylabel('Car Value')
plt.title('Value Depreciation', loc='left')
plt.legend()
plt.show()