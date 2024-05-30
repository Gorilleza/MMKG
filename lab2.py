import numpy as np

# Определение принадлежности точки полигону
def point_in_polygon(point, polygon):
    x, y = point
    inside = False
    
    for i in range(len(polygon)):
        j = (i + 1) % len(polygon)
        xi, yi = polygon[i]
        xj, yj = polygon[j]
        
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
    
    return inside

# Пример использования
polygon = [(2, 1), (4, 7), (8, 0), (4, -5)]
points = [(2, 1), (4, 7), (8, 0), (4, -5), (4, 1)]

for point in points:
    if point_in_polygon(point, polygon):
        print(f"Точка {point} лежит внутри полигона.")
    else:
        print(f"Точка {point} лежит снаружи полигона.")

# Линейные преобразования, матрицы линейных преобразований
def transform_point(point, matrix):
    """
    Применяет линейное преобразование, заданное матрицей, к точке.
    
    Аргументы:
    point - кортеж (x, y), координаты точки
    matrix - numpy-массив 2x2, матрица линейного преобразования
    
    Возвращает:
    кортеж (x', y'), координаты точки после преобразования
    """
    x, y = point
    transformed = np.dot(matrix, np.array([x, y]))
    return transformed[0], transformed[1]

# Пример использования
matrix = np.array([[2, 1], [-1, 3]])
print("Матрица линейного преобразования:")
print(matrix)

for point in points:
    new_point = transform_point(point, matrix)
    print(f"Точка {point} преобразована в {new_point}")