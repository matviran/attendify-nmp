from PIL import Image
import face_recognition

known_face_encodings = []
known_face_names = []
with open("book1.csv") as file:
    data = file.readlines()
    for line in data:
        line = line.strip()
        image, name = line.split(',')
        info = face_recognition.load_image_file(image+".jpg")
        face_locations = face_recognition.face_locations(info)
        encoding = face_recognition.face_encodings(info)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(name)
        for face_location in face_locations:
            top, right, bottom, left = face_location
            face_image = info[top:bottom, left:right]
            pil_image = Image.fromarray(face_image)
            pil_image.save(f"images/{image}.jpg")
print(known_face_names)