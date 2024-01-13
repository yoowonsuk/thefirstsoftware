import cv2

img = cv2.imread('lena.png', 1)
img = cv2.line(img, (0,0), (255,255), (0,255, 0), 5) # B G R (reverse)
img = cv2.arrowedLine(img, (0,255), (2,2), (0,0,255), 10)
img = cv2.rectangle(img, (384,0), (510,128), (0,0,255), 5)
#img = cv2.rectangle(img, (384,0), (510,128), (0,0,255), -1) # filled rectangle
img = cv2.circle(img, (445,62), 62, (0,255,0), 5) # negative will draw filled circle
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "Awesome Image", (10,500), font, 4, (0,0,255), 10, cv2.LINE_AA)
#print(img)
cv2.imshow('image', img)
#cv2.waitKey(5000) # for 5 sec
key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key==ord('s'):
    cv2.imwrite('lena2.png', img)
    cv2.destroyAllWindows()
#cv2.destroyWindow()

