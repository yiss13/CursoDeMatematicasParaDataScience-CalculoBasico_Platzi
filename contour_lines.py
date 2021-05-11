from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt


def function(x, y):
    return np.sin(x) + 2 * np.cos(y)


def plot(x, y, z):
    fig, ax = plt.subplots(subplot_kw = {"projection":"3d"})
    surf = ax.plot_surface(x, y, z, cmap = cm.cool)
    fig.colorbar(surf)
    plt.show()


def contourLines(x, y, z, res):
    fig, ax = plt.subplots()
    levelMap = np.linspace(np.min(z), np.max(z), num = res)
    cp = ax.contour(x, y, z, levels = levelMap, cmap = cm.cool) # Muestra las líneas
    cp = ax.contourf(x, y, z, levels = levelMap, cmap = cm.cool) # Muestra una superfice
    fig.colorbar(cp)
    plt.show()


def run():
    res = 100
    x = np.linspace(-4, 4, num = res)
    y = np.linspace(-4, 4, num = res)
    x, y = np.meshgrid(x, y)
    z = function(x, y)

    plot(x, y, z)
    contourLines(x, y, z, res)


if __name__ == "__main__":
    run()