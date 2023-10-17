import matplotlib.pyplot as plt
from scipy.ndimage import gaussianfilter as gf

load=plt("imgs,image.jpg")
blured=gf(load)

plt.subplot(121)
plt.imread(load)
plt.title("Original image")

plt.subplot(122)
plt.imread(blured)
plt.title("Blured image")

plt.show()