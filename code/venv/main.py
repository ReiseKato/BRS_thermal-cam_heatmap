import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FFMpegWriter
mpl.rcParams['animation.ffmpeg_path'] = r"S:\ffmpeg\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe"
import numpy as np
import time
import os

'''
BRS Motorsport: Melexis (768 -> 32x24)
'''

# original_data = np.random.randint(0, 100, size=32*24*16*10)

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
    count = 1
    while(index < n):
        cut_data = data[index:(size[0] * size[1])*count]
        index += size[0] * size[1]
        count += 1
        show_heatmap_single_frame(cut_data, size=size, vmin=vmin, vmax=vmax)
        time.sleep(1.0/frequency)

def prepare_data(data: np.array, size: (int, int)):
    n = len(data)
    cut = n % (size[0] * size[1])
    data = data[0:(n - cut)]
    return data

def heatmap_video(data: np.array, size: (int, int), vmin: float, vmax: float, frequency: float, save: int):
    nx = size[0]
    ny = size[1]
    prepare_data(data, size)
    counter = 1

    fig = plt.figure()
    first_frame = np.reshape(data[0:nx*ny], size)
    im = plt.imshow(first_frame, vmin=vmin, vmax=vmax, cmap='inferno', interpolation='hamming')
    frames = int(len(data)/(nx*ny)) - 1

    def init():
        im.set_data(np.zeros((nx,ny)))

    def animate(data: np.array):
        nonlocal counter
        start_index = nx * ny * counter
        end_index = min(nx * ny * (counter + 1), len(original_data))
        adj_data = original_data[start_index:end_index]
        adj_data = np.reshape(adj_data, size)
        im.set_data(adj_data)
        counter += 1
        return im

    def animate2(data: np.array):
        data = np.random.randint(0, 100, size=32 * 24)
        adj_data = np.reshape(data, size)
        im.set_data(adj_data)
        return im

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=1.0/frequency, repeat=False)
    plt.colorbar()
    if(save):
        filename = r"S:\BRS Motorsport\workplace_priv\heatmap.mp4"
        writer = animation.FFMpegWriter(fps=frequency)
        anim.save(filename, writer=writer)
    else:
        plt.show()


def test():
    size = (32, 24)
    data = np.random.randint(0, 100, size=32 * 24 * 16 * 10)
    nx = size[0]
    ny = size[1]
    prepare_data(data, size)

    fig = plt.figure()
    first_frame = np.reshape(data[0:nx * ny], size)
    im = plt.imshow(first_frame, vmin=0, vmax=100, cmap='inferno', interpolation='hamming')
    frames = int(len(data) / (nx * ny))

    n = len(data)
    index = 0
    count = 1
    while (index < n):
        cut_data = data[index:(size[0] * size[1]) * count]
        index += size[0] * size[1]
        count += 1
        show_heatmap_single_frame(cut_data, size=size, vmin=0, vmax=100)
        plt.show()




if __name__ == "__main__":
    size = (32, 24)
    original_data = np.random.randint(0, 100, size=32*24*16*10)
    data = np.random.randint(0, 100, size=32*24*16*10)
    # show_heatmap_video(data, size=size, vmin=0, vmax=100, frequency=16.0)
    # print(len(data)/(size[0]*size[1]))
    heatmap_video(data, size, 0, 100, 16.0, 1)
    # test()
