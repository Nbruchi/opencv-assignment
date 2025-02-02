import cv2

image = cv2.imread('resized_lena.jpg')

flipped_image = cv2.flip(image, 0)

cv2.imshow('Flipped Image', flipped_image)

cv2.waitKey(0)

cv2.imwrite('lena_flipped.jpg', flipped_image)

cv2.destroyAllWindows()