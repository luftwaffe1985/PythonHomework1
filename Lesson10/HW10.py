# Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум, 
# максимум и среднее арифметическое последовательности целых чисел.
# Экземпляры классов инициализируются без аргументов. 
# Метод add_number должен добавлять в статистику число, которое будет учтено при вычислении финального результата методом result. 
# Для экземпляров MinStat и MaxStat result должен возвращать целое число, 
# для AverageStat — число типа float (это число будет сравниваться с правильным ответом до седьмой значащей цифры).
# Если в последовательности отсутствуют числа и статистические величины вычислить невозможно, метод result должен возвращать None.

# class MinStat:
#     def __init__(self):
#         self.some_list = []

#     def add_number(self, n):
#         self.some_list.append(n)

#     def result(self):
#         if self.some_list == []:
#             return None
#         else:
#             return min(self.some_list)


# class MaxStat:
#     def __init__(self):
#         self.some_list = []

#     def add_number(self, n):
#         self.some_list.append(n)

#     def result(self):
#         if self.some_list == []:
#             return None
#         else:
#             return max(self.some_list)


# class AverageStat:
#     def __init__(self):
#         self.some_list = []

#     def add_number(self, n):
#         self.some_list.append(n)

#     def result(self):
#         if self.some_list == []:
#             return None
#         else:
#             return sum(self.some_list) / len(self.some_list)


# values = [1, 2, 4, 5]

# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)

# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))


# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()

# print(mins.result(), maxs.result(), average.result())


# values = [1, 0, 0]

# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()
# for v in values:
#     mins.add_number(v)
#     maxs.add_number(v)
#     average.add_number(v)

# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))

# Реализуйте класс Table, который хранит целые числа в двумерной таблице.
# При инициализации Table(rows, cols) экземпляру передаются число строк и столбцов в таблице.
# Строки и столбцы нумеруются с нуля. Ячейки таблицы инициализируются нулями.
# table.get_value(row, col) — прочитать значение из ячейки со строкой row, столбцом col.
# Если ячейка с индексами row и col не лежит внутри таблицы, нужно вернуть None.
# table.set_value(row, col, value) — записать число в ячейку со строкой row, столбцом col.
# Гарантируется, что в тестах будет в запись только в ячейки внутри таблицы.
# table.n_rows() — вернуть число строк в таблице.
# table.n_cols() — вернуть число столбцов в таблице.
# Формат ввода --------
# Каждый тест представляет собой код, в котором будут использоваться ваш класс.
# Файл c решением необязательно называть solution.py, он будет переименован автоматически.
# Тест запускается с вашим классом, а его вывод сравнивается с правильным решением.

# class Table():

#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         self.table = [[0] * cols for _ in range(rows)]

#     def get_value(self, row, col):
#         if 0 <= row < self.rows and 0 <= col < self.cols:
#             return self.table[row][col]
#         else:
#             return None
        
#     def set_value(self, row, col, value):
#         self.table[row][col] = value

#     def n_rows(self):
#         return self.rows

#     def n_cols(self):
#         return self.cols

#     def delete_row(self, row):
#         self.table.pop(row)
#         self.rows -= 1

#     def delete_col(self, col):
#         for row in range(self.rows):
#             self.table[row].pop(col)
#         self.cols -= 1

#     def add_row(self, row):
#         self.table.insert(row, [0] * self.cols)
#         self.rows += 1

#     def add_col(self, col):
#         for row in range(self.rows):
#             self.table[row].insert(col, 0)
#         self.cols += 1


# tab = Table(3, 5)
# tab.set_value(0, 1, 10)
# tab.set_value(1, 2, 20)
# tab.set_value(2, 3, 30)
# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.add_row(1)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()


# tab = Table(2, 2)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.set_value(0, 0, 10)
# tab.set_value(0, 1, 20)
# tab.set_value(1, 0, 30)
# tab.set_value(1, 1, 40)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.add_row(0)
# tab.add_col(1)

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()


# tab = Table(1, 1)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.set_value(0, 0, 1000)

# for i in range(tab.n_rows()):
#     for j in range(tab.n_cols()):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()

# tab.add_row(0)
# tab.add_row(2)
# tab.add_col(0)
# tab.add_col(2)

# tab.set_value(0, 0, 2000)
# tab.set_value(0, 2, 3000)
# tab.set_value(2, 0, 4000)
# tab.set_value(2, 2, 5000)

# for i in range(-1, tab.n_rows() + 1):
#     for j in range(-1, tab.n_cols() + 1):
#         print(tab.get_value(i, j), end=' ')
#     print()
# print()