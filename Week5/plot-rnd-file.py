import matplotlib.pyplot as plt
import os

# Get current working directory
current_dir = os.getcwd()
# Read data from file
file_path = os.path.join(current_dir, 'data.csv')

# Handling the case where the file is not available
try:
    with open(file_path, 'r') as file:
        data = file.readlines()
except FileNotFoundError:
    print("Error: data.csv file not found in the current directory.")
    exit()

# Creating lists to hold the data
x = []
y = []

# Using a for loop to iterate through the csv lines
for line in data:
    # Removing the "," from the copied in lines
    values = line.strip().split(',') 
    # Extracting the appropriate values
    x.append(int(values[0])) # first character --> index 0
    y.append(int(values[1])) # second character --> index 1

# Plot the data
plt.plot(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot from Data.csv')

# Show the plot
plt.show()
