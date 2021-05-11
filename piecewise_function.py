import numpy as np
import matplotlib.pyplot as plt


def piecewiseFunction(x):
    y = np.zeros(len(x))

    for idx, x in enumerate(x):

        if x >= 0:
            y[idx] = 1.0

    return y


def plot(x, y):
    fig, ax = plt.subplots()
    plt.xlim(-10, 10)
    plt.ylim(-1, 2)
    ax.plot(x, y)
    ax.grid()
    # ax.axhline(y = 0, color = "g")
    # ax.axvline(x = 0, color = "g")
    plt.xlabel("x-Independiente")
    plt.ylabel("y-Dependiente")
    plt.show()


def run():
    x = np.linspace(-10.0, 10.0, num = 1000)
    y = piecewiseFunction(x)

    print("La función es: x^2")
    
    plot(x, y)


if __name__ == "__main__":
    run()