import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np
import time

'''
BRS Motorsport: Melexis (768 -> 32x24)
'''

def show_heatmap_single_frame(data: np.array, size: (int, int), vmin: float, vmax: float):
    adj_data = np.reshape(data, size)
    plt.imshow(adj_data, vmin=vmin, vmax=vmax, cmap='inferno', interpolation='hamming')
    plt.colorbar()
    plt.show()

def show_heatmap_video(data: np.array, size: (int, int), vmin: float, vmax: float, frequency: float):
    n = len(data)
    cut = n%(size[0]*size[1])
    data = data[0:(n-cut)]
    n = len(data)
    index = 0
    count = 1
    while(index < n):
        cut_data = data[index:(size[0] * size[1])*count]
        index += size[0] * size[1]
        count += 1
        show_heatmap_single_frame(cut_data, size=size, vmin=vmin, vmax=vmax)
        time.sleep(1.0/frequency)

def main():
    nx = 50
    ny = 50

    fig = plt.figure()
    data = np.random.rand(nx, ny)
    im = plt.imshow(data)

    def init():
        im.set_data(np.zeros((nx, ny)))

    def animate(i):
        # xi = i // ny
        # yi = i % ny
        data = np.random.rand(nx, ny)
        im.set_data(data)
        return im

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=50, repeat=False)


if __name__ == "__main__":
    size = (32, 24)
    data = np.random.randint(0, 100, size=32*24*16*10)
    # show_heatmap_video(data, size=size, vmin=0, vmax=100, frequency=16.0)
    main()



