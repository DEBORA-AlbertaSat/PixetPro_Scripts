"""
This script shows how to manipulate the meta data for MpxFrame object.

"""
DT_CHAR     = 0
DT_BYTE     = 1
DT_I16      = 2
DT_U16      = 3
DT_I32      = 4
DT_U32      = 5
DT_I64      = 6
DT_U64      = 7
DT_FLOAT    = 8
DT_DOUBLE   = 9
DT_BOOL     = 10
DT_STRING   = 11


def addMetaData(fr):
    """ example of adding meta data to frame"""

    print(fr.addMetaData("Test1", "Desc1", DT_CHAR, "c"))
    print(fr.addMetaData("Test2", "Desc2", DT_BYTE, 13))
    print(fr.addMetaData("Test3", "Desc3", DT_I16, -123))
    print(fr.addMetaData("Test4", "Desc4", DT_I32, -1023))
    print(fr.addMetaData("Test5", "Desc5", DT_U32, 1023))
    print(fr.addMetaData("Test6", "Desc6", DT_U64, 10023))
    print(fr.addMetaData("Test7", "Desc7", DT_FLOAT, -10023.13))
    print(fr.addMetaData("Test8", "Desc8", DT_DOUBLE, -100123.13))
    print(fr.addMetaData("Test9", "Desc9", DT_STRING, "Test string"))

    print(fr.addMetaData("Testx1", "Desc1", DT_CHAR, "Test char"))
    print(fr.addMetaData("Testx2", "Desc2", DT_BYTE, [13, 14]))
    print(fr.addMetaData("Testx3", "Desc3", DT_I16, [-123, -124]))
    print(fr.addMetaData("Testx4", "Desc4", DT_I32, [-1023, -1024]))
    print(fr.addMetaData("Testx5", "Desc5", DT_U32, [1023, 1024]))
    print(fr.addMetaData("Testx6", "Desc6", DT_U64, [1000023, 1000024]))
    print(fr.addMetaData("Testx7", "Desc7", DT_FLOAT, [-10023.13, 13.3]))
    print(fr.addMetaData("Testx8", "Desc8", DT_DOUBLE, [-100123.13, 15.6]))

    print(fr.metaData("Test1").data())
    print(fr.metaData("Test2").data())
    print(fr.metaData("Test3").data())
    print(fr.metaData("Test4").data())
    print(fr.metaData("Test5").data())
    print(fr.metaData("Test6").data())
    print(fr.metaData("Test7").data())
    print(fr.metaData("Test8").data())
    print(fr.metaData("Test9").data())
    print(fr.metaData("Testx1").data())
    print(fr.metaData("Testx2").data())
    print(fr.metaData("Testx3").data())
    print(fr.metaData("Testx4").data())
    print(fr.metaData("Testx5").data())
    print(fr.metaData("Testx6").data())
    print(fr.metaData("Testx7").data())
    print(fr.metaData("Testx8").data())


# example of adding meta data when new frame is measured:

def beforeSaveEvent(data):
    addMetaData(data)
    print(data)


# register event before saving data (frame) and do one acquisition
# unregisterr event in the end
dev = pixet.devices()[0]
dev.registerBeforeSaveDataEvent(beforeSaveEvent, beforeSaveEvent)
dev.doSimpleAcquisition(1, 0.1, 1, "/tmp/test.pmf")
fr = dev.lastAcqFrameRefInc()
dev.unregisterBeforeSaveDataEvent(beforeSaveEvent, beforeSaveEvent)

