#
#
while True:
    try:
        a = int(input('Введите количество столбцов: '))#stolb
        b = int(input('Введите количество строк: '))#stroki
        matrix = [[0] * a for i in range(b)]
        print('Исходная матрица:')
        for i in range(b):
            for j in range(a):
                matrix[i][j] = int(input(f'Введите элемент[{i + 1},{j + 1}]: '))
        def bebra(matrix):
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix[i])):
                    print(matrix[i][j], end=' ')
                print('\n')
        bebra(matrix)
        minel = []
        minel.append(min(min(matrix[i])for i in range(1, b, 2)))
        minel.append(min(min(matrix[i])for i in range(0, b)))
        minel.append(max(max(matrix[i])for i in range(0, b)))
        print(minel)
        p, p2 = [], []
        for i in range(b):
            for j in range(a):
                if matrix[i][j] == minel[1]:
                    p = [i, j]
                if matrix[i][j] == minel[2]:
                    p2 = [i, j]
        matrix[p[0]][p[1]], matrix[p2[0]][p2[1]] = matrix[p2[0]][p2[1]], matrix[p[0]][p[1]]
        print('Матрица2:')
        bebra(matrix)
        print('Минимальный элемент чётной строки:', minel[0])
        break
    except ValueError:
        print('Ошибка ввода! введите заново.')
#проверка на коммит часть 2