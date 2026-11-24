import cv2
import numpy as np

image1 = cv2.imread("image1.jpg")
image2 = cv2.imread("image2.jpg")

image1 = cv2.resize(image1 , (400,400))
image2 = cv2.resize(image2 , (400,400))

blended1 = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)
blended2 = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
blended3 = cv2.addWeighted(image1, 0.2, image2, 0.8, 0)

cv2.imshow('Blended Image 1 (0.7, 0.3)', blended1)
cv2.imshow('Blended Image 2 (0.5, 0.5)', blended2)
cv2.imshow('Blended Image 3 (0.2, 0.8)', blended3)

cv2.waitKey(0)
cv2.destroyAllWindows()