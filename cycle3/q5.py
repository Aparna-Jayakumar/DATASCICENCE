import matplotlib.pyplot as plt
modes_of_transport = ["Walking", "Cycling", "Car", "Bus", "Train"]
frequency = [29,15,35,18,3]
plt.figure(figsize=(8, 6))
plt.bar(modes_of_transport, frequency, width=0.1, color='green')
plt.xlabel('Mode of Transport')
plt.ylabel('Frequency')
plt.title('Primary Mode of Transport to School')

# Show the bar graph
plt.show()
