import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import Delaunay

# Заданные точки
points = np.array([[-10, 1], [-10, 10], [-2, 0], [-2, 9], [10, 8]])

# Построение триангуляции Делоне
tri = Delaunay(points)

# Визуализация точек
plt.scatter(points[:,0], points[:,1], color='red')

# Отрисовка триангулированных треугольников
for indices in tri.simplices:
    plt.plot(points[indices,0], points[indices,1], 'b-')

plt.gca().set_aspect('equal', adjustable='box')
plt.show()