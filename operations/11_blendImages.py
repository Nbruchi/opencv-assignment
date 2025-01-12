import cv2

fish = cv2.imread('fish.png')
pig = cv2.imread('pig.png')

blended = cv2.addWeighted(fish, 0.5, pig, 0.5, 0)

cv2.imshow('Blended', blended)

cv2.waitKey(0)

cv2.imwrite('pish.png', blended)

cv2.destroyAllWindows()