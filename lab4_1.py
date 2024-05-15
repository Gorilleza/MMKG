import matplotlib.pyplot as plt
import numpy as np

# Определяем вершины исходного полигона
vertices = np.array([
    [0, 0],   # A1
    [0, 3],  # A2
    [-3, 5],  # A3
    [-5, 4],   # A4
    [-2, 2],   # A5
    [-3, 4]    # A6
])

# Определяем секущие узлы
A3_1 = np.array([-17/5, 24/5])

# Определяем новые полигоны
polygon1 = np.array([vertices[0], vertices[1], vertices[2], A3_1, vertices[0]])  # A1, A2, A3, A6_1, A1
polygon2 = np.array([vertices[3], vertices[4],  vertices[3]])               # A4, A5, A6_2, A4
polygon3 = np.array([vertices[5], A3_1, vertices[5]])                      # A6, A6_1, A6_2, A6

# Визуализация
fig, ax = plt.subplots()

# Исходный полигон
ax.plot(np.append(vertices[:, 0], vertices[0, 0]), np.append(vertices[:, 1], vertices[0, 1]), color='blue', label='Исходный полигон')

# Полигоны после разбиения
for poly, color in zip([polygon1, polygon2, polygon3], ['green', 'red', 'purple']):
    ax.fill(poly[:, 0], poly[:, 1], alpha=0.5, fc=color, ec='black')

# Секущие узлы
ax.scatter(*A3_1, color='black', zorder=5)

# Настройки отображения
ax.legend()
ax.set_aspect('equal')
plt.grid(True)
plt.show()