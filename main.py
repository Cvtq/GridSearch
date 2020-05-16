# Вариант 2

cuts = [[-5, 5], [-5, 5], [-5, 5]]
f = "x**2 - 2*x + y**2 + 4*y + z**2 - 8*z + 21"

def findExtr(f, c):
    cuts = c
    k = len(cuts)
    m = 5
    d = cuts[0][1] - cuts[0][0]
    h = d / m

    min = None

    e = 0.0001

    # Пока шаг сетки больше eps
    while (h > e):

        # Найдем координаты всех точек сетки
        grid = []
        for i in range(m):
            x = cuts[0][0] + i * h
            for j in range(m):
                 y = cuts[1][0] + j * h
                 for k in range(m):
                     z = cuts[2][0] + k * h
                     grid.append([x, y, z])

        # Предположим, что минимум в первых координатах
        x = grid[0][0]
        y = grid[0][1]
        z = grid[0][2]
        min = eval(f)
        pMinimum = [x, y, z]

        # Найдем минимум
        for i in range(len(grid) - 1):
            x = grid[i + 1][0]
            y = grid[i + 1][1]
            z = grid[i + 1][2]
            point = eval(f)

            if point < min:
                min = point
                pMinimum = [x, y, z]

        # Сузим поиск
        for i in range(len(cuts)):
            cuts[i] = [pMinimum[i] - h, pMinimum[i] + h]

        d = cuts[0][1] - cuts[0][0]
        h = d / m

    print("Min = {}".format(min))
    print("At ({}, {}, {})".format(pMinimum[0], pMinimum[1], pMinimum[2]))

findExtr(f, cuts)
