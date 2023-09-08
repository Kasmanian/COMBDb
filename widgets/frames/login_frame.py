from tkinter import ttk

from .borderless_frame import BorderlessFrame


class LoginFrame(BorderlessFrame):
    def __init__(self, master):
        BorderlessFrame.__init__(self, master)
        # set card size
        EM = master.EM
        master.geometry(f"{24*EM}x{32*EM}")

        # define user interface items
        logoImg = None
        titleLabel = None
        usernameInput = None
        passwordInput = None
        loginButton = None  # takes the user's credintials and logs in
        exitButton = ttk.Button(self, text="Exit", command=master.end)
        exitButton.pack()
        msgLabel = None  # displays error or validation notification

        # center and set attributes
        self.center()
