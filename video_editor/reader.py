import os

import cv2
import tqdm


class Reader:

    def __init__(self, fpath, speed):
        self.name = os.path.basename(fpath)
        self.speed = speed
        self._cap = cv2.VideoCapture(fpath)

        self.fps = int(round(self._cap.get(cv2.CAP_PROP_FPS)))
        self.size = (
            int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        )
        self.frames = int(self._cap.get(cv2.CAP_PROP_FRAME_COUNT))

    def __iter__(self):
        for i in tqdm.tqdm(range(self.frames), desc=self.name, ncols=80):
            ret, frame = self._cap.read()
            if ret:
                if not i % self.speed:
                    yield frame
            else:
                break
        self._cap.release()