***********************
Django Upload Validator
***********************
.. image:: https://circleci.com/gh/naeem91/django-upload-validator/tree/master.svg?style=svg
    :target: https://circleci.com/gh/naeem91/django-upload-validator/tree/master


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

Wildcard character specification is also supported. e.g; for accepting only images:
::

    profile_image = forms.FileField(
        label='', help_text="Only image formats are accepted.", required=False,
        validators=[FileTypeValidator(
            allowed_types=[ 'image/*']
        )]
    )


Running Tests
#############
#. Install testing requirements :code:`pip install -r tests/requirements.txt`
#. Run :code:`python runtests.py` inside the root directory of package
