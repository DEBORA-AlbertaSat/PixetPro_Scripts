#! /usr/bin/env python
import pypixet

# initialize pixet
pypixet.start()

# get pixet API
pixet = pypixet.pixet


# print pixet version
print(pixet.pixetVersion())


# other commands .....


# de initialize pixet
pypixet.exit()



