#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import re
import os
import os.path
import random
import numpy as np


class APL():
    def __init__(self):
        self.data = {}
        self.ss = set()
        self.aa = set()

    def load(self, path="./apl"):
        if os.path.isdir(path):
            size = 360
            dx = 360 / size
            for _, _, fnames in os.walk(path):
                for f in fnames:
                    sp = f.split('_')
                    self.aa.add(sp[0])
                    self.ss.add(sp[1])
                    key = (sp[0], sp[1])
                    self.data[key] = np.zeros((size, size))

                    p = path + "/" + f

                    if ".swp" not in p:
                        with open(p) as f:
                            for line in f.readlines():
                                line = line.rstrip('\r\n')
                                tokens = re.sub("\s+", " ", line).split(' ')

                                phi = float(tokens[0])
                                psi = float(tokens[1])
                                p = float(tokens[2])

                                x = round((phi + 180) / dx)
                                y = round((psi + 180) / dx)

                                self.data[key][x, y] = p
                        break

        else:
            if path == "":
                raise Exception("path is empty, please use keyword path to point to the file")
            else:
                raise Exception("Could not find: %s" % path)

    def print(self):
        k = (random.sample(self.aa, 1)[0], random.sample(self.ss, 1)[0])

        for x in range(0, 360):
            for y in range(0, 360):
                print(x - 180, y - 180, self.data[k][x, y])

            print()


if __name__ == "__main__":
    apl = APL()
    apl.load()

    # apl.print()
