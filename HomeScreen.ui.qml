/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    id: body
    width: 1920
    height: 1080

    Text {
        id: welcome
        width: 432
        height: 64
        text: qsTr("Welcome!")
        anchors.verticalCenter: parent.verticalCenter
        font.pixelSize: 48
        horizontalAlignment: Text.AlignHCenter
        anchors.horizontalCenter: parent.horizontalCenter
    }
}
