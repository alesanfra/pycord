"""Convenient wrapper on top of FFMpeg"""

__version__ = "0.1.1"

import multiprocessing as _mp

_mp.set_start_method("spawn")


def _decode(queue: _mp.Queue):
    queue.put("hi")


def read(timeout: float = 10.0):
    queue = _mp.Queue()

    process = _mp.Process(target=_decode, args=(queue,))
    process.start()

    while True:
        frame = queue.get(block=True, timeout=timeout)
        if frame is None:
            break
        yield frame

    process.join()
