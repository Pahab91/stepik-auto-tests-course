'''Если приведенная ниже задача кажется вам сложной, то вам следует пройти первый курс по языку Python,
который не требует начальных знаний языка: https://stepic.org/course/Программирование-на-Python-67﻿.
Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.
Вашей программе на вход подается последовательность строк.
Первая строка содержит число n (1 ≤ n ≤ 100).
В следующих n строках содержится по одному целому числу.
Выведите одно число – сумму данных n чисел.
Примечание:
﻿Чтобы считать одно число из стандартного потока ввода, можно использовать, например, следующий код'''
#
# s = []
# number = 0
# n = int(input())
# for i in range(n):
#     s.append(int(input()))
#     number = int(s[i]) + number
# print(number)


"""Количеством различных объектов называется максимальный размер множества объектов, 
в котором любые два объекта являются различными.
Рассмотрим пример:
objects = [1, 2, 1, 2, 3] # будем считать, что одинаковые числа соответствуют одинаковым объектам, 
а различные – различным
Тогда все различные объекты являют собой множество {1, 2, 3}﻿. 
Таким образом, количество различных объектов равно трём."""


# #objects = [1, 2, 1, 2, 3]
# objects1 = set()
# for i in objects:
#     objects1.add(id(i))
# print(len(objects1))

#print(type(None))


""" 1. Создайте класс Point3D, который хранит координаты в виде списка. Пропишите у него конструктор для создания
экземпляров с локальными координатами. Также добавьте методы, позволяющие изменять координаты и получать их (в виде
кортежа). """
# class Point3D:
#     x, y, z = [0, 0, 0]
#
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def cortage(self, x, y, z):
#         a = (x, y, z)
#         return a
#
#
# cord1 = Point3D(1, 2, 3)
# print(cord1.__dict__)
# print(cord1.cortage(4, 5, 6))


"""2. Объявите класс Point с конструктором, который бы позволял создавать экземпляр на основе другого, 
уже существующего. Если аргументы в конструктор не передаются, то создается объект с локальными атрибутами по 
умолчанию. """

# class Point:
#     def __init__(self, x_or_obj=0, y=0):
#         if isinstance(x_or_obj, Point):  # ВАЖНО!!!
#             self.x = x_or_obj.x  # ВАЖНО!!! p1 и значение х = р2 и значение х
#             self.y = x_or_obj.y
#         else:
#             self.x = x_or_obj
#             self.y = y
#
#
# p1 = Point(1, 2)
# p2 = Point(p1)
# print(p1)
# print(p2)
# print(p1.__dict__)
# print(p2.__dict__)


"""3. Напишите программу, в которой пользователь вводит координаты x, y с клавиатуры, создается соответствующий 
экземпляр и он сохраняется в списке. Количество вводимых объектов N=5. Затем, вывести их атрибуты в консоль. """

# class List_cords:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# n = 2
# l1 = []
# for i in range(n):
#     dot = List_cords(int(input()), int(input()))
#     l1.append(dot)
# #   print(dot.__dict__)
# print(l1)
# for dot in l1:
#     print(dot.__dict__)


"""Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно 
положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность 
добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее 
вместимость. 
При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True﻿."""

# class MoneyBox:
#     def __init__(self, capacity=10, n_coins=0):
#         self.capacity = capacity
#         self.n_coins = n_coins
#
#     # конструктор с аргументом – вместимость копилки
#
#     def can_add(self, v):
#         self.v = v
#         if self.v <= (self.capacity - self.n_coins):
#             return True
#
#         else:
#             return False
#         # True, если можно добавить v монет, False иначе
#
#     def add(self, v):
#         if self.can_add(self.v) is True:
#             self.n_coins += v


"""Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел 
из этой последовательности, затем сумму второй пятерки, и т. д. 
Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части. 
Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д. 
Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок 
последовательных элементов по мере их накопления. 
Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно 
необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма. """

# class Buffer:
#     def __init__(self):
#         self.b = []
#
#     def add(self, *a):
#         self.a = list(a)
#         self.b += a
#         #        print(self.b)
#         for i in range(len(self.b)):
#             if len(self.b) >= 5:
#                 print(self.b[0] + self.b[1] + self.b[2] + self.b[3] + self.b[4])
#                 self.b = self.b[5:]
#
#     def get_current_part(self):
#         return self.b
#
#
# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part()  # вернуть [1, 2, 3]
# buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part()  # вернуть [6]
# buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part()  # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part()


"""Реализуйте структуру данных, представляющую собой расширенную структуру стек. Необходимо поддерживать добавление 
элемента на вершину стека, удаление с вершины стека, и необходимо поддерживать операции сложения, вычитания, 
умножения и целочисленного деления. 
Операция сложения на стеке определяется следующим образом. Со стека снимается верхний элемент (top1), затем снимается 
следующий верхний элемент (top2), и затем как результат операции сложения на вершину стека кладется элемент, 
равный top1 + top2. 
Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2) и целочисленного деления (
top1 // top2). 
Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.
Требуемая структура класса:"""

# class ExtendedStack(list):
#
#
#     def sum(self):
#         if len(self) >= 2:
#             self.append(self.pop() + self.pop())
#
#
#     def sub(self):
#         if len(self) >= 2:
#             self.append(self.pop() - self.pop())
#
#     def mul(self):
#         if len(self) >= 2:
#             self.append(self.pop() * self.pop())
#
#     def div(self):
#         if len(self) >= 2:
#             self.append(self.pop() // self.pop())
#
#
# def test():
#     ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
#     ex_stack.div()
#     assert ex_stack.pop() == 2
#     ex_stack.sub()
#     assert ex_stack.pop() == 6
#     ex_stack.sum()
#     assert ex_stack.pop() == 7
#     ex_stack.mul()
#     assert ex_stack.pop() == 2
#     assert len(ex_stack) == 0
# test()