# import matplotlib.pyplot as plt
# x = [-4,-3,-2,1,2,3,4,5]
# y = [16,9,4,1,4,9,16,25]
# plt.plot(x,y)
# plt.xlabel('x-axis')
# plt.ylabel('y-axis')
# plt.title('my First Graph')
# plt.show()








# import matplotlib.pyplot as plt
 
# # line 1 points
# x1 = [1,2,3]
# y1 = [2,4,1]
# # plotting the line 1 points 
# plt.plot(x1, y1, label = "line 1")
 
# # line 2 points
# x2 = [1,2,3]
# y2 = [4,1,3]
# # plotting the line 2 points 
# plt.plot(x2, y2, label = "line 2")
 
# # naming the x axis
# plt.xlabel('x - axis')
# # naming the y axis
# plt.ylabel('y - axis')
# # giving a title to my graph
# plt.title('Two lines on same graph!')
 
# # show a legend on the plot
# plt.legend()
 
# # function to show the plot
# plt.show()









# importing the required modules
import matplotlib.pyplot as plt
import numpy as np
 
# setting the x - coordinates
x = np.arange(0, 2*(np.pi), 0.1)
# setting the corresponding y - coordinates
y = np.sin(x)
 
# potting the points
plt.plot(x, y)
 
# function to show the plot
plt.show()