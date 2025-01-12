import cv2

image = cv2.imread('lena.jpg')

cv2.imshow('Image', image)

cv2.waitKey(0)

cv2.imwrite('lena.png', image)

cv2.imwrite('lena.bmp', image)

cv2.destroyAllWindows()
