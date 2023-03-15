import os
import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import Qt, QObject, QUrl
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QGuiApplication

# if __name__ == '__main__':

#     loader = QUiLoader()
#     app = QApplication(sys.argv)
#     engine = QQmlApplicationEngine('App.qml')
#     # engine.screenLoader.source = 'HomeScreen.ui.qml'
#     window = engine.rootObjects()[0]
#     #window.children()[1].setProperty('source', 'HomeScreen.ui.qml')
#     # [0].findChild(QObject, 'body')
#     print(window.children()[1])
#     #window.show()
#     sys.exit(app.exec())

class LoginScreen(QQuickView):
    def __init__(self, app):
        super(LoginScreen, self).__init__()
        self.app = app
        self.setResizeMode(QQuickView.SizeRootObjectToView)
        qmlFile = os.path.join(os.path.dirname(__file__), 'LoginScreen.ui.qml')
        self.setSource(QUrl.fromLocalFile(os.path.abspath(qmlFile)))
        loginButton = self.findChild(QObject, "loginButton")
        loginButton.clicked.connect(self.successful_login)

    def successful_login(self):
        qmlFile = os.path.join(os.path.dirname(__file__), 'HomeScreen.ui.qml')
        self.setSource(QUrl.fromLocalFile(os.path.abspath(qmlFile)))

class HomeScreen(QQuickView):
    def __init__(self, app):
        super(HomeScreen, self).__init__()
        self.app = app
        self.setResizeMode(QQuickView.SizeRootObjectToView)
        qmlFile = os.path.join(os.path.dirname(__file__), 'HomeScreen.ui.qml')
        self.setSource(QUrl.fromLocalFile(os.path.abspath(qmlFile)))

class Document(QQuickView):
    def __init__(self, app):
        super(Document, self).__init__()
        self.setResizeMode(QQuickView.SizeRootObjectToView)
        self.app = app
        self.loadUI('LoginScreen.ui.qml')

    def loadUI(self, fileName):
        file = os.path.join(os.path.dirname(__file__), fileName)
        self.setSource(QUrl.fromLocalFile(os.path.abspath(file)))

class App(QGuiApplication):
    def __init__(self):
        super(App, self).__init__(sys.argv)
        self.document = LoginScreen(self)
        if self.document.status() == QQuickView.Error:
            sys.exit(-1)
        self.document.showMaximized()
        sys.exit(self.exec())

if __name__ == '__main__':
    app = App()
