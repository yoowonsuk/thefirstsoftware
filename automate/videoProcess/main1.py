import cv2

video = cv2.VideoCapture("video.mp4")
#print(video)
print(video.read()) # first frame (True, numpy)

success, frame = video.read()
count = 1
while success:
    cv2.imwrite(f'images/{count}.jpg')
    success, frame = video.read()

    count += 1

nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAR_PROP_FPS)

print(nr_frames, fps) # 90.0 30.0

#timestamp = '00:00:02.75'
timestmap = input('Enter timestamp in hh:mm:ss format: ')
timestamp_list = timestamp.split(':')
hh, mm, ss = timestamp_list
timestamp_list_floats = [float(i) for i in timestamp_list_floats]
hours, minutes, seconds = timestamp_list_floats

#print(timestamp_list)

frame_nr = hours * 3600 * fps + minutes * 60 * fps + seconds * fps
video.set(1, frame_nr) # first para is prop(erty)
# https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a8c6d8c2d37505b5ca61ffd4bb54e9a7c
success, frame = video.read()
#cv2.imwrite(f'Frame at {hours}:{minutes}:{seconds}.jpg', frame)
cv2.imwrite(f'Frame at {hh}:{mm}:{ss}.jpg', frame)

