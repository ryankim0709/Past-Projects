import numpy as np

info = input()
info = info.split()

height = float(info[0])
radius = float(info[1])

volume = np.pi * radius * radius * height
print(round(volume, 2),"cubic inches")