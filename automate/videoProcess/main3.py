# pip3.9 install opencv-python
import cv2

video = cv2.VideoCapture(0)
success, frame = video.read()

height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml')
output = cv2.VideoWriter('output.avi', 
        #cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height)) # MAC VLC program
        cv2.VideoWriter_fourcc(*'DIVX'), 15, (width, height)) # webcam frame

count = 0
while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 4)
    '''
    # Live
    cv2.inshow("Recording", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    '''
    output.write(frame)
    success, frame = video.read()
    count += 1
    print(count)

output.release()
video.release()
cv2.destroyAllWindows()
