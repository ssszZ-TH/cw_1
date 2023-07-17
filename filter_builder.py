# Python program to explain cv2.line() method 
   
# importing cv2 
import cv2 as cv
import numpy as np
   
image=np.zeros((32,32))


# Start coordinate, here (0, 0)
# represents the top left corner of image
start_point = (0, 10)

# End coordinate, here (250, 250)
# represents the bottom right corner of image
end_point = (20, 30)

# Green color in BGR
color = (255, 255, 255)
  
# Line thickness of 9 px
thickness = 1

# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
image = cv.line(image, start_point, end_point, color, thickness)

# Displaying the image
cv.imwrite("./filter.png",image)