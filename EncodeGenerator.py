# Importing Modules
import os
import cv2
import face_recognition
import pickle


# Importing Student Images
folderPath = 'Images'
modePathList = os.listdir(folderPath)
imgList = []

for path in modePathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))