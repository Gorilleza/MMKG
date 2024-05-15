import matplotlib.pyplot as plt
import numpy as np

def inside(polygon, x, y):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n+1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def clip_line(polygon, x1, y1, x2, y2):
    if inside(polygon, x1, y1) and inside(polygon, x2, y2):
        return x1, y1, x2, y2
    elif inside(polygon, x1, y1) and not inside(polygon, x2, y2):
        x, y = line_intersection(polygon, x1, y1, x2, y2)
        return x1, y1, x, y
    elif not inside(polygon, x1, y1) and inside(polygon, x2, y2):
        x, y = line_intersection(polygon, x1, y1, x2, y2)
        return x, y, x2, y2
    else:
        return None

def line_intersection(polygon, x1, y1, x2, y2):
    n = len(polygon)
    intersections = []
    for i in range(n):
        x3, y3 = polygon[i]
        x4, y4 = polygon[(i+1) % n]
        den = (x1-x2)*(y3-y4) - (y1-y2)*(x3-x4)
        if den != 0:
            t = ((x1-x3)*(y3-y4) - (y1-y3)*(x3-x4)) / den
            u = -((x1-x2)*(y1-y3) - (y1-y2)*(x1-x3)) / den
            if 0 <= t <= 1 and 0 <= u <= 1:
                x = x1 + t*(x2-x1)
                y = y1 + t*(y2-y1)
                intersections.append((x, y))
    return intersections[0] if intersections else None

# Координаты точек
A = (-2, -1)
B = (3, 1)
C1 = (0, 0)
C2 = (1, 0)
C3 = (2, 1)
C4 = (1, 2)
C5 = (0, 1)

# Координаты отрезка для отсечения
P1 = (1/2, 0)
P2 = (4/3, 1/3)

# Построение полигона и отрезка
polygon = [C1, C2, C3, C4, C5, C1]
x_polygon, y_polygon = zip(*polygon)
plt.plot(x_polygon, y_polygon, 'black')
plt.plot([A[0], B[0]], [A[1], B[1]], 'black')
plt.plot([P1[0], P2[0]], [P1[1], P2[1]], 'black')
plt.scatter(*zip(P1, P2), color='b')

# Выполнение отсечения
result = clip_line(polygon, P1[0], P1[1], P2[0], P2[1])
if result:
    x1, y1, x2, y2 = result
    plt.plot([x1, x2], [y1, y2], 'black')

# Настройка графика
plt.xlim(-3, 4)
plt.ylim(-2, 3)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Отсечение отрезка')
plt.grid(True)

# Вывод графика
plt.show()
