import cv2 as cv
import numpy as np

image=cv.imread("./21456.jpg",cv.IMREAD_GRAYSCALE)
kernnel =cv.imread("./filter.png",cv.IMREAD_GRAYSCALE)

##ทำไงก็ได้ให้ sum เเล้วได้ 1
## โดยการใช้สูตร n/sum
## 
n = kernnel.sum()
kernnel = kernnel/n

image = cv.filter2D(src=image, ddepth=-1, kernel=kernnel)

cv.imwrite("./ANC.png",image)