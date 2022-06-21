import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

def D(x):
    dim = (np.min(np.shape(x)) > 1) #+ 1
    if dim == 1:
        # ker = np.array([.5, 0, -.5], dtype=np.float64)
        # ker = ker / np.linalg.norm(ker)
        # grad = signal.convolve(x, ker, mode='same')
        grad = np.gradient(x)
    elif dim == 2:
        scharr = np.array([[ -3-3j, 0-10j,  +3 -3j],
                           [-10+0j, 0+ 0j, +10 +0j],
                           [ -3+3j, 0+10j,  +3 +3j]]) # Gx + j*Gy
        grad = signal.convolve2d(x, scharr, mode='same', boundary='symm')
    return grad

def main():
    # x = np.linspace(-3.14, 3.14, 100)
    # y = np.sin(x)
    # Dy = np.gradient(y)

    # plt.plot(x, y, 'b-', label='y')
    # plt.plot(x, Dy, 'r-', label='D(y)')
    
    # plt.grid()
    # plt.legend()
    # plt.show()

    pass

if __name__ == '__main__':
    # main()
    x = np.linspace(-3.14, 3.14, 100)
    y = np.sin(x)
    Dy = np.gradient(y)

    plt.plot(x, y, 'b-', label='y')
    plt.plot(x, Dy, 'r-', label='D(y)')
    
    plt.grid()
    plt.legend()
    plt.show()