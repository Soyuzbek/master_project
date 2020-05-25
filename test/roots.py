# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 09:59:38 2020

@author: Raimbek Sultanov
"""
import matplotlib.pyplot as plt
import numpy as np
# Заданная функция
def f0(x):
#    return 2
#    return 2*x
#    return (x-4.0)*(x-4.0)-4
#    http://mathprofi.ru/metod_kasatelnyh.html
#    return np.exp(x)-x-2.0
#    return x*x-np.sin(x)
# Из википедии Контрпримеры
# https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D1%82%D0%BE%D0%B4_%D0%9D%D1%8C%D1%8E%D1%82%D0%BE%D0%BD%D0%B0
#    return np.cos(x)-x**3
#    return x**3-2*x+2
#    return x**2
    if np.abs(x) < 1.0e-15:
        return 0.0
    else:
        return x+x**2*np.sin(2.0/x) # Есть мнимые корни !!!! надо анализировать
#      return x + (x**4)**(1/3.0) 
# Производные заданной функции
def d1f(x0,h):
    return (f0(x0+h)-f0(x0-h))/(2*h)
def d2f(x0,h):
    return (d1f(x0+h,h)-d1f(x0-h,h))/(2*h)
def d3f(x0,h):
    return (d2f(x0+h,h)-d2f(x0-h,h))/(2*h)
def d4f(x0,h):
    return (d3f(x0+h,h)-d3f(x0-h,h))/(2*h)
def d5f(x0,h):
    return (d4f(x0+h,h)-d4f(x0-h,h))/(2*h)

eps = 0.00001 # Точность приближения
h = 0.001 # Шаг для вычисления производной

x0 =  -0.001 # Начальное приближение
print("Начальное приближение x[0] = ",x0)
# Выберем x1 так чтобы abs(x1-x0) > eps. Это для начало цикла
if np.abs(x0) > 1.0e-100:
    x1 = x0 + np.sign(x0)*(1.0+np.abs(eps))
else:
    x1 = 1.0
# Алгоритм
k=0 # Счетчик итераций
d =  np.abs(x1-x0) # Оценка приближения
while d > eps:
    k += 1
    c0=f0(x0)           # Коэффиценты ряда Тейлора
    c1=d1f(x0,h)        # Коэффиценты ряда Тейлора
    c2=d2f(x0,h)/2.0    # Коэффиценты ряда Тейлора
    c3=d3f(x0,h)/6.0    # Коэффиценты ряда Тейлора
    c4=d4f(x0,h)/24.0   # Коэффиценты ряда Тейлора
    c5=d5f(x0,h)/120.0  # Коэффиценты ряда Тейлора
    proots=np.roots([0,0,0,0,c1,c0])     # Метод Ньютона
    proots=np.roots([0,0,0,c2,c1,c0])    # Метод Парабол
    proots=np.roots([0,0,c3,c2,c1,c0])   # Метод Ньютона с 3 производной
    proots=np.roots([0,c4,c3,c2,c1,c0])  # Метод Ньютона с 4 производной
    proots=np.roots([c5,c4,c3,c2,c1,c0]) # Метод Ньютона с 5 производной
    if len(proots) > 0:
        x1=proots[np.abs(proots).argmin()]+x0 # Ядро принципа выбора решений из {h[i]} 
        rootIs = True
    else:
        rootIs = False
        break
    print("x["+str(k)+"] = ",x1)
    d = np.abs(x1-x0)
    x0 = x1
    
if rootIs:
    print("Корень  x["+str(k)+"] = ",x1, "Значения функции = ",f0(x1))
else:
    print("Нет корней")

x = np.arange(-0.5,0.5,0.01)
y = x
i=0
while i < len(x):
    y[i] =f0(x[i])
    i +=1
plt.plot(y)
plt.show()
x = np.arange(0.05,1.0,0.001)
y = x
i=0
while i < len(x):
    y[i] =d1f(x[i],h/10)
    i +=1
plt.plot(y)
plt.show()
