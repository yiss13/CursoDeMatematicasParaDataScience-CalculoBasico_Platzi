import numpy as np
import matplotlib.pyplot as plt


def g(x):
    return x ** 2


def f(x):
    return np.sin(x)


def plot(x, y):
    fig, ax = plt.subplots()
    plt.xlim(-10, 10)
    plt.ylim(-1, 1)
    ax.plot(x, y)
    ax.grid()
    ax.axhline(y = 0, color = "g")
    ax.axvline(x = 0, color = "g")
    plt.xlabel("x-Independiente")
    plt.ylabel("y-Dependiente")
    plt.show()


def run():
    x = np.linspace(-10, 10, num = 1000)
    y = f(g(x))
    
    plot(x, y)


if __name__ == "__main__":
    run()