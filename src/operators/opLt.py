import scipy.signal as signal
import numpy as np

def Lt(x):
    dim = (np.min(np.shape(x)) > 1) + 1
    if dim == 1:
        ker = np.array([1, -2, 1], dtype=np.float64)
        lap = signal.convolve(x, ker, mode='same')
    elif dim == 2:
        ker = np.array([[0,1,0], [1,-4,1], [0,1,0]], dtype=np.float64) # V4
        # ker = np.array([[1,1,1], [1,-8,1], [1,1,1]], dtype=np.float64) # V8
        lap = signal.convolve2d(x, ker, mode='same', boundary='symm')
    return lap

def main():
    pass

if __name__ == '__main__':
    main()