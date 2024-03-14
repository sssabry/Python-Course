# importing part [pyplot] of the "matplotlib" package and nicknaming it "plt"
import matplotlib.pyplot as plt

# Sample data --> (1,2) (2,4) (3,6) (4,8) (5,10) stored in 2D lists!
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plot the data
plt.plot(x, y)

# Add labels and title -- using built in functionalities in the package
plt.xlabel('I am the X-axis')
plt.ylabel('I am the Y-axis')
plt.title('This is a Simple Plot')

# Show the plot
plt.show()

