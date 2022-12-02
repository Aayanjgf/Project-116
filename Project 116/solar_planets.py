import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Sun", (20,300), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Mercury", (105,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Venus", (190,170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Earth", (290,260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Mars", (390,170), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Jupiter", (420,280), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Saturn", (770,130), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Uranus", (970,290), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Neptune", (1100,145), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))

cv2.imshow("output", img)

cv2.imwrite("Solar_systemwithname.jpg", img)

cv2.waitKey(0)





