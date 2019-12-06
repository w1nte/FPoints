#!/usr/bin/env python2

import glob
import re
import os


def read_points(file):
    if os.path.isfile(file):
        with open(file, "r") as f:
            s = re.search(r"Punkte gesamt: ?(\d+)", f.read(), re.IGNORECASE)
            return int(s.group(1)) if s else 0
    return 0


if __name__ == '__main__':
    results = glob.glob("*.out")
    filename = re.compile("(.*)(_1\.out)")

    tasks = map(lambda f: filename.search(f).group(1), filter(filename.match, results))
    points = map(lambda f: (read_points(f + "_1.out") + read_points(f + "_2.out")) / (2 if os.path.isfile(f + "_2.out")
                                                                                      else 1), tasks)

    print(str(sum(points)) + " / 500")