import matplotlib.pyplot as plt 
import numpy as np 

#pip install matplotlib 

fig, ax = plt.subplots()                                                
ax.plot([1, 1.5, 1.5, 1, 0.8, 1.5, 3.5, 4.5, 4.3, 3.5, 3.5, 4, 3.5, 2.5, 1.5, 1], [1, 3.5, 5.5, 3.5, 3.5, 6.5, 6.5, 3.5, 3.5, 5.5, 3.5, 1, 1, 3, 1, 1]) 
ax.plot([2, 2, 3, 3, 2], [6.5, 7.5, 7.5, 6.5, 6.5])
ax.plot([0, 16], [1, 1])
ax.plot([9, 9], [1, 3])
ax.plot([8.5, 9.5], [2.5, 3.5])
ax.plot([8.5, 9.5], [3.5, 2.5])
ax.plot([8.5, 9.5], [3, 3])
ax.plot([9, 9], [3, 3.5])
ax.plot([14, 14], [1, 7.5])
ax.plot([12, 16], [7, 8])
ax.plot([12, 16], [8, 7])
ax.plot([14, 14], [7.5, 8.5])
ax.plot([12, 16], [7.5, 7.5])



plt.show()                                                             
