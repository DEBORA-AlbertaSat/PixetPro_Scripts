import pypxproc
import traceback
import time
dev = pixet.devices()[0]

def messageCb(error, msg):
    print("Message: {}, error={}".format(error, msg))

def progressCb(finished, progress):
    print("Progress: {}, finished={}".format(progress, finished))



s = pypxproc.SpectraImaging()
s.messageCallback = messageCb
s.progressCallback = progressCb

# Replay data
rc = s.replayData("somdata.t3pa", "", True)
print("Rc={}".format(rc))


# Start Measurement
measTime = 2
acqTime = 0.5
outFile = ""
processData=True
#rc = s.startMeasurement(acqTime, measTime, outFile, processData)
#print("Rc={}".format(rc))
#s.abort()

rc = s.loadCalibrationFromDevice()
print("Load calib from device {}".format(rc))


#rc = s.loadCalibrationFromFiles("test.xml")
#rc = s.loadCalibrationFromFiles("test.a|test.b|test.c|test.t")
#print("Load calib from device {}".format(rc))

rc = s.saveToFile("meas.bcfg")
print("Save to file rc={}".format(rc))
rc = s.loadFromFile("meas.bcfg")
print("Load from file rc={}".format(rc))

while s.isRunning():
    print("ProcessedPixPerSecond {}".format(s.processedPixelsPerSecond()))
    print("MeasuredPixPerSecond {}".format(s.measuredPixelsPerSecond()))
    time.sleep(0.3)


filePath="/tmp/sum.pmf"
zoom=1
correction=False
rc = s.saveSumFrame(filePath,zoom,correction)
print("Save sum frame rc={}".format(rc))

filePath="/tmp/frames.pmf"
oneFile=True
rc = s.saveDataAsFramesToFile(filePath,oneFile)
print("Save data as frames rc={}".format(rc))

filePath="/tmp/spect.txt"
rc = s.saveDataAsSpectrumToFile(filePath)
print("Save data as spectrum rc={}".format(rc))

enIndex = 1
sumFrame = True
normalize = False
zoom = 1
rc, frame = s.getFrameForEnergy(enIndex, sumFrame, normalize, zoom)
print("Get Frame for Energy rc={}, len={}".format(rc, len(frame)))


enFrom = 1
enTo = 10
normalize = False
rc, frame = s.getFrameForEnergyRange(enFrom, enTo, normalize)
print("Get Frame for Energy range rc={}, len={}".format(rc, len(frame)))


rc, spect, step = s.getGlobalSpectrum()
print("Get global spectrum rc={}, len={}, step={}".format(rc, len(spect), step))

rc, spect, step = s.getGlobalSpectrumInRect(10, 10, 100, 100)
print("Get global spectrum in rect rc={}, len={}, step={}".format(rc, len(spect), step))


