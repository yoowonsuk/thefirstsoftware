# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import cv2

video = cv2.VideoCapture("video.mp4")
success, frame = video.read()

height = frame.shape[0]
width = frame.shape[1]

face_cascade = cv2.CascadeClassifier('faces.xml')
output = cv2.VideoWriter('output.avi', 
        cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height)) # MAC VLC program

count = 0
while success:
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 4)
    output.write(frame)
    success, frame = video.read()
    count += 1
    print(count)

output.release()

'''
import cv2

image = cv2.imread('humans.jpen', 1)
face_cascade = cv2.CascadeClassifier('faces.xml')

faces = face_cascade.detectMultiScale(image, 1.1, 4)
print(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), 4)

cv2.imwrite('human_faces.jpeg', image)

import cv2

video = cv2.videoCapture('video.mp4')
success, frame = video.read()

count = 1
while success:
    cv2.imwrite(f'images/{count}.jpg', frame)
    success, frame = video.read()
    count += 1
'''

