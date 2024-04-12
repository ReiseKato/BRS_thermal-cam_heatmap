import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import seaborn as sns
from scipy.ndimage import gaussian_filter
import numpy as np
import os

'''seaborn'''

size = (32, 24)
orig_data0 = np.random.randint(0, 100, size=32*24*16*10)
orig_data1 = np.random.randint(0, 100, size=32*24*16*10)

# gauss_data0 = gaussian_filter(data0, sigma=1)
# gauss_data1 = gaussian_filter(data1, sigma=1)

# fig, (ax0, ax1) = plt.subplots(1, 2, sharey=True)

# sns.heatmap(np.reshape(gauss_data0, size), vmin=0, vmax=100, cmap='inferno', square=True, ax=ax0)
# sns.heatmap(np.reshape(gauss_data1, size), vmin=0, vmax=100, cmap='inferno', square=True, ax=ax1)
# plt.show()

'''save animation'''
def save_anim(anim, filename):
    dir_list = os.listdir()
    filename = "heatmap_seaborn"
    filename_type = filename + ".mp4"
    filename_index = 0
    while filename_type in dir_list:
        filename += str(filename_index)
        filename_type = filename + ".mp4"
        filename_index += 1
    filename += ".mp4"
    writer = animation.FFMpegWriter(fps=frequency)
    anim.save(filename, writer=writer)

'''make solution matrices from existing data'''
def get_solution_matrices(data:np.array, size:(int,int)):
    def slice_data(data: np.array, size: (int, int)):
        n = len(data)
        cut = n % (size[0] * size[1])
        return data[0:n - cut]
    data = slice_data(data, size)
    frames = int(len(data) / (size[0] * size[1]))

    solution_matrix = np.array(data[0:size[0]*size[1]])
    counter = 1
    for i in range(frames):
        solution_matrix = np.vstack((solution_matrix, data[size[0]*size[1]*counter:size[0]*size[1]*(counter+1)]))
    return solution_matrix

    '''animation seaborn heatmap'''
def seaborn_animation(data:np.array, size:(int, int), vmin:float, vmax:float, frequency:float):
    nx = size[0]
    ny = size[1]
    counter = 1

    n = len(data)
    cut = n%(size[0]*size[1])
    frames = int(len(data[0:n - cut]) / (nx * ny)) - 1

    solution_matrix = get_solution_matrices(data, size)

    gauss_data = gaussian_filter(solution_matrix[0], sigma=1)
    fig = plt.figure()
    hm = sns.heatmap(np.reshape(gauss_data, size), vmin=0, vmax=100, cmap='inferno', square=True, cbar=False)
    #mesh = hm.collections[0]
    #sns.heatmap(np.reshape(gauss_data, size), vmin=0, vmax=100, cmap='inferno', square=True, cbar=False)

    def init():
        sns.heatmap(np.zeros(size))

    def animate(i):
        nonlocal counter
        hm = sns.heatmap(np.reshape(gaussian_filter(solution_matrix_global[counter], sigma=1), size), vmin=0, vmax=100, cmap='inferno', square=True, cbar=False)
        counter += 1
        print(counter)
        return hm

    anim = animation.FuncAnimation(fig, animate, frames=frames, interval=1.0/frequency, repeat=False)
    plt.show()




'''subplot animation'''

def heatmap_video_subplot(data0: np.array, data1: np.array, size: (int, int), vmin: float, vmax: float, frequency: float):
    nx = size[0]
    ny = size[1]
    counter = 1

    n = len(data0)
    cut = n % (size[0] * size[1])
    gauss_data0 = gaussian_filter(data0[0:nx*ny], sigma=1)
    gauss_data1 = gaussian_filter(data1[0:nx*ny], sigma=1)

    fig, (ax0, ax1) = plt.subplots(1, 2, sharey=True)

    sns.heatmap(np.reshape(gauss_data0, size), vmin=0, vmax=100, cmap='inferno', square=True, ax=ax0)
    sns.heatmap(np.reshape(gauss_data1, size), vmin=0, vmax=100, cmap='inferno', square=True, ax=ax1)
    frames = int(len(data0[0:n-cut])/(nx*ny)) - 1

    def init():
        sns.heatmap(np.zeros(size), ax=ax0)
        sns.heatmap(np.zeros(size), ax=ax1)

    def animate(data: np.array):
        nonlocal counter
        start_index = nx * ny * counter
        end_index = min(nx * ny * (counter + 1), len(orig_data0))
        adj_data0 = np.reshape(orig_data0[start_index:end_index], size)
        adj_data1 = np.reshape(orig_data1[start_index:end_index], size)
        sns.heatmap(adj_data0, vmin=0, vmax=100, cmap='inferno', square=True, ax=ax0)
        sns.heatmap(adj_data1, vmin=0, vmax=100, cmap='inferno', square=True, ax=ax1)
        counter += 1
        #return im

    def animate2(data: np.array):
        data = np.random.randint(0, 100, size=32 * 24)
        adj_data = np.reshape(data, size)
        im.set_data(adj_data)
        return im

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=1.0/frequency, repeat=False)
    plt.show()

def test2():
    # Beispiel Daten für die Heatmap
    data_1 = np.random.rand(10, 10)
    data_2 = np.random.rand(10, 10)

    # Erstellen der Heatmap mit Seaborn
    fig, (ax1, ax2) = plt.subplots(1, 2)
    heatmap1 = sns.heatmap(data_1, cmap='inferno', cbar=False, ax=ax1)
    heatmap2 = sns.heatmap(data_2, cmap='inferno', cbar=False, ax=ax2)
    heatmaps = [heatmap1, heatmap2]

    # Ihre Animationsfunktion
    def update(frame):
        # Hier können Sie die Daten für die Heatmap aktualisieren
        new_data1 = np.random.rand(10, 10)
        new_data2 = np.random.rand(10, 10)
        ax1.clear()
        ax2.clear()
        heatmap1 = sns.heatmap(new_data1, cmap='inferno', cbar=False, ax=ax1)
        heatmap2 = sns.heatmap(new_data2, cmap='inferno', cbar=False, ax=ax2)
        heatmaps = [heatmap1, heatmap2]
        return heatmaps

    # Ihre FuncAnimation erstellen
    ani = FuncAnimation(fig, update, frames=10, interval=200)

    plt.show()

test2()
#solution_matrix_global = get_solution_matrices(orig_data0, size)
#seaborn_animation(orig_data0, size, 0, 100, 16.0)
#print(len(solution_matrix[7]))





