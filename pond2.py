import numpy as np
import matplotlib.pyplot as plt
import random



a = list(range(0, 40, 5))
a = [i/2 for i in a]
# print(a)

step_points = [(random.randint(1, 19), random.randint(1, 19)) for i in range(29)]
print(step_points)
sorted_step_points = sorted(step_points, key=lambda point: point[1])
print(sorted_step_points, "sorted_step_points")
first_stepx = sorted_step_points[0][0]
first_stepy = sorted_step_points[0][1]
first_step = sorted_step_points[0]

steps = [p for p in step_points if first_stepx - 4 < p[0] < first_stepx + 4 and p[1] > 0]
print(steps)
sorted_steps = sorted(steps, key=lambda point: point[1])
last_stepx = sorted_steps[-1][0]
print(last_stepx)

start = (first_stepx, 0)
end = (last_stepx, 20)

sorted_steps.insert(0, start)
sorted_steps.append(end)
print(sorted_steps)

current_pos = start

x_steps, y_steps = [obst[0] for obst in step_points], [obst[1] for obst in step_points]
#print(x_steps, y_steps)

sorted_steps = np.array(sorted_steps)
# plt.plot(path[:, 0], path[:, 1])
plt.plot(sorted_steps[:, 0], sorted_steps[:, 1])
# plt.plot(path)

plt.scatter(x_steps, y_steps)
# plt.plot(path[:, 1], path[:, 0])

plt.grid()
plt.show()