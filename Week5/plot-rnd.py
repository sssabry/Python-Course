import matplotlib.pyplot as plt
import random

# Generate random data
x = list(range(1, 11))  #  x-axis values from 1 to 10
y = [random.randint(1, 100) for i in range(10)]  # Randomized y-axis values

# Plot the data
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot with Random Data')

# Show the plot
plt.show()

