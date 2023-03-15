// Copyright (C) 2021 The Qt Company Ltd.
// SPDX-License-Identifier: LicenseRef-Qt-Commercial OR GPL-3.0

import QtQuick 6.2
import QtQuick.Window 6.2
// import COMBDb

Window {
    id: window

    minimumWidth: 960
    minimumHeight: 540

    visible: true
    visibility: Qt.WindowFullScreen
    title: "COMBDb"

    Loader {
        id: screenLoader
        source: "LoginScreen.ui.qml"
        height: window.height
        width: window.width
    }

//    LoginScreen {
//        id: loginScreen
//        height: window.height
//        width: window.width
//    }

//    HomeScreen {
//        id: homeScreen
//        height: window.height
//        width: window.width
//    }

}

