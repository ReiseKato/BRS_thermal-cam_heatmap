import matplotlib.pyplot as plt
import numpy as np
import time

'''
BRS Motorsport: Melexis (768 -> 32x24)
'''

def show_heatmap_single_frame(data: np.array, size: (int, int), vmin: float, vmax: float):
    adj_data = np.reshape(data, size)
    plt.imshow(adj_data, vmin=vmin, vmax=vmax, cmap='inferno', interpolation='hamming')
    plt.colorbar()
    #plt.show()

def show_heatmap_video(data: np.array, size: (int, int), vmin: float, vmax: float, frequency: float):
    n = len(data)
    cut = n%(size[0]*size[1])
    data = data[0:(n-cut)]
    n = len(data)
    index = 0
    while(index < n):
        cut_data = data[index:(size[0] * size[1])]
        index += size[0] * size[1]
        show_heatmap_single_frame(cut_data, size=size, vmin=vmin, vmax=vmax)
        time.sleep(1.0/frequency)



if __name__ == "__main__":
    size = (32, 24)
    data = np.random.randint(0, 100, size=32*24*16*10)
    # show_heatmap_video(data, size=size, vmin=0, vmax=100, frequency=16.0)
    print(size[0]*size[1])
    n = len(data)
    print(n)
    cut = n % (size[0] * size[1])
    data = data[0:(n - cut)]
    print(len(data))

