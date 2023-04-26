import numpy as np


def my_cubic_spline(x, y, X):

    # Calculate the second derivatives of the function at each point
    n = len(x)
    h = np.zeros(n - 1)
    b = np.zeros(n - 1)
    u = np.zeros(n - 1)
    v = np.zeros(n - 1)

    for i in range(n - 1):
        h[i] = x[i + 1] - x[i]
        b[i] = (y[i + 1] - y[i]) / h[i]

    u[1] = 2.0 * (h[0] + h[1])
    v[1] = 6.0 * (b[1] - b[0])

    for i in range(2, n - 1):
        u[i] = 2.0 * (h[i - 1] + h[i - 2]) - h[i - 2] ** 2 / u[i - 1]
        v[i] = 6.0 * (b[i] - b[i - 1]) - h[i - 2] * v[i - 1] / u[i - 1]

    z = np.zeros(n)
    z[-2] = v[-1] / u[-1]

    for i in range(n - 3, -1, -1):
        z[i + 1] = (v[i] - h[i] * z[i + 2]) / u[i + 1]

    # Evaluate the cubic spline at each point in X
    m = len(X)
    Y = np.zeros(m)

    for i in range(m):
        j = np.searchsorted(x, X[i], side='right') - 1
        if j < 0:
            j = 0
        elif j >= n - 1:
            j = n - 2

        t = (X[i] - x[j]) / h[j]
        Y[i] = ((z[j + 1] - z[j]) * t + 3.0 * (y[j + 1] - y[j]) / h[j] - (2.0 * z[j] + z[j + 1]) * t ** 2) * t + y[j]

    return Y
