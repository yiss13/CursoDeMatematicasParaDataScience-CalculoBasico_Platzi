import numpy as np
import matplotlib.pyplot as plt


def linealFunction(m, x, b):
    return m * x + b


def plot(x, y):
    fig, ax = plt.subplots()
    plt.xlim(-20, 20)
    plt.ylim(-20, 20)
    ax.plot(x, y)
    ax.grid()
    ax.axhline(y = 0, color = "g")
    ax.axvline(x = 0, color = "g")
    plt.xlabel("x-Independiente")
    plt.ylabel("y-Dependiente")
    plt.show()


def run():
    m = 1
    b = 2
    x = np.linspace(-10.0, 10.0, num = 100)
    y = linealFunction(m, x, b)

    print("La función es: y =", m, "* x +", b)
    
    plot(x, y)


if __name__ == "__main__":
    run()