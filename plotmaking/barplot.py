import matplotlib.pyplot as plt

#run the program: python3 barplot.py
#y and x must have the same size

# Declare Values
y = [10, 5, 3, 5, 7, 6]
x = [1, 2, 3, 4, 5, 6]

# Bar Plot
plt.rcParams["figure.figsize"] = (15,7)
plt.bar(x, y)
plt.title('Sales per Executive')
plt.xlabel('ID Number')
plt.ylabel('Weekly Sales')
plt.show()