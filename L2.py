import cv2
import numpy as np

image = cv2.imread("pika.png")
cv2.imshow("original img", image)

kernel = np.ones((5,5) , np.uint8)
eroded = cv2.erode(image , kernel , iterations=1)

cv2.imshow("Eroded Image", eroded)

blurred = cv2.blur(image , (5, 5))
cv2.imshow("Blurred Image", blurred)

gaussian_blurred = cv2.GaussianBlur(image , (5, 5), 2)
cv2.imshow("gaussian Blurred Image", gaussian_blurred)

resize = cv2.resize(image, (300,300))
cv2.imshow("Resized Image", resize)


border1 = cv2.copyMakeBorder(image ,20,20,30,30, cv2.BORDER_CONSTANT ,value = [200,0,100])
cv2.imshow("Border Image", border1)


border2 = cv2.copyMakeBorder(image ,20,20,30,30, cv2.BORDER_REPLICATE ,value = [200,0,100])
cv2.imshow("Border2 Image", border2)

border3 = cv2.copyMakeBorder(image ,20,20,30,30, cv2.BORDER_REFLECT ,value = [200,0,100])
cv2.imshow("Border3 Image", border3)


border4 = cv2.copyMakeBorder(image ,20,20,30,30, cv2.BORDER_WRAP ,value = [200,0,100])
cv2.imshow("Border4 Image", border4)


cv2.waitKey(0)
cv2.destroyAllWindows()