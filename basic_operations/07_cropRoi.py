import cv2

image = cv2.imread('lena.jpg')

cropped_image = image[750:1500, 750:1500]

cv2.imshow('Cropped Image', cropped_image)

cv2.waitKey(0)

cv2.imwrite('lena_cropped.jpg', cropped_image)

cv2.destroyAllWindows()