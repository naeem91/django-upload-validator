import os
from ddt import ddt, data

from django.test import TestCase

from upload_validator import FileTypeValidator


TEST_FILES_DIR = os.path.join(os.path.dirname(__file__), 'test_files')


TEST_FILES = [
    # word
    'word-mac.doc', 'word-mac.docx', 'word-windows.docx', 'word-ubuntu.doc', 'word-ubuntu.docx',
    # excel
    'excel-mac.xls', 'excel-mac.xlsx', 'excel-windows.xlsx', 'excel-ubuntu.xls', 'excel-ubuntu.xlsx', 'document.xlsx',
    # power point
    'sample.ppt', 'sample.pptx',
    # pdf
    'sample.pdf',
    # images
    'sample.png', 'sample.jpeg', 'sample.tif',
]


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

    @data(*TEST_FILES)
    def test_valid_types(self, filename):
        """
        Tests that different files are detected correctly
        """
        validator = FileTypeValidator(
            allowed_types=[
                'application/msword',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                'application/pdf',
                'application/vnd.ms-powerpoint',
                'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                'application/vnd.ms-excel',
                'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
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
            allowed_types=[
                'application/msword',
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            ],
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
