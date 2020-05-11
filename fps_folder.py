import os

import fps as fps_mod


def main(path, fps, speed):
    dname = os.path.dirname(path)
    ext = os.path.splitext(path)[1]
    for f in os.listdir(dname):
        if not f.endswith(ext):
            continue
        fpath = os.path.join(dname, f)
        fps_mod.main(fpath, fps, speed)


if __name__ == "__main__":
    main(**fps_mod.collect_args())