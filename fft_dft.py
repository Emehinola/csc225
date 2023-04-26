import numpy as np
import time


# Generate 2048-length signal
signal = np.random.rand(2048)

# Compute FFT and record the time
start_time = time.time()
fft = np.fft.fft(signal)
fft_time = time.time() - start_time

# Compute DFT and record the time
start_time = time.time()
dft = np.zeros_like(fft)
dft_time = None


def main_code():
    global dft_time

    N = len(signal)
    for k in range(N):
        for n in range(N):
            dft[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)
    dft_time = time.time() - start_time

    # Compare the times
    print(output_fft())
    print(output_dft())


def output_fft():
    return f'FFT Time Output: {fft_time}'


def output_dft():
    return f'DFT Time Output: {dft_time}'
