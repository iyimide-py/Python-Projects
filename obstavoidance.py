import numpy as np
import matplotlib.pyplot as plt
import random


num_obstacles = 9
start = (0, 0)
end = (5, 5)
semi_end = (4.2, 5)
avoidance_x = 1.2
avoideance_y = 0.5

# Start and end points
a = [0, 5]
b = [0, 5]
plt.scatter(a, b)

# Random obstacle generation
x = [0, 1, 2, 3, 4, 5, 1, 2, 3]
y = [0, 1, 2, 3, 4, 5, 1, 2, 3]

obstacles_x = []
obstacles_y = []

random.shuffle(x)
random.shuffle(y)
plt.scatter(x, y)

obstacles_x.append(x)
obstacles_y.append(y)
print(obstacles_x)
print(obstacles_y)

x = 0
y = 0
plt.scatter(x, y + 1)
plt.scatter(x + 1, y)

path = []
current_pos = start
while current_pos != end:
    path.append(current_pos)
    if current_pos[0] + 1 != obstacles_x[0][0] and current_pos[1] + 1 != obstacles_y[0][0]:
        current_pos = (current_pos[0] + avoidance_x, current_pos[1] + avoideance_y)
    else:
        break

path.append(semi_end)
path.append(end)
print(path)

path = np.array(path)
plt.plot(path[:, 0], path[:, 1])
plt.plot(path[:, 1], path[:, 0])

plt.grid()
plt.show()
