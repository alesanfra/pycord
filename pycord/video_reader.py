import ffmpeg
import numpy


class VideoReader:
    def __init__(self, uri):
        probe = ffmpeg.probe(uri)
        video_info = next(s for s in probe['streams'] if s['codec_type'] == 'video')
        self.width = int(video_info['width'])
        self.height = int(video_info['height'])
        self.num_frames = int(video_info['nb_frames'])
        self.stream = ffmpeg.input(uri)

    def __len__(self):
        return self.num_frames

    def __getitem__(self, frame):
        return self.get_batch([frame])

    def get_batch(self, indices):
        """Get a batch of frames in one call

        :param indices:
        :return:
        """
        select_string = "+".join(f"eq(n,{i})" for i in indices)

        out, err = self.stream \
            .filter_('select', select_string) \
            .output('pipe:', format='rawvideo', pix_fmt='rgb24', vsync=0) \
            .run(capture_stdout=True, capture_stderr=True)

        return numpy.frombuffer(out, numpy.uint8).reshape([len(indices), self.height, self.width, 3])

    def get_range(self, start, end):
        """Get a range of frames

        :param start:
        :param end:
        :return:
        """
        if start > self.num_frames:
            raise ValueError("start outside video")

        if end > self.num_frames:
            raise ValueError("end ouside video")

        count = end - start
        if count < 1:
            raise ValueError("start must be < end")

        out, err = self.stream \
            .filter_('select', 'gte(n,{})'.format(start)) \
            .output('pipe:', format='rawvideo', pix_fmt='rgb24', vframes=count) \
            .run(capture_stdout=True, capture_stderr=True)

        return numpy.frombuffer(out, numpy.uint8).reshape([count, self.height, self.width, 3])
