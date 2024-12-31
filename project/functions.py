'''в этом файле прописаны функции для работы с уравнениями функций и класс для обработки стандартных уравнений'''
import matplotlib.pyplot as plt
from aiogram.types import FSInputFile
import numpy as np
from validation import valid_a, valid_b, valid_c, valid_k
class two_D_graph:
    def __init__(self, a=0, b=0, c=0, k=0):
        self.a = valid_a(a)
        self.b = valid_b(b)
        self.c = valid_c(c)
        self.k = valid_k(k)
        self.list_x = list()
        self.list_y = list()
        self.photo = None



    def x_root(self):
        '''функция создает списки переменных подходящих данному уравнению корня'''
        try:
            for x in range(-50, 50):
                y = (self.a * x + self.b) ** 0.5 + self.c
                self.list_x.append(x)
                self.list_y.append(y)
        except TypeError:
            raise TypeError


    def x_gip(self):
        '''функция создает списки переменных подходящих данному уравнению гиперболы'''
        try:
            for x in range(-50, 50):

                if x + self.a != 0:
                    y = self.k / (x + self.a)
                    self.list_x.append(x)
                    self.list_y.append(y)
        except TypeError:
            raise TypeError


    def x_cube(self):
        '''функция создает списки переменных подходящих данному кубическому уравнению'''
        try:
            for x in range(-50, 50):
                y = self.a * x ** 3 + self.b
                self.list_x.append(x)
                self.list_y.append(y)
        except TypeError:
            raise TypeError


    def x_square(self):
        '''функция создает списки переменных подходящих данному квадратному уравнению'''
        try:
            for x in range(-50, 50):
                y = self.a * x ** 2 + self.b * x + self.c
                self.list_x.append(x)
                self.list_y.append(y)
        except TypeError:
            raise TypeError

    def x_line(self):
        '''функция создает списки переменных подходящих данному уравнению прямой'''
        try:
            for x in range(-50, 50):
                y = self.k * x + self.b
                self.list_x.append(x)
                self.list_y.append(y)
        except TypeError:
            raise TypeError



    def f_graph(self):
        '''функция рисует график функции и сохраняет его в переменной photo в формате png'''
        plt.clf()
        # очищает график, если бот уже использовался
        plt.plot(self.list_x, self.list_y)
        # строит график
        plt.grid()
        # чертит сетку

        arrowprops = {'arrowstyle': '->'}
        plt.annotate('', xy=(50, 0), xytext=(-50, 0), arrowprops=arrowprops)
        plt.annotate('', xy=(0, 50), xytext=(0, -50), arrowprops=arrowprops)
        # создает стрелочки для Ох и Оу
        plt.savefig('image.png')
        self.photo = FSInputFile('image.png')
        # return self.photo



def graph(equation):
    '''функция рисует график на плоскости записанного уравнения и сохраняет его в переменной photo в формате png'''
    plt.clf()
    list_x = list()
    list_y = list()
    for x in range(-50, 50):
        for y in range(-50, 50):
            if eval(equation):
                list_x.append(x)
                list_y.append(y)
                # при верном равенстве введенного уравнения элементы добавляются в список

    plt.plot(list_x, list_y)
    plt.grid()
    arrowprops = {'arrowstyle': '->'}
    plt.annotate('', xy=(50, 0), xytext=(-50, 0), arrowprops=arrowprops)
    plt.annotate('', xy=(0, 50), xytext=(0, -50), arrowprops=arrowprops)

    plt.savefig('image.png')
    photo = FSInputFile('image.png')
    return photo

def graph_3d(equation3d):
    '''функция рисует график в 3d пространстве и сохраняет его в переменной photo в формате png'''
    plt.clf()
    ax = plt.axes(projection='3d')
    x = np.linspace(-100, 100, 100)
    y = np.linspace(-100, 100, 100)
    x, y = np.meshgrid(x, y)
    z = eval(equation3d)
    ax.plot3D(x, y, z, 'green')
    plt.grid()
    plt.savefig('image.png')
    photo = FSInputFile('image.png')
    return photo