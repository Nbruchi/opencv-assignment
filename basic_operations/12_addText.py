import cv2

image = cv2.imread('lena.jpg')

cv2.putText(image, 'Lena, the famous!', (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 6, (0, 255, 0), 20)

cv2.imshow('Text', image)

cv2.waitKey(0)

cv2.imwrite('lena_text.jpg', image)

cv2.destroyAllWindows()