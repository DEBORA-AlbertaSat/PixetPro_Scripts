#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright (C) 2015 Daniel Turecek
#
# @file      t3p_to_t3pa.py
# @author    Daniel Turecek <daniel@turecek.de>
# @date      2015-12-03
import struct
import sys


def convertFile(fileName, outputFile):
    # struct_unpack = struct.Struct("<IIBBH").unpack_from # old file
    struct_unpack = struct.Struct("<IQBBH").unpack_from  # new file
    out = open(outputFile, "w")
    out.write("Index\tMatrix Index\tToA\tToT\tFToA\tOverflow\n")
    index = 0
    with open(fileName, "rb") as f:
        while True:
            pixelraw = f.read(16)
            if len(pixelraw) < 16:
                break
            if not pixelraw:
                break
            pixeldata = struct_unpack(pixelraw)
            out.write("%d\t%d\t%d\t%d\t%d\t%d\n" % (index, pixeldata[0], pixeldata[1], pixeldata[4], pixeldata[3], pixeldata[2]))
            index += 1
    out.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: t3p_to_t3pa.py filename.t3p output.t3pa")
        sys.exit(0)
    fileName = sys.argv[1]
    outputFile = sys.argv[2]
    convertFile(fileName, outputFile)
