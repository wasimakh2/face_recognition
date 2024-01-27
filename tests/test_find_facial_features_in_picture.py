import unittest
from unittest import mock

import face_recognition
from examples.find_facial_features_in_picture import \
    find_facial_features_in_picture
from PIL import Image, ImageDraw


class TestFindFacialFeaturesInPicture(unittest.TestCase):
    @mock.patch('face_recognition.load_image_file')
    @mock.patch('face_recognition.face_landmarks')
    @mock.patch('builtins.print')
    @mock.patch('PIL.Image.fromarray')
    @mock.patch('PIL.ImageDraw.Draw')
    def test_find_facial_features_in_picture(self, mock_draw, mock_fromarray, mock_print, mock_face_landmarks, mock_load_image_file):
        # Mock image file
        test_image = Image.new('RGB', (100, 100))

        # Mock return values
        mock_load_image_file.return_value = test_image
        mock_face_landmarks.return_value = {'feature1': [(0, 0), (10, 10)], 'feature2': [(20, 20), (30, 30)]}

        # Call the function under test
        find_facial_features_in_picture("test_image.jpg")

        # Assert the function calls and outputs
        mock_load_image_file.assert_called_once_with("test_image.jpg")
        mock_face_landmarks.assert_called_once_with(test_image)
        mock_print.assert_called_with("I found 1 face(s) in this photograph.")
        mock_fromarray.assert_called_once_with(test_image)
        mock_draw.assert_called_once()

        # Additional assertions for facial features
        mock_draw.return_value.line.assert_any_call([(0, 0), (10, 10)], width=5)
        mock_draw.return_value.line.assert_any_call([(20, 20), (30, 30)], width=5)

if __name__ == '__main__':
    unittest.main()
