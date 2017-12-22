"""
This is a file to descrive the Python module distribution and
helps with installation.

More info on various arguments here:
https://docs.python.org/2.7/distutils/setupscript.html
"""
from setuptools import setup


setup(
    name='template',
    version='0.0.1',
    description='This is a template',
    url='https://github.com/uc-cdis/template-repo',
    license='Apache',
    packages=[
        'template-repo',
    ],
)
