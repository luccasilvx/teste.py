import cv2
import matplotlib.pyplot as plt
import numpy as np
# print(cv2.__version__) apenas verificar a versão
img = cv2.imread('opencv.jpg', cv2.IMREAD_COLOR)
img = np.array(img,dtype = 'float32', ndims = 4)
# print(type(img))

plt.imshow(img)