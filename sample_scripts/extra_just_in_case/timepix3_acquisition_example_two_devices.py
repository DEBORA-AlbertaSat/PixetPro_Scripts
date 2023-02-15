#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# Copyright (C) 2018 Daniel Turecek
#
# @file      tpx3_two_acqt.py
# @author    Daniel Turecek <daniel@turecek.de>
# @date      2018-07-25
import time
import thread

dev1 = pixet.devicesByType(pixet.PX_DEVTYPE_TPX3)[0]
dev2 = pixet.devicesByType(pixet.PX_DEVTYPE_TPX3)[1]

# set Timepix3 operation mode:
dev1.setOperationMode(pixet.PX_TPX3_OPM_TOATOT)
dev2.setOperationMode(pixet.PX_TPX3_OPM_TOATOT)
#dev1.setOperationMode(pixet.PX_TPX3_OPM_EVENT_ITOT)
#dev1.setOperationMode(pixet.PX_TPX3_OPM_TOA)
#dev1.setOperationMode(pixet.PX_TPX3_OPM_TOT_NOTOA)


def acqThread1():
    # make data driven acquisition for 5 seconds and save to file:
    dev1.doAdvancedAcquisition(1, 1, pixet.PX_ACQTYPE_DATADRIVEN, pixet.PX_ACQMODE_NORMAL, pixet.PX_FTYPE_AUTODETECT, 0, "/tmp/test1.t3pa")
    print("Finished 1")

def acqThread2():
    # make data driven acquisition for 5 seconds and save to file:
    dev2.doAdvancedAcquisition(1, 1, pixet.PX_ACQTYPE_DATADRIVEN, pixet.PX_ACQMODE_NORMAL, pixet.PX_FTYPE_AUTODETECT, 0, "/tmp/test2.t3pa")
    print("Finished 2")

thread.start_new_thread(acqThread1, ())
thread.start_new_thread(acqThread2, ())

