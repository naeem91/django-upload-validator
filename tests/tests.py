import os
from ddt import ddt, data

from django.test import TestCase

from upload_validator import FileTypeValidator


TEST_FILES_DIR = os.path.join(os.path.dirname(__file__), 'test_files')


@ddt
class TestFileValidator(TestCase):
    def test_initialization(self):
        """
        Tests initialization of validator class
        """
        validator = FileTypeValidator(
            allowed_types=['image/jpeg']
        )

        self.assertTrue(isinstance(validator, FileTypeValidator))

    @data('sample.doc', 'sample.pdf', 'sample.docx', 'sample.pptx', 'sample.ppt',
          'sample.tif', 'sample.jpeg', 'sample.png')
    def test_valid_types(self, filename):
        """
        Tests that different files are detected correctly
        """
        validator = FileTypeValidator(
            allowed_types=[
                'application/msword',
                'application/pdf',
                'application/vnd.ms-powerpoint',
                'image/tiff',
                'image/jpeg',
                'image/png'
            ]
        )

        file_path = os.path.join(TEST_FILES_DIR, filename)

        file_obj = open(file_path)
        validator(file_obj)
        file_obj.close()

    def test_invalid_content(self):
        """
        Checks where extension is valid but file content is invalid
        """
        validator = FileTypeValidator(
            allowed_types=['image/jpeg']
        )

        file_with_wrong_content = os.path.join(TEST_FILES_DIR, 'wrong_jpg.jpeg')

        try:
            validator(open(file_with_wrong_content))
        except Exception as e:
            code = e.code
        else:
            code = None

        self.assertEqual(code, 'invalid_type')

    def test_extension_check(self):
        """
        Checks case where file has valid type but extension is not allowed
        """
        validator = FileTypeValidator(
            allowed_types=['application/msword'],
            allowed_extensions=['.doc', '.docx']
        )

        test_file = os.path.join(TEST_FILES_DIR, 'sample.docm')

        try:
            validator(open(test_file))
        except Exception as e:
            code = e.code
        else:
            code = None

        self.assertEqual(code, 'invalid_extension')
