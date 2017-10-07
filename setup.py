from setuptools import setup
import sys

setup(
    name='MERCURYCLAVE',
    version='0.1',
    py_modules=['MERCURYCLAVE', 'utils'],
    entry_points={
        'console_scripts': [
            'mercuryclave = MERCURYCLAVE:main'
        ]
     },
)
