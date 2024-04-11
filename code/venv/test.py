import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Beispiel Daten: Ein 1D-Array von 768 Werten für ein Bild
image_data = np.random.rand(768*20)

# Anzahl der Frames pro Sekunde (FPS) und die Anzahl der Frames insgesamt
fps = 2  # Bilder pro Sekunde
total_frames = 20  # Gesamtzahl der Frames

# Anzahl der Werte, die bei jedem Update aktualisiert werden sollen
update_count = 32 * 24  # Anzahl der Pixel in einem Bild

# Ihre Animationsfunktion
def update(frame):
    start_index = frame * update_count
    end_index = min((frame + 1) * update_count, len(image_data))
    updated_values = image_data[start_index:end_index]
    heatmap_data = np.zeros((24, 32))
    heatmap_data.flat[:len(updated_values)] = updated_values
    im.set_array(updated_values.T)
    return im,

# Erstellen Sie Ihre Figure und Axes
fig, ax = plt.subplots()
im = ax.imshow(np.zeros((24, 32)), cmap='hot')  # Erstellen Sie eine initiale Heatmap

# Ihre FuncAnimation erstellen
ani = FuncAnimation(fig, update, frames=range(total_frames), interval=10)  # Berechnung der Frame-Dauer

plt.show()