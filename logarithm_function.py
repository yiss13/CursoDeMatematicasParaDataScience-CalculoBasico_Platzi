import numpy as np
import matplotlib.pyplot as plt


def logarithmFunction(x):
    return np.log2(x)


def plot(x, y):
    fig, ax = plt.subplots()
    plt.xlim(0, 3)
    plt.ylim(-7, 2)
    ax.plot(x, y)
    ax.grid()
    ax.axhline(y = 0, color = "g")
    ax.axvline(x = 0, color = "g")
    plt.xlabel("x-Independiente")
    plt.ylabel("y-Dependiente")
    plt.show()


def run():
    x = np.linspace(0.01, 2.0, num = 100)
    y = logarithmFunction(x)
    
    plot(x, y)


if __name__ == "__main__":
    run()