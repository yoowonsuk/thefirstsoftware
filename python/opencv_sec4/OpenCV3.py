import cv2 
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("HS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("HV", "Tracking", 0, 255, nothing)
while(True):
    frame = cv2.imread('objects.png', 1)
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    #l_r = np.array([0,120,70])
    #u_r = np.array([10,255,255])
    
    mask = cv2.inRange(hsv_image,l_r,u_r)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('FrameBGR', frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    
    key = cv2.waitKey(0)
    if key == 27:
        break
cv2.destroyAllWindows()
