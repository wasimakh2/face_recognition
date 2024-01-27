import face_recognition
from PIL import Image, ImageDraw
import face_recognition

# Load the image file into a numpy array using face_recognition library
image = face_recognition.load_image_file("two_people.jpg")

# Find all facial features in all the faces in the image using face_recognition library
facial_features = face_recognition.face_land_landmarks(image)
image = face_recognition.load_image_file("two_people.jpg")

# Find all facial features in all the faces in the image
face_landmarks_list = face_recognition.face_landmarks(image)

facial_features

# Create a PIL imagedraw object to draw facial features on the image
facial_features_image = Image.fromarray(image)
facial_features_draw = ImageDraw.Draw(facial_features_image)
pil_image = Image.fromarray(image)
d = ImageDraw.Draw(pil_image)

for face_landmarks in face_landmarks_list:

    # Print the location of each facial feature in this image
    for facial_feature in face_landmarks.keys():
        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    # Let's trace out each facial feature in the image with a line!
    for facial_feature in face_landmarks.keys():
        d.line(face_landmarks[facial_feature], width=5)

# Show the picture
facial_features_image.show()
