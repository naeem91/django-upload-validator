import os
from setuptools import setup


with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-upload-validator',
    version='1.0',
    packages=['upload_validator'],
    description='A simple Django file type validator using python-magic',
    long_description=README,
    author='Mckinsey Academy',
    author_email='dev@mckinseyacademy.com',
    url='https://github.com/mckinseyacademy/django-upload-validator',
    license='MIT',
    install_requires=[
        'python-magic'
    ]
)
