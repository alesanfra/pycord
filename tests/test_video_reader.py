"""
Generate test video with the following command
ffmpeg -n -f lavfi -i testsrc=duration=5:size=1280x720:rate=5 -pix_fmt yuv420p -vcodec libx264 data/video.mp4
"""

import os
from unittest import TestCase

from pycord.video_reader import VideoReader


class TestVideoReader(TestCase):
    DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'video.mp4'))

    def test_get_batch(self):
        vr = VideoReader(self.DATA_PATH)

        b = vr.get_batch([5, 8])

        self.assertEqual(b.shape, (2, 720, 1280, 3))

    def test_get_range(self):
        vr = VideoReader(self.DATA_PATH)

        b = vr.get_range(2, 18)

        self.assertEqual(b.shape, (16, 720, 1280, 3))
