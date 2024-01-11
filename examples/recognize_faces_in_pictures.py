import face_recognition


"""Load jpg files and compare faces."""

# Load the jpg files into numpy arrays
biden_image = face_recognition.load_image_file("biden.jpg")
obama_image = face_recognition.load_image_file("obama.jpg")
unknown_image = face_recognition.load_image_file("obama2.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
def load_and_compare_faces():
    """Load jpg files and compare faces."""
    try:
        biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
        obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
        unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
    except IndexError:
        print("Error: No faces detected in the images. Aborting...")
        quit()
    except Exception as e:
        print("An error occurred while processing the images. Aborting...")
        quit()
    known_faces = [
        biden_face_encoding,
        obama_face_encoding
    ]
    results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
    print(f"Is the unknown face a picture of Biden? {results[0]}")
    print(f"Is the unknown face a picture of Obama? {results[1]}")
    print(f"Is the unknown face a new person that we've never seen before? {not True in results}")

"""Load jpg files and compare faces."""
try:
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError as e:
    print("Error: No faces detected in the images. Aborting...")
    quit()

known_faces = [
    biden_face_encoding,
    obama_face_encoding
]

# Compare the faces to detect matches
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print(f"Is the unknown face a picture of Biden? {results[0]}")
print(f"Is the unknown face a picture of Obama? {results[1]}")
print(f"Is the unknown face a new person that we've never seen before? {not True in results}")
