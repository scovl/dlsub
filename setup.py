from setuptools import setup, find_packages

setup(
    name='dlsub',
    version='0.0.1',
    description='A tool for downloading and processing YouTube video transcripts.',
    author='Vitor Lobo Ramos',
    author_email='lobocode@gmail.com',
    url='https://github.com/lobocode/dlsub',
    packages=find_packages(),
    install_requires=[
        'enelvo==0.15',
        'pychatsonic==0.1',
        'setuptools==44.1.1',
        'spacy==3.5.2',
        'tqdm==4.65.0',
        'youtube_transcript_api==0.6.0',
    ],
    entry_points={
        'console_scripts': [
            'dlsub=dlsub:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
