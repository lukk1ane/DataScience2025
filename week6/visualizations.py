import matplotlib.pyplot as plt
import numpy as np

#Task 1
#Plot temperature changes over a week and label the axes, title, and gridlines
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [12,14,15,11,13,16,18]

plt.figure(figsize = (8,5))

plt.plot(days, temperatures, marker = 'o')
plt.xlabel("Day of the week")
plt.ylabel("Temperature")
plt.title("Temperature changes over a week")

plt.grid(True)
plt.show()

'''
Task2
Plot daily sales for two products over a month and compare them
in one graph
'''
days = np.arange(1, 31)  # Days 1 to 30

product_A_sales = [10, 12, 11, 15, 14, 13, 16, 18, 17, 19,
                   20, 21, 19, 18, 17, 20, 22, 23, 25, 24,
                   26, 28, 27, 29, 30, 31, 32, 33, 35, 34]

product_B_sales = [8, 9, 10, 11, 12, 11, 13, 14, 12, 15,
                   16, 15, 14, 16, 17, 18, 17, 19, 20, 22,
                   21, 20, 23, 24, 25, 26, 27, 28, 30, 29]

plt.figure(figsize=(10, 5))

plt.plot(days, product_A_sales, marker="o", label="Product A")
plt.plot(days, product_B_sales, marker="s", label="Product B")

plt.xlabel("Day of the Month")
plt.ylabel("Sales")
plt.title("Daily Sales Comparison of Two Products Over a Month")

plt.grid(True)

plt.legend()

plt.show()

'''
Task3
Create a scatter plot showing the relationship between three
variables using color or size
'''
x = np.random.rand(50) * 100
y = np.random.rand(50) * 50
z = np.random.rand(50) * 200

plt.figure(figsize=(8, 5))

scatter = plt.scatter(x, y, c=z, cmap='viridis')

plt.xlabel("Variable X")
plt.ylabel("Variable Y")
plt.title("Scatter Plot Showing Relationship Between Three Variables (Color Represents Z)")

plt.colorbar(scatter, label="Variable Z Value")
plt.grid(True)

plt.show()

'''
Task4
Visualize average monthly revenue for three stores with grouped
bar charts
'''
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

store1 = [30, 45, 50, 60, 70, 65]
store2 = [40, 55, 45, 65, 75, 80]
store3 = [35, 50, 60, 55, 85, 90]


plt.figure(figsize=(10, 5))

x = np.arange(len(months))
width = 0.25

plt.bar(x - width, store1, width, label="Store 1")
plt.bar(x,         store2, width, label="Store 2")
plt.bar(x + width, store3, width, label="Store 3")


plt.xlabel("Month")
plt.ylabel("Average Monthly Revenue")
plt.title("Average Monthly Revenue of Three Stores (Grouped Bar Chart)")


plt.xticks(x, months)

plt.legend()
plt.grid(axis='y')

plt.show()

'''
Task5
Plot histograms comparing two different distributions on the same
figure
'''
data1 = np.random.normal(50, 10, 500)
data2 = np.random.normal(60, 15, 500)

plt.figure(figsize=(8, 5))

plt.hist(data1, bins=20, alpha=0.6, label="Distribution 1")
plt.hist(data2, bins=20, alpha=0.6, label="Distribution 2")

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histograms Comparing Two Distributions")
plt.legend()

plt.show()
'''
Task6 
Display customer segment percentages in a pie chart with one
segment highlighted
'''
labels = ["Segment A", "Segment B", "Segment C", "Segment D"]
sizes = [40, 25, 20, 15]
explode = [0.1, 0, 0, 0]

plt.figure(figsize=(7, 7))

plt.pie(sizes, labels=labels, explode=explode, autopct="%1.1f%%", shadow=True)
plt.title("Customer Segment Percentages")

plt.show()

'''
Task7
Create a 2x2 layout of subplots showing a line plot, bar chart,
histogram, and scatter plot
'''
x = np.arange(1, 11)
y = x**2
bar_values = [5, 7, 3, 8, 6, 9, 2, 4, 7, 5]
hist_data = np.random.normal(50, 10, 100)
scatter_x = np.random.rand(50) * 10
scatter_y = np.random.rand(50) * 100

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y)
axs[0, 0].set_title("Line Plot")

axs[0, 1].bar(x, bar_values, color="orange")
axs[0, 1].set_title("Bar Chart")

axs[1, 0].hist(hist_data, bins=15, color="green", alpha=0.7)
axs[1, 0].set_title("Histogram")

axs[1, 1].scatter(scatter_x, scatter_y, color="red")
axs[1, 1].set_title("Scatter Plot")

for ax in axs.flat:
    ax.grid(True)

plt.tight_layout()
plt.show()
'''
Task8
Plot a customized line chart and highlight key data points with
annotations
'''
x = np.arange(1, 11)
y = [5, 7, 6, 8, 10, 9, 12, 11, 13, 15]

plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', linestyle='--', color='purple')

plt.xlabel("Day")
plt.ylabel("Sales")
plt.title("Customized Line Chart with Key Points Highlighted")
plt.grid(True)

key_points = {5:10, 10:15}
for xp, yp in key_points.items():
    plt.annotate(f"({xp},{yp})", xy=(xp, yp), xytext=(xp+0.2, yp+0.5),
                 arrowprops=dict(facecolor='black', arrowstyle='->'))

plt.show()

'''
Task9
Visualize a 10x10 matrix as a heatmap with color variations
representing values
'''
matrix = np.random.randint(1, 101, size=(10, 10))

plt.figure(figsize=(8, 6))
plt.imshow(matrix, cmap='viridis', interpolation='nearest')
plt.colorbar(label="Value")
plt.title("Heatmap of 10x10 Matrix")
plt.show()

'''
Task10
Build a mini visualization report combining three different
chart types with titles and legends
'''

x = np.arange(1, 11)
line_y = [5, 7, 6, 8, 10, 9, 12, 11, 13, 15]
bar_y = [3, 5, 2, 6, 4, 7, 5, 6, 4, 5]
scatter_x = np.random.rand(10) * 10
scatter_y = np.random.rand(10) * 15

plt.figure(figsize=(10, 6))

plt.plot(x, line_y, marker='o', linestyle='-', color='blue', label='Line Chart')
plt.bar(x, bar_y, alpha=0.6, color='orange', label='Bar Chart')
plt.scatter(scatter_x, scatter_y, color='red', label='Scatter Plot')

plt.xlabel("X-axis")
plt.ylabel("Values")
plt.title("Mini Visualization Report Combining Three Chart Types")
plt.legend()
plt.grid(True)

plt.show()