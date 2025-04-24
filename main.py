import cv2
import os

# Set proxy at runtime
os.environ['HTTP_PROXY'] = 'http://edcguest:edcguest@172.31.100.25:3128'
os.environ['HTTPS_PROXY'] = 'http://edcguest:edcguest@172.31.100.25:3128'

thres = 0.45  # Threshold to detect object

# Load class names
classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# Load model
configPath = 'ssd_mobilenet.pbtxt'
weightsPath = 'frozen_inference.pb'


net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Start webcam
cap = cv2.VideoCapture(0)  # Use 1 if you have an external cam
cap.set(3, 1280)
cap.set(4, 720)
cap.set(10, 70)

# Run detection loop
while True:
    success, img = cap.read()
    classIds, confs, bbox = net.detect(img, confThreshold=thres)
    print(classIds, bbox)

    if len(classIds) != 0:
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):

            # Check to avoid index error
            if classId < len(classNames):
                label = classNames[classId-1].upper()
            else:
                label = f"{classId}: {classNames[classId-1].upper()}"  # fallback label

            cv2.rectangle(img, box, color=(0, 255, 0), thickness=2)
            cv2.putText(img, label, (box[0]+10, box[1]+30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(img, f'{round(confidence * 100, 2)}%',
                    (box[0]+10, box[1]+60),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)


    cv2.imshow('Output', img)
    cv2.waitKey(1)

print("Server is running")