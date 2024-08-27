from setuptools import setup, find_packages

setup(
    name='CSV cleaner',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pandas==2.1.4',
        'click==8.1.7',
        'pytest==7.4.0',
    ],
    entry_points={
        'console_scripts': [
            'cleaner=src.main:main',
        ],
    },
)