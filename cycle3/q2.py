import matplotlib.pyplot as plt
days = ['mon' ,'tues' ,'wed','thur','fri']
drink= [300,450,150,400,650]
food= [400,500,350,300,500]
plt.figure(figsize=(8,8))
plt.subplot(2,1,1)
plt.plot(days,drink,linestyle='dotted',color='blue',label='sales data1',marker='H',markersize=8,markerfacecolor='red',markeredgecolor='black')
plt.xlabel('day of week')
plt.ylabel('drink sale')
plt.title('sales data1',loc='right')
plt.grid(color='green',linestyle='--')
plt.legend()
plt.subplot(2,1,2)
plt.plot(days, food, linestyle='--', color='purple', label='Sales Data2', marker='D', markersize=8,markerfacecolor='green', markeredgecolor='red')
plt.xlabel('Days of the Week')
plt.ylabel('Sale of Food')
plt.title('Sales Data2', loc='center')
plt.grid(color='Teal', linestyle='--')
plt.legend()
plt.tight_layout()
plt.show()