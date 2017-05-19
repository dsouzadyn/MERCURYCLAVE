from setuptools import setup

setup(
    name='MERCURYCLAVE',
    version='0.1',
    py_modules=['MERCURYCLAVE', 'utils'],
    entry_points='''
        [console_scripts]
        MERCURYCLAVE=MERCURYCLAVE:main
    ''',
)
