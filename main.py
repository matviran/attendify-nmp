# Importing Modules
import os
import pickle
import numpy
import cv2
import cvzone
import face_recognition

# Adding Video Capture Method and Window Size
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Importing Background
imgBackground = cv2.imread('Resources/background.png')

# Importing Mode Images to list
folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

# Loading Encoding File
print('Loading the Encoded File')
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print('Encode File Loaded')

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# Calling the Video Capture Window
while True:
    success, img = cap.read()

    imgS = cv2.resize(img , (0, 0) , None , 0.25 , 0.25 )
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    imgBackground[162 : 162 + 480 , 55 : 55 + 640] = img
    imgBackground[44:44 + 633 , 808:808 + 414] = imgModeList[3]

    # Looping through the Encodings
    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        print("matches", matches)
        print("faceDis", faceDis)

        matchIndex = numpy.argmin(faceDis)
        print('MatchIndex', matchIndex)

        if matches[matchIndex]:
            print('Known Face Detected')
            print(studentIds[matchIndex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4 , x2*4 , y2*4 , x1*4
            bbox = 55+x1, 162+y1, x2-x1, y2-y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)

            # cv2.rectangle(imgBackground, pt1=y1*4, pt2=x1*4, color='black')

    # Opening the Face Attendance GUI
    cv2.imshow("Attendify - No More Proxy!", imgBackground)
    cv2.waitKey(1)