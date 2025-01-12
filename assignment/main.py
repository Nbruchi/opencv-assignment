import cv2

image = cv2.imread("assignment-001-given.jpg")
cv2.rectangle(image, (260, 200), (990, 920), (0, 255, 0), 8)

rect_image = image.copy()
cv2.rectangle(rect_image, (800, 100), (1100, 195), (0, 0, 0), -1)
image = cv2.addWeighted(rect_image, 0.5, image, 0.5, 0)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "RAH972U", (810, 165), font, 2, (0, 255, 0), 4)

cv2.imshow("Assignment",image)

cv2.waitKey(0)
cv2.imwrite("assignment-001-result.jpg",image)
cv2.destroyAllWindows()