from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Table(QAbstractTableModel) :

    def __init__(self, parent, headers) :
        QAbstractTableModel.__init__(self, parent) 
        ## Data structure is bound by the shape of the headers:
        # Rows x #colums of headers 
        self.headers = headers
        # values
        self.values = [] 

    def update(self, new_data) :
        self.beginResetModel()
        self.values = new_data
        self.endResetModel()

    def rowCount(self, index) :
        return len(self.values)

    def columnCount(self, index) :
        return len(self.headers)

    def setData(self, index, role=Qt.DisplayRole) :
        # i override this with nothing because by default qt lets you edit
        pass ## FOR NOW-later can implement ability to change data

    def data(self, index, role=Qt.DisplayRole) :
        if role == Qt.DisplayRole :
            r = index.row()
            c = index.column()
            return self.values[r][c]

    def headerData(self, section, orientation, role=Qt.DisplayRole) :
        if orientation == Qt.Horizontal and role == Qt.DisplayRole :
            return self.headers[section] 
        # otherwise return the default
        return QAbstractTableModel.headerData(self, section, orientation, role)

    # flags for editing
    def flags(self, index) :
        fl = QAbstractTableModel.flags(self, index)
        return fl 
