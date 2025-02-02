import cv2

image = cv2.imread('resized_lena.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Gray Image', gray_image)

cv2.waitKey(0)

cv2.imwrite('lena_gray.jpg', gray_image)

cv2.destroyAllWindows()