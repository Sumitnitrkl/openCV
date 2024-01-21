import numpy as np
import cv2

# Specify the dimensions of the image
width, height = 840, 680

# Create a white image
white_image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Specify the path to save the image
save_path = r'C:\Users\Sumit Kumar\Desktop\opencv\pure_white_image.png'

# Save the image with the specified path
cv2.imwrite(save_path, white_image)

# Optionally, display the image
cv2.imshow('Pure White Image', white_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
