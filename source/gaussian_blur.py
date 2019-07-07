import numpy as np
import cv2
import os

image_path= "/home/nvidiacuda/test1.png"
print(os.path.exists(image_path))

img = cv2.imread(image_path,1)
# print(img)
# print(type(img))
cv2.imshow('test', img)
cv2.waitKey(0)
