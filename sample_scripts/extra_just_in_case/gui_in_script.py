import os
import pygui

#scriptDir = os.path.dirname(__file__) # gets the directory where this script is located
#window = pygui.loadFromUiFile(scriptDir + "/test.ui")
#window.show()
#l=window.gridLayout

def onButton():
    print("button")

window = pygui.MainWindow()



label=window.Label("Test")
label2=window.Label("Test")
button=window.Button("TestButton")
fr=window.MpxFrame()
w=window.Widget()
gb=window.GroupBox()
gb.setTitle("Test groupbox")

glayout = window.newGridLayout()
glayout.addWidget(label, 0, 0, 1, 1)
gb.setLayout(glayout)

wlayout = window.newGridLayout()
wlayout.addWidget(fr, 0, 0, 1, 1)
w.setLayout(wlayout)


l = window.newGridLayout()
l.addWidget(gb, 0, 0, 1, 1)
l.addWidget(w, 1, 0, 1, 1)
l.addWidget(button, 0, 1, 1, 1)
l.addWidget(label2, 2, 0, 2, 2)
window.setLayout(l)
window.show()

button.clicked=onButton