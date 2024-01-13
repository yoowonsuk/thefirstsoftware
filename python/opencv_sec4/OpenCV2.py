import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def mouse_events(event, x, y, flags, params):

    if event==cv2.EVENT_LBUTTONDOWN:
        text="The Left Mouse Button is clicked"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text,(x,y),font,0.5,(0,255,0), 2)  
        cv2.imshow('Lena', img)

    if event==cv2.EVENT_RBUTTONDOWN:
        text="The Right Mouse Button is clicked"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text,(x,y),font,0.5,(0,0,255), 2)  
        cv2.imshow('Lena', img)

    if event==cv2.EVENT_RBUTTONDBLCLK:
        #text="The Right Mouse Button is clicked 2 Times"
        text="X"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text,(x,y),font,0.5,(0,0,255), 2)  
        cv2.imshow('Lena', img)

img = cv2.imread('lena.png', 1)
_, th1 = cv2.threshold(img, 127, 255,cv2.THRESH_BINARY)   # return => _
#_, th1 = cv2.threshold(img, 127, 255,cv2.THRESH_BINARY_INV)   # return => _
#cv2.imshow('Lena', img)
cv2.imshow('Gradient Image', img)
cv2.imshow('Threshold1', th1)

#cv2.setMouseCallback('Lena', mouse_events) # same image name 'Lena'
cv2.waitKey(0)
cv2.destroyAllWindows()
