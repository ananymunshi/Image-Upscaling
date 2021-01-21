import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('room.png',1)
img1 = [
		(0.5,1,0,0.13),
		(0.4,0.6,1,0.7),
		(0.77,0,0.87,0.62),
		(0.32,0.54,0.99,0.2)
		]
plt.imshow(img1, cmap = 'gray', interpolation = 'spline36')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()