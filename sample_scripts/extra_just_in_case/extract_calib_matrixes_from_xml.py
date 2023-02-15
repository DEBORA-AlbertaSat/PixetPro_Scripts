#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright (C) 2016 Daniel Turecek
#
# @file      extract_calib_from_xml.py
# @author    Daniel Turecek <daniel@turecek.de>
# @date      2016-03-18
import sys
import os
import glob
import base64
import struct

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def writeMatrix(fileName, data):
    f = open(fileName, "w")
    for i, x in enumerate(data):
        f.write("%f " % x)
        if (i + 1) % 256 == 0:
            f.write("\n")
    f.close()

def extractCalibs(fileName):
    tree = ET.ElementTree(file=fileName)
    root = tree.getroot()

    # get chip ID:
    chipid = ""
    theitem = ""
    for item in root:
        if "-W" in item.tag:
            chipid = item.tag
            theitem = item
            break

    if not chipid:
        sys.exit("invalid xml file.")

    caliba = theitem.find("caliba").text
    calibb = theitem.find("calibb").text
    calibc = theitem.find("calibc").text
    calibt = theitem.find("calibt").text

    caliba = base64.b64decode(caliba)
    caliba = struct.unpack('d' * (len(caliba) / 8), caliba)
    calibb = base64.b64decode(calibb)
    calibb = struct.unpack('d' * (len(calibb) / 8), calibb)
    calibc = base64.b64decode(calibc)
    calibc = struct.unpack('d' * (len(calibc) / 8), calibc)
    calibt = base64.b64decode(calibt)
    calibt = struct.unpack('d' * (len(calibt) / 8), calibt)

    writeMatrix("caliba.txt", caliba)
    writeMatrix("calibb.txt", calibb)
    writeMatrix("calibc.txt", calibc)
    writeMatrix("calibt.txt", calibt)

if len(sys.argv) < 2:
    print("Usage script.py FITPix-J07-W0167.xml")
    sys.exit(0)
extractCalibs(sys.argv[1])

