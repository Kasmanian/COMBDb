import json
import os
import sys
import shutil

from database import Database

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
# from PySide6.QtCore import QObject, QUrl
# from PySide6.QtQuick import QQuickView


# class Page(QQuickView):
#     def __init__(self, qmlFile, app, adb: Database):
#         super(Page, self).__init__()
#         self.app = app
#         self.adb = adb
#         self.setResizeMode(QQuickView.SizeRootObjectToView)
#         qmlSource = os.path.join(os.path.dirname(__file__), qmlFile)
#         self.setSource(QUrl.fromLocalFile(os.path.abspath(qmlSource)))
#         for child in self.children():
#             childName = child.objectName()
#             setattr(self, childName, child)

#     def QUERY_ARGS(self, argNames):
#         args = []
#         for name in argNames:
#             arg = getattr(self, name)
#             args.append(arg.text or arg.toPlainText() or arg)
#         return args


class Indexer():
    def __init__(self, adb: Database, qwargs: dict, fields: list):
        self.adb = adb
        self.qwargs = qwargs
        self.fields = fields
        self.update()


    def update(self):
        self.payload = self.adb.select(**self.qwargs)
        self.indexes = {}
        for i in range(0, len(self.payload)):
            row = self.payload[i]
            for field in self.fields:
                if i<1:
                    self.indexes[field][row[field]] = [i]
                else:
                    self.indexes[field][row[field]].append(i)


    def subset(self, field: str, value: any):
        subset = []
        for index in self.indexes[field][value]:
            subset.append(self.payload[index])
        return subset


    def recast(self, inField: str, value: any, outField: str):
        return self.indexes[inField][value][0][outField]
    

# def create_demo(resetOnCall=False):
#     cwd = os.getcwd()
#     demoFilePath = cwd+r'\COMBDb\demo\COMBDb.accdb'
#     if resetOnCall or not os.path.isfile(demoFilePath):
#         shutil.copyfile(cwd+r'\COMBDb\COMBDb.accdb', demoFilePath)
#     else:
#         print('Loading previously initialized demo...')
#     return demoFilePath

def validate_json(pathToJson: str):
    """Validates if .json exists or creates one."""
    try:
        with open(pathToJson, "x") as j:
            json.dump({}, j)
    except:
        pass

def write_to_json(pathToJson: str, keysToUnpack: list, val):
    """Writes to a .json file."""
    data = None
    with open(pathToJson, "r") as j:
        data = json.load(j)
    temp = data
    for i in range(0, len(keysToUnpack)-1):
        key = keysToUnpack[i]
        if key not in temp[key]:
            temp[key] = {}
        temp = temp[key]
    temp[keysToUnpack[-1]] = val
    with open(pathToJson, "w") as j:
        json.dump(data, j)


def read_from_json(pathToJson: str, keysToUnpack: list):
    """Reads from a .json file"""
    with open(pathToJson, "r") as j:
        data = json.load(j)
        for key in keysToUnpack:
            if key not in data:
                return None
            data = data[key]
        return data
