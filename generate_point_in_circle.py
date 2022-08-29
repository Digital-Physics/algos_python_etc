import numpy as np
import matplotlib.pyplot as plt
import math


def point(radius: float, x_center: float, y_center: float) -> list[float]:
    """uniformly sample random points from inside a circle"""
    # we adjust the radius sampling so we choose small radii less often, proportional to the area their circle covers
    # naive sampling: rad = np.random.uniform(0, radius)
    rad = np.random.uniform(0, radius**2)**(1/2)
    angle = np.random.uniform(0, 2 * math.pi)

    x_out = math.cos(angle) * rad + x_center
    y_out = math.sin(angle) * rad + y_center

    return [x_out, y_out]


xs = []
ys = []

for i in range(1000):
    x, y = point(1, 0.5, 7)
    xs.append(x)
    ys.append(y)


plt.scatter(xs, ys)
plt.show()

