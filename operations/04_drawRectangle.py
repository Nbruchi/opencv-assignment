import cv2

image = cv2.imread('lena.jpg')

cv2.rectangle(image, (750, 750), (1500, 1500), (0, 255, 0), 8)

cv2.imshow('Rectangle', image)

cv2.waitKey(0)

cv2.imwrite('lena_rectangle.jpg', image)

cv2.destroyAllWindows()