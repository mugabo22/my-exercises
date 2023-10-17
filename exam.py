import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter as gf

load=plt.imread("imgs/image.jpg")
blured=gf(load)

plt.subplot(121)
plt.imshow(load)
plt.title("Original image")

plt.subplot(122)
plt.imshow(blured)
plt.title("Blured image")



plt.show()