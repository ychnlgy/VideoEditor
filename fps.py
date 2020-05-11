import argparse
import os

import video_editor


def main(path, fps, speed):
    output_dname = os.path.join(os.path.dirname(path), "%s" % fps)
    output_fname = os.path.basename(path)
    output_aname = os.path.join(output_dname, output_fname)
    if not os.path.isdir(output_dname):
        os.makedirs(output_dname)

    writer = video_editor.Writer(output_aname, fps)
    reader = video_editor.Reader(path, speed)

    writer.rewrite(reader)


def collect_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True)
    parser.add_argument("--fps", type=int, default=30)
    parser.add_argument("--speed", type=int)
    return vars(parser.parse_args())


if __name__ == "__main__":
    main(**collect_args())