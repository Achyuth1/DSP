import cv2
import numpy as np

img = cv2.imread('char1_2.png',0)
img = img/256
print(img)