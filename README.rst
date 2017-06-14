***********************
Django Upload Validator
***********************

Django Upload Validator is a simple utility for validating file types and extensions using `python-magic` library.

Installation
############

Install the `current PyPI release <https://pypi.python.org/pypi/django-upload-validator>`__:

.. code:: bash

    pip install django-upload-validator

Usage
#####
General usage
::

    from upload_validator import FileTypeValidator

    validator = FileTypeValidator(
        allowed_types=['application/msword'],
        allowed_extensions=['.doc', '.docx']
    )

    file_resource = open('sample.doc')

    # ValidationError will be raised in case of invalid type or extension
    validator(file_resource)

Usage as a FileField validator in Django forms
::

    from upload_validator import FileTypeValidator

     profile_image = forms.FileField(
        label='', help_text="Formats accepted: JPEG nd PNG", required=False,
        validators=[FileTypeValidator(
            allowed_types=[ 'image/jpeg','image/png']
        )]
    )


Running Tests
#############
#. Install testing requirements :code:`pip install -r tests/requirements.txt`
#. Run :code:`python runtests.py` inside the root directory of package
