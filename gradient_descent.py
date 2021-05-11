from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt


def function(x, y):
    return x ** 2 + y ** 2


def derivate(increasedPoint, point, h):
    return (function(increasedPoint[0], increasedPoint[1]) - function(point[0], point[1])) / h


def plot(x, y, z):
    fig, ax = plt.subplots(subplot_kw = {"projection":"3d"})
    surf = ax.plot_surface(x, y, z, cmap = cm.cool)
    fig.colorbar(surf)
    plt.show()


def contourLines(x, y, z, res):
    fig, ax = plt.subplots()
    levelMap = np.linspace(np.min(z), np.max(z), num = res)
    cp = ax.contourf(x, y, z, levels = levelMap, cmap = cm.cool) 
    fig.colorbar(cp)
    plt.title("Descenso del gradiente")

    point = np.random.rand(2) * 8 - 4 # La función rand(2) regresa un vector entre 0 y 1 de 2 componentes, como el punto va a estar definido entre 0 y 1, pero lo que se requiere es que esté entre -4 y 4 al valor dado por la función rand se multplica por 8 y se resta 4.
    plt.plot(point[0], point[1], "o", c = "k")

    for i in range(1000):
        learningRate = 0.01
        point = point - learningRate*gradientDescent(point) # Fórmula del descenso del gradiente

        if i % 10 == 0:
            plt.plot(point[0], point[1], "o", c = "g")
    
    plt.plot(point[0], point[1], "o", c = "w")

    plt.show()


def gradientDescent(point):
    grad = np.zeros(2)
    h = 0.01

    for idx, val in enumerate(point):
        copyPoint = np.copy(point)
        copyPoint[idx] = copyPoint[idx] + h
        partialDerivative = derivate(copyPoint, point, h)
        grad[idx] = partialDerivative

    return grad


def run():
    res = 100
    x = np.linspace(-4, 4, num = res)
    y = np.linspace(-4, 4, num = res)
    x, y = np.meshgrid(x, y)
    z = function(x, y)

    # plot(x, y, z)
    contourLines(x, y, z, res)


if __name__ == "__main__":
    run()