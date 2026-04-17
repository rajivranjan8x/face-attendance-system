import face_recognition
import os
import pickle

path = 'dataset'

images = []
classNames = []

for file in os.listdir(path):
    img = face_recognition.load_image_file(f'{path}/{file}')
    images.append(img)
    classNames.append(os.path.splitext(file)[0])

encodeList = []

for img in images:
    encodings = face_recognition.face_encodings(img)
    if encodings:
        encodeList.append(encodings[0])

with open("encodings.pkl", "wb") as f:
    pickle.dump((encodeList, classNames), f)

print("Encoding Complete ✅")