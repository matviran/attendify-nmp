# Importing Modules
import os
import cv2

# Adding Video Capture Method and Window Size
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Importing Background
imgBackground = cv2.imread('Resources/background.png')

# Importing Mode Images to list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModelist = []

for path in modePathList:
    imgModelist.append(cv2.imread(os.path.join(folderModePath, path)))

# Calling the Video Capture Window
while True:
    success, img = cap.read()

    imgBackground[162 : 162 + 480 , 55 : 55 + 640] = img
    imgBackground[44:44 + 633 , 808:808 + 414] = imgModelist[0]

    # Opening the Face Attendance GUI
    cv2.imshow("Attendify - No More Proxy!", imgBackground)
    cv2.waitKey(1)