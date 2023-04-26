import numpy as np

"""

"""


def idft(x):
    N = len(x)
    idft_x = np.zeros(N, dtype=np.complex128)

    for n in range(N):
        for k in range(N):
            idft_x[n] += (1/N) * np.exp(2j*np.pi*k*n/N) * x[k]
    return idft_x


x = [1, 2, 3, 4]
idft_x = idft(x)


def display_output():
    print(f"Output: {idft_x}")  # display output

