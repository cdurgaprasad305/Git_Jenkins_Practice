import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("Line Chart Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Bar Graph
categories = ["A", "B", "C"]
values = [5, 7, 3]

plt.bar(categories, values)
plt.title("Bar Chart")
plt.show()

x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

plt.scatter(x, y)
plt.title("Scatter Plot")
plt.show()


data = [1, 2, 2, 3, 3, 3, 4, 4, 5]

plt.hist(data, bins=5)
plt.title("Histogram")
plt.show()


plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig("my_plot.png")  # Saves the plot as a PNG file

