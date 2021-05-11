import numpy as np
import matplotlib.pyplot as plt


def polynomialFunction(x):
    return x ** 2


def plot(x, y):
    fig, ax = plt.subplots()
    plt.xlim(-20, 20)
    plt.ylim(-5, 100)
    ax.plot(x, y)
    ax.grid()
    ax.axhline(y = 0, color = "g")
    ax.axvline(x = 0, color = "g")
    plt.xlabel("x-Independiente")
    plt.ylabel("y-Dependiente")
    plt.show()


def run():
    x = np.linspace(-10.0, 10.0, num = 100)
    y = polynomialFunction(x)

    print("La función es: x^2")
    
    plot(x, y)


if __name__ == "__main__":
    run()