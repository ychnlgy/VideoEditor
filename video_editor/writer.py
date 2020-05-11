import cv2
import numpy


class Writer:

    def __init__(self, fpath, fps):
        self._fpath = fpath
        self._fps = fps

    def rewrite(self, reader):
        out = cv2.VideoWriter(self._fpath, cv2.VideoWriter_fourcc(*'JPEG'), self._fps, reader.size)
        skip = reader.fps//self._fps
        assert skip > 0, "Output FPS %d should be an integer factor smaller than input FPS of %d!" % (self._fps, reader.fps)
        for i, frame in enumerate(reader):
            if not i % skip:
                out.write(frame)
        out.release()