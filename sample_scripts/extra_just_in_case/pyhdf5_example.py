import pyhdf5

pyhdf5.open("/d/results.h5", False, 0)
print pyhdf5.subItems("/")

print pyhdf5.getItem("/BHTest/Data/Frame_0/AcqTime")
print len(pyhdf5.getItem("/BHTest/Data/Frame_0/Data"))
print pyhdf5.setItem("/Test/temp", 13)
print pyhdf5.setItem("/Test/temp2", [13, 14, 15])
print pyhdf5.setItem("/Test/temp3", [13.1, 14.1, 15.1])
print pyhdf5.setItem("/Test/temp4", "Test")

pyhdf5.close()