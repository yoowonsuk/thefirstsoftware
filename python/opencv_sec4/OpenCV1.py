import cv2
import datetime

cap = cv2.VideoCapture(0) # -1
#cap = cv2.VideoCapture('taylor.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('Register.avi', fourcc, 20.0, (640,480))  #fourcc.org
print("frame Width before setting", cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 3
print("frame Height before setting", cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 4

#while(True):
while(cap.isOpened()):
    ret,frame = cap.read()
    output.write(frame)
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    if ret == Ture:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width : "+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+" Height : "+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        dT = datetime.datetime.now()
        frame = cv2.putText(frame, text, (10,20),  font, 1, (0,0,255), 2, cv2.LINE_AA)
        #frame = cv2.putText(frame, dT, (10,20),  font, 1, (0,0,255), 2, cv2.LINE_AA)

        #gray = cv2.cvtColor(frame, cv2_COLOR_BGR2GRAY)
        cv2.imshow("Video Frame", frame)
        #cv2.imshow("Video Frame", gray)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
output.release()
cv2.destroyAllWindows()


# shift F10 > pycharm Run shortcut
