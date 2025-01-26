import cv2
import os

CASCADE = 'faces.xml'
INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'
COLOR = (255, 255, 255)
WIDTH = 4
SCALE = 1.1
NEIGHTBORS = 4

def has_face(image_path):
    image = cv2.imread(image_path, 1)
    face_cascade = cv2.CascadeClassifier(CASCADE)
    
    faces = face_cascade.detectMultiScale(image, SCALE, NEIGHBORS)# https://deep-learning-study.tistory.com/244
    print(faces)
    
    if len(faces != 0:
        for (x, y, w, h) in faces: #horizontal, vertical, width, height
            cv2.rectangle(image, (x,y), (x+w, y+h), COLOR, WIDTH)
    
    #cv2.imwrite('human_faces.jpeg', image)
        return image


images = os.listdir(INPUT_FOLDER)
for image in images:
    face_image = has_face(f'{INPUT_FOLDER}/{image}')
    if face_image is not None:
        cv2.imwrite(f'{OUTPUT_FOLDER}/{image}', face_image)




image = cv2.imread('humans.jpeg', 1)
face_cascade = cv2.CascadeClassifier('faces.xml')

faces = face_cascade.detectMultiScale(image, 1.1, 4)# https://deep-learning-study.tistory.com/244
print(faces)

for (x, y, w, h) in faces: #horizontal, vertical, width, height
    cv2.rectangle(image, (x,y), (x+w, y+h), (255, 255, 255), 4)

cv2.imwrite('human_faces.jpeg', image)



