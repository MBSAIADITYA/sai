import cv2
import numpy as np

# Let's load a simple image with 3 black squares
image = cv2.imread('black.jpg')
image = cv2.resize(image,(800,800))
cv2.imwrite("black.jpg",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
