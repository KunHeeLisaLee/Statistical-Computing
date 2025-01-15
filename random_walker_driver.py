import matplotlib.pyplot as plt
from random_walker_module import RandomWalker, ModifiedRandomWalker

"""for part b)"""
# Instantiate RandomWalker objects
rw0 = RandomWalker()
rw1 = RandomWalker()
rw2 = RandomWalker()
rw3 = RandomWalker()

# Lists storing coordinates of RandomWalker objects
x0, y0 = [rw0.get_x_pos()], [rw0.get_y_pos()]
x1, y1 = [rw1.get_x_pos()], [rw1.get_y_pos()]
x2, y2 = [rw2.get_x_pos()], [rw2.get_y_pos()]
x3, y3 = [rw3.get_x_pos()], [rw3.get_y_pos()]

# Evolve RandomWalker objects 1,000 steps in time
for _ in range(1000):
    rw0.step()
    rw1.step()
    rw2.step()
    rw3.step()

    """Append coordinates"""
    x0.append(rw0.get_x_pos())
    y0.append(rw0.get_y_pos())
    x1.append(rw1.get_x_pos())
    y1.append(rw1.get_y_pos())
    x2.append(rw2.get_x_pos())
    y2.append(rw2.get_y_pos())
    x3.append(rw3.get_x_pos())
    y3.append(rw3.get_y_pos())

# Plot trajectories
plt.figure(figsize=(10, 8))
plt.plot(x0, y0, label='RandomWalker 1')
plt.plot(x1, y1, label='RandomWalker 2')
plt.plot(x2, y2, label='RandomWalker 3')
plt.plot(x3, y3, label='RandomWalker 4')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('RandomWalker Trajectories')
plt.legend()
plt.show()

"""for part d)"""
# Instantiate RandomWalker objects
rw0 = RandomWalker()
rw1 = RandomWalker()
rw2 = RandomWalker()
rw3 = ModifiedRandomWalker()

# Lists storing coordinates of RandomWalker objects
x0, y0 = [rw0.get_x_pos()], [rw0.get_y_pos()]
x1, y1 = [rw1.get_x_pos()], [rw1.get_y_pos()]
x2, y2 = [rw2.get_x_pos()], [rw2.get_y_pos()]
x3, y3 = [rw3.get_x_pos()], [rw3.get_y_pos()]

# Evolve RandomWalker objects 1,000 steps in time
for _ in range(1000):
    rw0.step()
    rw1.step()
    rw2.step()
    rw3.step([rw0, rw1, rw2])  # take previous objects and decide

    """Append coordinates"""
    x0.append(rw0.get_x_pos())
    y0.append(rw0.get_y_pos())
    x1.append(rw1.get_x_pos())
    y1.append(rw1.get_y_pos())
    x2.append(rw2.get_x_pos())
    y2.append(rw2.get_y_pos())
    x3.append(rw3.get_x_pos())
    y3.append(rw3.get_y_pos())

# Plot trajectories
plt.figure(figsize=(10, 8))
plt.plot(x0, y0, label='RandomWalker 1')
plt.plot(x1, y1, label='RandomWalker 2')
plt.plot(x2, y2, label='RandomWalker 3')
plt.plot(x3, y3, label='ModifiedRandomWalker', linestyle='--')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('RandomWalker Trajectories')
plt.legend()
plt.show()
