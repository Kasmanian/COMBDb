/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 6.2
import QtQuick.Controls 6.2
// import COMBDb

Rectangle {
    id: body
    objectName: qsTr("body")
    // width: Constants.width
    // height: Constants.height
    color: "#ffffff"
    border.color: "#808080"
    border.width: 0
    smooth: true
    antialiasing: true


    Rectangle {
        id: rectangle
        width: 440
        height: 520
        color: "#ffffff"
        radius: 16
        border.color: "#808080"
        border.width: 1
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter

        Rectangle {
            id: usernameContainer
            width: 380
            height: 32
            color: "#ffffff"
            radius: 8
            border.color: username.activeFocus? "#6baef8" : "#808080"
            anchors.top: parent.top
            anchors.topMargin: 340
            anchors.horizontalCenter: parent.horizontalCenter

            TextField {
                id: username
                background: Rectangle {
                    color: "#00ffffff"
                }
                anchors.fill: parent
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                clip: false
                font.pointSize: 10
                font.family: "Arial"
                placeholderText: qsTr("Username")
                validator: RegularExpressionValidator { regularExpression: /[0-9A-Za-z!()-.?_`~;:@#$%^&*+=]+/ }
            }
        }

        Rectangle {
            id: passwordContainer
            x: 30
            y: 60
            width: 380
            height: 32
            color: "#ffffff"
            radius: 8
            border.color: password.activeFocus? "#6baef8" : "#808080"
            anchors.top: parent.top
            anchors.topMargin: 390
            anchors.horizontalCenter: parent.horizontalCenter

            TextField {
                id: password
                background: Rectangle {
                    color: "#00ffffff"
                }
                x: -30
                y: -390
                opacity: 1
                visible: true
                anchors.fill: parent
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                clip: false
                font.family: "Arial"
                placeholderText: qsTr("Password")
                font.pointSize: 10
                echoMode: qsTr("Password")
                validator: RegularExpressionValidator { regularExpression: /[0-9A-Za-z!()-.?_`~;:@#$%^&*+=]+/ }
            }
        }

        Rectangle {
            id: loginButtonContainer

            property bool enabled: username.acceptableInput && password.acceptableInput
            property var dynamicColor: !loginButtonContainer.enabled? "#808080" : loginButton.containsMouse? "#6baef8" : "#4390e4"

            x: 30
            y: 60
            width: 380
            height: 32
            color: loginButtonContainer.dynamicColor
            radius: 8
            border.color: "#00ffffff"
            border.width: 0
            anchors.top: parent.top
            layer.mipmap: false
            anchors.topMargin: 440
            anchors.horizontalCenter: parent.horizontalCenter

            MouseArea {
                id: loginButton
                objectName: qsTr("loginButton")
                anchors.fill: parent
                hoverEnabled: true
                cursorShape: loginButtonContainer.enabled? Qt.PointingHandCursor : Qt.ArrowCursor
            }

            Text {
                id: loginText
                color: "#ffffff"
                text: qsTr("Login")
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                font.pixelSize: 14
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
                font.family: "Arial"
                anchors.rightMargin: 0
                anchors.leftMargin: 0
                anchors.bottomMargin: 0
                anchors.topMargin: 0
            }
        }

        Image {
            id: asodHeader
            y: -150
            width: 400
            height: 140
            source: "assets/asod_header.png"
            anchors.horizontalCenterOffset: -6
            layer.samples: 0
            anchors.horizontalCenter: parent.horizontalCenter
            layer.smooth: false
            layer.mipmap: false
            cache: true
            asynchronous: false
            mipmap: false
            antialiasing: false
            mirror: false
            smooth: true
            autoTransform: false
            fillMode: Image.PreserveAspectFit
        }
    }
}
