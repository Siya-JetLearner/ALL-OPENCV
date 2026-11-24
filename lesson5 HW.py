
import cv2
import numpy as np


# 1. DRAWING A LINE

img = cv2.imread("road.png")
height, width = img.shape[:2]
cv2.line(img, (0, 0), (width, height), (0, 0, 255), 5)
cv2.imshow("Drawing a Line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# 2. DRAWING MULTIPLE LINES

img = cv2.imread("road.png")
height, width = img.shape[:2]
centre_x = width // 2
centre_y = height // 2
cv2.line(img, (0, centre_y), (width, centre_y), (255, 0, 0), 3)
cv2.line(img, (centre_x, 0), (centre_x, height), (0, 255, 0), 3)
cv2.imshow("Multiple Lines", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# 3. RECTANGLE BORDER

img = cv2.imread("box.png")
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)
cv2.imshow("Rectangle Border", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 4. TRAFFIC SIGNAL


img = np.ones((500, 300, 3), dtype=np.uint8) * 255
cv2.rectangle(img, (75, 30), (225, 470), (0, 0, 0), -1)
cv2.circle(img, (150, 110), 55, (0, 0, 255), -1)
cv2.circle(img, (150, 250), 55, (0, 255, 255), -1)
cv2.circle(img, (150, 390), 55, (0, 255, 0), -1)
cv2.imshow("Traffic Signal", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



# 5. BOUNDING BOX WITH LABEL

img = cv2.imread("person.png")
cv2.rectangle(img, (50, 50), (250, 300), (0, 255, 0), 3)
cv2.rectangle(img, (50, 20), (150, 50), (0, 255, 0), -1)
cv2.putText(img, "Person", (55, 43),cv2.FONT_HERSHEY_SIMPLEX, 0.7,(0, 0, 0), 2)
cv2.imshow("Bounding Box with Label", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
