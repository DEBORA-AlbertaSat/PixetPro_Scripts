#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright (C) 2016 Daniel Turecek
#
# @file      convert_t3r_t3pa.py
# @author    Daniel Turecek <daniel@turecek.de>
# @date      2016-05-10
import sys
import traceback
from tpx3luts import *

def bytes_from_file(filename, chunksize=8192):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                for b in chunk:
                    yield ord(b)
            else:
                break

def processFile(inputFile, outputFile, colShiftNum, itot):
    colshifttbl = LUT_COLSHIFTS[colShiftNum]

    it = bytes_from_file(inputFile).__iter__()
    pixelIndexInFile = 0
    try:
        f = open(outputFile, "w")
        f.write("Index\tMatrix Index\tToA\tToT\tFToA\tOverflow\n")
        cnt = 0
        for b in it:
            cnt += 1
            # skip dummy data until packet
            while (b & 0xF0) != 0xB0:
                for i in range(4):
                    b = it.next()
                    cnt += 1

            data = [b, it.next(), it.next(), it.next(), it.next(), it.next(), it.next(), it.next()]
            cnt += 7
            print(" ".join("%02X" % x for x in data), cnt)
            address = (data[0] & 0x0F) << 12 | (data[1] << 4) | ((data[2] >> 4) & 0x0F)
            toa = ((data[2] & 0x0F) << 10) | (data[3] << 2) | ((data[4] >> 6) & 0x03)
            tot = ((data[4] & 0x3F) << 4) | ((data[5] >> 4) & 0x0F)
            ftoa = (data[5] & 0x0F)
            eoc = (address >> 9) & 0x7F
            sp = (address >> 3) & 0x3F
            pix = address & 0x07
            x = eoc * 2 + (pix / 4)
            y = (sp * 4 + (pix % 4))
            idx = y * 256 + x

            if itot:
                toa = LUT_ITOT[toa] if toa >= 1 and toa < MAX_LUT_ITOT else WRONG_LUT_ITOT
                ftoa = LUT_EVENT[ftoa] if ftoa >= 1 and ftoa < MAX_LUT_EVENT else WRONG_LUT_EVENT
            else:
                toa = LUT_TOA[toa] if toa >= 0 and toa < MAX_LUT_TOA else WRONG_LUT_TOA
                ftoa = (ftoa + colshifttbl[x])
            tot = LUT_TOT[tot] if tot >= 1 and tot < MAX_LUT_TOT else WRONG_LUT_TOT
            totalToa = (data[6] << 22) + (data[7] << 14) + toa

            f.write("%d\t%d\t%d\t%d\t%d\t%d\n" % (pixelIndexInFile, idx, totalToa, tot, ftoa, 0))
            pixelIndexInFile += 1

        f.close()
    except:
        traceback.print_exc()
    return 0

processFile(sys.argv[1], sys.argv[2], 4, False)
