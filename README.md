[![PyPI version](https://badge.fury.io/py/pycord.svg)](https://badge.fury.io/py/pycord)

# Pycord - A tiny python wrapper on top of FFMpeg

**Pycord** is a simple python wrapper on top of ffmpeg 
designed to load videos into numpy ndarrays quickly and easily.

You can use **Pycord** in place of more complex video loader as [OpenCV](https://pypi.org/project/opencv-python/) 
or [Decord](https://pypi.org/project/decord/) in your Computer Vision or Machine Learning projects.

## Example
```python
from pycord.video_reader import VideoReader

vr = VideoReader("video.mp4")

b = vr.get_batch([5, 8])
```

## Documentation
There's no documentation at the moment, take a look to the tests to find some examples of use.

## Contributing
The main idea of this project is to provide a decord-like interface 
completely written in python (hance the name **pycord**, a **py**thon implementation of de**cord**).

Any contribution is welcome as long as it is implemented in pure python.

## I'm looking for something faster...

If you think **pycord** is slow, and you don't mind to deal directly with some low-level code, 
take a look to my other project [iterframes](https://github.com/alesanfra/iterframes)!
It's a python module implemented in [Rust](https://www.rust-lang.org) with the aim to be as fast as possible.
