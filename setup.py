from setuptools import setup
import sys


if not sys.version_info[0] == 2:
    sys.exit("Sorry, Python 3 is not supported (yet)")

setup(
    name='MERCURYCLAVE',
    version='0.1',
    py_modules=['MERCURYCLAVE', 'utils'],
    entry_points='''
        [console_scripts]
        MERCURYCLAVE=MERCURYCLAVE:main
    ''',
)
