import thread
import time

# gets the first connected device:
dev = pixet.devices()[0]

# function that is running the acquisition in separate thread:
def acqthread():
    acqCount = 5
    acqTime = 0.1
    # starts acquisition in frame mode and software triggering
    rc = dev.doAdvancedAcquisition(acqCount, acqTime, pixet.PX_ACQTYPE_FRAMES, pixet.PX_ACQMODE_TRG_SWSTART, 0, 0, "")
    print("Acq: %d" % rc)

# start the acquisition function
thread.start_new_thread(acqthread, ())

# send 5 times the software trigger
for i in range(5):
    # just some delay
    time.sleep(1)

    # check that the device is ready to accept triger
    while dev.isReadyForSoftwareTrigger(0) == False:
        time.sleep(0.001)

    # so the trigger
    rc = dev.doSoftwareTrigger(0)
    print("Trigger: %d" % rc)



#dev.abortOperation()

