import cv2

video = cv2.VideoCapture("video.mp4")

width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)) #1080
nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT) # 90 (3 sec)
fps = video.get(cv2.CAR_PROP_FRS) # 30
print(width) # 1920.0
