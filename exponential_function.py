import numpy as np
import matplotlib.pyplot as plt


def exponentialFunction(x):
    return np.e ** x


def plot(x, y):
    fig, ax = plt.subplots()
    plt.xlim(-5, 5)
    plt.ylim(0, 3)
    ax.plot(x, y)
    ax.grid()
    ax.axhline(y = 0, color = "g")
    ax.axvline(x = 0, color = "g")
    plt.xlabel("x-Independiente")
    plt.ylabel("y-Dependiente")
    plt.show()


def run():
    x = np.linspace(-4.0, 1.0, num = 100)
    y = exponentialFunction(x)
    
    plot(x, y)


if __name__ == "__main__":
    run()