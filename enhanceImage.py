import cv2
import numpy as np
import matplotlib.pyplot as plt 

def sharp_image (pic) : 
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    return cv2.filter2D(pic, -1, kernel) 

pic = cv2.imread("./image/MALMBS.jpg") 
sharp_image = sharp_image(pic)

original_and_sharpened_image = np.hstack((pic, sharp_image))

plt.figure(figsize = [30, 30])
plt.axis('off')
plt.imshow(original_and_sharpened_image[:,:,::-1])
plt.show()

cv2.imwrite("./image/MALMBS_sharpened.jpg", sharp_image)