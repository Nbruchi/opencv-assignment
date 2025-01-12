import cv2
import numpy as np

image = cv2.imread('resized_lena.jpg')

b, g, r = cv2.split(image)

blue_channel = cv2.merge((b,np.zeros_like(b),np.zeros_like(b)))
green_channel = cv2.merge((np.zeros_like(g),g,np.zeros_like(g)))
red_channel = cv2.merge((np.zeros_like(r),np.zeros_like(r),r))

slides =[
    ("Blue Channel(Colorize)", blue_channel),
    ("Green Channel(Colorize)", green_channel),
    ("Red Channel(Colorize)", red_channel)
]

slide_duration = 2000

for title,img in slides:
    cv2.imshow(title, img)
    cv2.waitKey(slide_duration)

merged_image = cv2.merge((b,g,r))
cv2.imshow('Merged Image(Swapped)', merged_image)

cv2.waitKey(0)

cv2.destroyAllWindows()