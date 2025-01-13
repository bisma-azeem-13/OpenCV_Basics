import os
import cv2 as cv
import numpy as np
from PIL import Image

# List of people
people = ['Elizabeth Olsen', 'Henry Cavill', 'Louis Partridge', 'Millie Bobby Brown', 'Scarlett Jonhsson']
print(people)

DIR = r'C:\Users\hp\Desktop\Train'
haar_cascade = cv.CascadeClassifier("haar_face.xml")

# Create training set
features = []  # img arrays of faces
labels = []  # corresponding label

def create_train_set():
    for person in people:
        path = os.path.join(DIR, person)  # getting folder path of each person
        label = people.index(person)

        # Rename images with a sequential counter based on folder name
        image_count = 1
        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            # Convert .jfif to .jpeg if necessary
            if img.endswith(".jfif"):
                try:
                    img_pil = Image.open(img_path)
                    new_name = f"{person}-{image_count}.jpeg"  # Use folder name
                    new_path = os.path.join(path, new_name)
                    img_pil.save(new_path, "JPEG")
                    img_path = new_path  # Update img_path to use the renamed JPEG
                except Exception as e:
                    print(f"Error converting {img_path}: {e}")
                    continue

            img_array = cv.imread(img_path)  # reading img
            if img_array is None:
                print(f"Error reading {img_path}")
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]  # region of interest so crop out the face
                features.append(faces_roi)  # appending the features
                labels.append(label)

            image_count += 1

create_train_set()
print("Training Done---")

features = np.array(features, dtype='object')
labels = np.array(labels)
#2. Face recognizer
#instatiating 
face_recognizer = cv.face.LBPHFaceRecognizer_create() 

#training on features list and labels
face_recognizer.train(features, labels)

#saving trained models and dataset
face_recognizer.save("face_trained.yml")
np.save("features.py", features)
np.save("labels.py",labels)