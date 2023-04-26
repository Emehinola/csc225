import numpy as np
import matplotlib.pyplot as plt


# Define the sin function
def sin(x):
    return np.sin(x)


# Define the Taylor series approximations
def taylor(x, n):
    if n == 0:
        return x*0
    elif n == 1:
        return x
    elif n == 3:
        return x - (x**3)/6
    elif n == 5:
        return x - (x**3)/6 + (x**5)/120
    elif n == 7:
        return x - (x**3)/6 + (x**5)/120 - (x**7)/5040


def plot_sine():
    # Define the x values for the plot
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    # Plot the sin function and the Taylor series approximations
    plt.plot(x, sin(x), label='sin(x)')
    plt.plot(x, taylor(x, 1), label='1st order')
    plt.plot(x, taylor(x, 3), label='3rd order')
    plt.plot(x, taylor(x, 5), label='5th order')
    plt.plot(x, taylor(x, 7), label='7th order')

    # Set the plot title and axis labels
    plt.title('sin(x) and Taylor Series Approximations')
    plt.xlabel('x')
    plt.ylabel('y')

    # Set the legend and show the plot
    plt.legend()
    plt.show()

