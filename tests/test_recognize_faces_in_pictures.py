import unittest

import face_recognition
from examples.recognize_faces_in_pictures import recognize_faces_in_pictures


class TestRecognizeFacesInPictures(unittest.TestCase):
    def test_recognize_faces_with_faces(self):
        # Load test image with faces
        test_image = face_recognition.load_image_file("path/to/test_image_with_faces.jpg")

        # Get face encodings for test image
        face_encodings = face_recognition.face_encodings(test_image)

        # Create list of known face encodings
        known_face_encodings = face_encodings

        # Call recognize_faces_in_pictures function
        result = recognize_faces_in_pictures(test_image, known_face_encodings)

        # Assert result matches expected output
        self.assertEqual(result, "Expected output for test image with faces")

    def test_recognize_faces_without_faces(self):
        # Load test image without faces
        test_image = face_recognition.load_image_file("path/to/test_image_without_faces.jpg")

        # Call recognize_faces_in_pictures function
        result = recognize_faces_in_pictures(test_image, [])

        # Assert result matches expected output
        self.assertEqual(result, "Expected output for test image without faces")

    # Add additional test methods as needed

if __name__ == "__main__":
    unittest.main()
