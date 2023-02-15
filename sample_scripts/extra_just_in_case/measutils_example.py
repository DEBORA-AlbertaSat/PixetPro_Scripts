"""
This scripts shows example how to control Measuremetn utils plugin from python.

Meas utils functions:

siStart(idev, acqTime, measTime, outputFilePath, processData)
siStop(idev)
siIsRunning(idev)
siReplayData(idev, filePath, outputFilePath)
siSaveFrames(idev, filePath, int flags)
siSaveSumFrame(idev, filePath, zoomFactor, correction)
siSaveSpectra(idev, filePath)
siSetParameters(idev, spectraFrom, spectraTo, binCount, subPixFactor, correction)
siSetMaskNoisyPixels(idev, mask)

"""
import pymeasutils
import time

idev = pixet.devices()[0].asIDev()
mu = pixet.plugin("measutils").privateInterface()
print(mu)

# sets spectra from = 0, to 300, bin count = 300, subpixel factor = 1, correction True:
mu.siSetParameters(idev, 0, 300, 300, 1, True)

# starts the measuremetn and save data to file
mu.siStart(idev, 0.5, 3, "/tmp/test.t3r", False)


# wait till measurement finishes:
isRunning = True

while isRunning:
    isRunning = mu.siIsRunning(idev)
    print(isRunning)
    time.sleep(0.1)
#mu.siStop(idev)

#mu.siSaveSumFrame(idev, "/d/xs/tmpdata/sum.txt", 1, False)
#mu.siSaveSpectra(idev, "/d/xs/tmpdata/spectra.txt")
#mu.siSaveFrames(idev, "/d/xs/tmpdata/frames.pmf", 1) # 0 - multiple files, 1 - frames in single file
