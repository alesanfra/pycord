import os

from setuptools import setup

requirements = os.path.abspath(os.path.join(os.path.dirname(__file__), 'requirements.txt'))
install_requires = []

if os.path.isfile(requirements):
    with open(requirements) as f:
        install_requires = f.read().splitlines()

setup(
    name='pycord',
    packages=['pycord'],
    version='0.0.1',
    description='Convenient wrapper on FFmpeg',
    author='Alessio Sanfratello',
    url='https://github.com/alesanfra/pycord',
    # download_url=download_url,
    install_requires=install_requires
)
