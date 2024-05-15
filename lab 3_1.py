import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Углы поворота
alpha = -np.arccos(1/8)
beta = -np.pi + np.arccos(np.sqrt(7)/4)
gamma = 0

# Матрица поворота
rotation_matrix = np.array([
   [np.cos(beta)*np.cos(gamma),
    np.cos(alpha)*np.sin(gamma) + np.sin(alpha)*np.sin(beta)*np.cos(gamma),
    np.sin(alpha)*np.sin(gamma) - np.cos(alpha)*np.sin(beta)*np.cos(gamma)],
   [-np.cos(beta)*np.sin(gamma),
    np.cos(alpha)*np.cos(gamma) - np.sin(alpha)*np.sin(beta)*np.sin(gamma),
    np.sin(alpha)*np.cos(gamma) + np.cos(alpha)*np.sin(beta)*np.sin(gamma)],
   [np.sin(beta), -np.sin(alpha)*np.cos(beta), np.cos(alpha)*np.cos(beta)]
])

# Векторы осей
axis_vectors = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

# Поворот векторов осей
rotated_axes = np.dot(rotation_matrix, axis_vectors.T).T

# Вершины тетраэдра
tetrahedron_vertices = np.array([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]])

# Поворот вершин тетраэдра
rotated_tetrahedron = np.dot(rotation_matrix, tetrahedron_vertices.T).T

# Визуализация
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Отображение осей
ax.quiver(0, 0, 0, rotated_axes[:, 0], rotated_axes[:, 1], rotated_axes[:, 2], color='r')
ax.text(rotated_axes[0, 0], rotated_axes[0, 1], rotated_axes[0, 2], 'x')
ax.text(rotated_axes[1, 0], rotated_axes[1, 1], rotated_axes[1, 2], 'y')
ax.text(rotated_axes[2, 0], rotated_axes[2, 1], rotated_axes[2, 2], 'z')

# Отображение тетраэдра
ax.plot([rotated_tetrahedron[0, 0], rotated_tetrahedron[1, 0]],
        [rotated_tetrahedron[0, 1], rotated_tetrahedron[1, 1]],
        [rotated_tetrahedron[0, 2], rotated_tetrahedron[1, 2]], 'b-')
ax.plot([rotated_tetrahedron[0, 0], rotated_tetrahedron[2, 0]],
        [rotated_tetrahedron[0, 1], rotated_tetrahedron[2, 1]],
        [rotated_tetrahedron[0, 2], rotated_tetrahedron[2, 2]], 'b-')
ax.plot([rotated_tetrahedron[0, 0], rotated_tetrahedron[3, 0]],
        [rotated_tetrahedron[0, 1], rotated_tetrahedron[3, 1]],
        [rotated_tetrahedron[0, 2], rotated_tetrahedron[3, 2]], 'b-')
ax.plot([rotated_tetrahedron[1, 0], rotated_tetrahedron[2, 0]],
        [rotated_tetrahedron[1, 1], rotated_tetrahedron[2, 1]],
        [rotated_tetrahedron[1, 2], rotated_tetrahedron[2, 2]], 'b-')
ax.plot([rotated_tetrahedron[1, 0], rotated_tetrahedron[3, 0]],
        [rotated_tetrahedron[1, 1], rotated_tetrahedron[3, 1]],
        [rotated_tetrahedron[1, 2], rotated_tetrahedron[3, 2]], 'b-')
ax.plot([rotated_tetrahedron[2, 0], rotated_tetrahedron[3, 0]],
        [rotated_tetrahedron[2, 1], rotated_tetrahedron[3, 1]],
        [rotated_tetrahedron[2, 2], rotated_tetrahedron[3, 2]], 'b-')

# Настройка осей
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Отображение графика
plt.show()
