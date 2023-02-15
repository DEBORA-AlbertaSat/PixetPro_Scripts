"""
This script shows example how to control the clustering plugin from python.

Clustering module functions:

start(idev)
stop(idev)
isRunning(idev)
replayData(idev, filePath)
clearData(idev)
saveFrames(idev, frameIdex, filePath, flags)    # flags=1 save as spectrum, flags=0 save frames
setLogOKClusterLogFile(idev, clusterLogFilePath)
setLogAllClusterLogFile(idev, clusterLogFilePath)
setLogBadClusterLogFile(idev, clusterLogFilePath)

"""

import pyclustering

# get pointer to devcontrol object
clustering = pixet.plugin("clustering").privateInterface()

# replay data with clustering from first device:
dev = pixet.devices()[0]
clustering.setLogAllClusterLogFile(dev.asIDev(), "/tmp/output.clog")
#clustering.setLogOKClusterLogFile(dev.asIDev(), "/tmp/output.clog")
#clustering.setLogBadClusterLogFile(dev.asIDev(), "/tmp/output.clog")

#clustering.replayData(dev.asIDev(), "/tmp/data.t3pa")
#clustering.replayData(dev.asIDev(), "/tmp/data.t3r")
clustering.replayData(dev.asIDev(), "/tmp/somefile.clog")

