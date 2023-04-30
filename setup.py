from setuptools import setup, find_packages

setup(
    name='dlsub',
    version='1.0.0',
    description='A command line tool for downloading transcripts of YouTube videos',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/dlsub',
    packages=find_packages(),
    install_requires=[
        'youtube_transcript_api'
    ],
    entry_points={
        'console_scripts': [
            'dlsub=dlsub.main:main'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
