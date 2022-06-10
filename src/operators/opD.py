import scipy.signal as signal
import numpy as np

def D(x):
    dim = (np.min(np.shape(x)) > 1) + 1
    if dim == 1:
        ker = np.array([-1, 0, 1], dtype=np.float64)
        grad = signal.convolve(x, ker, mode='same')
    elif dim == 2:
        scharr = np.array([[ -3-3j, 0-10j,  +3 -3j],
                           [-10+0j, 0+ 0j, +10 +0j],
                           [ -3+3j, 0+10j,  +3 +3j]]) # Gx + j*Gy
        grad = signal.convolve2d(x, scharr, mode='same', boundary='symm')
    return grad

def main():
    pass

if __name__ == '__main__':
    main()