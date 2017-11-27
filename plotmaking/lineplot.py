import matplotlib.pyplot as plt

#run the program: python3 lineplot.py
#y, x1 and x2 must have the same size

y = [1,4,9,16,25,36,49,64,81,100]
x1 = [5,10,15,20,25,30,35,40,45,47]
x2 = [1,1,2,3,5,8,13,21,34,53]

plt.rcParams["figure.figsize"] = (15,7)
plt.plot(y,x1, marker='+', linestyle='--', color='b',label='Blue Shift')
plt.plot(y,x2, marker='o', linestyle='-', color='r', label='Red Shift')
plt.xlabel('Days to Election')
plt.ylabel('Popularity')
plt.title('Candidate Popularity')
plt.legend(loc='lower right')

plt.show()