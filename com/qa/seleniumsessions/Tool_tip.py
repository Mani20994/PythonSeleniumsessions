import sys
from PySide import QtGui,QtCore

app = QtGui.QApplication(sys.argv)
btn = QtGui.QPushButton("Mouse hover here")
btn.setToolTi("This is our tool")
btn.show()
app.exec_()
