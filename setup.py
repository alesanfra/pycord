from setuptools import setup

setup(
    name='pycord',
    packages=['pycord'],
    version='0.0.1',
    description='Convenient wrapper on FFmpeg',
    author='Alessio Sanfratello',
    url='https://github.com/kkroening/ffmpeg-python',
    # download_url=download_url,
    install_requires=[
        'ffmpeg-python',
        'numpy'
    ],
)
