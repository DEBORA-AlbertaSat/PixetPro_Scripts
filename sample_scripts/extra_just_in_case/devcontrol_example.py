"""
This scripts show example how to control the main window from python script (showing the frame in the windows,
simulating clicking on start/stop button, changing acquisition parameters, ...)
Each device has seperate window and therefore fist parameter of the functions is the idev object of the device (device.asIDev())

Device Control functions:

showFrame(idev, frame)
setOutputFile(idev, fileName, outputEnabled)
setAcqParams(idev, acqCount, acqTime)
setAcqType(idev, acqType)
setRepeat(idev, repeatCount, repeatEnabled)
start(idev)
stop(idev)
isRunning(idev)
setColorMap(idev, index)
setRange(idev, min, max)
setWindowAll(idev, checked)
setCurrentSubFrame(idev, index)
setAcqMode(idev, mode)

"""

import pydevcontrol

# get pointer to devcontrol object
devctrl = pixet.plugin("devcontrol").privateInterface()

# load some frame from disk and show it in first device preview window:
dev = pixet.devices()[0]
frame = pixet.dataMgr().loadFrame("/tmp/frame.pmf", 0);
devctrl.showFrame(dev.asIDev(), frame)
frame.destroy()

# change acquisition parameters in main window - acqCount=100, acqTime=0.5 s:
devctrl.setAcqParams(dev.asIDev(), 100, 0.5)

# simulate clicking on start button on main window:
devctrl.start(dev.asIDev())

# simulate clicking on stop button on main window:
devctrl.stop(dev.asIDev())



