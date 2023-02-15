import _thread as thread
import time

acqCount = 30
dev = pixet.devices()[0]

def acqthread():
    rc = dev.doAdvancedAcquisition(acqCount, 0.01, pixet.PX_ACQTYPE_FRAMES, pixet.PX_ACQMODE_TRG_SWSTART, 0, 0, "")
    print("Acq: %d" % rc)

print(dev.isReadyForSoftwareTrigger(0))
thread.start_new_thread(acqthread, ())
startTime = time.time()
for i in range(acqCount):
    time.sleep(0.001)
    if i % 5 == 0:
        time.sleep(0.5)
    while dev.isReadyForSoftwareTrigger(0) == False:
        time.sleep(0.001)

    rc = dev.doSoftwareTrigger(0)
    print("Trigger: %d" % rc)

endTime = time.time()
diffTime = endTime - startTime
fps = acqCount / diffTime
print("TIme: {}, Fps: {}".format(diffTime, fps))

#dev.abortOperation()

