import cv2

image = cv2.imread('lena.jpg')

cv2.rectangle(image, (750, 750), (1500, 1500), (0, 255, 0), 8)
cv2.circle(image, (1125, 1125), 375, (0, 255, 0), 8)

cv2.imshow('Rectangle and Circle', image)

cv2.waitKey(0)

cv2.imwrite('lena_shapes.jpg', image)

cv2.destroyAllWindows()