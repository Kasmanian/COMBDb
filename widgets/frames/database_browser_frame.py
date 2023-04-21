from tkinter import ttk

from .borderless_frame import BorderlessFrame


class DatabaseBrowserFrame(BorderlessFrame):
    def __init__(self, master):
        BorderlessFrame.__init__(self, master)
        # set card size
        EM = master.EM
        master.geometry(f"{24*EM}x{32*EM}")

        # define user interface items
        openButton = ttk.Button(self, text="Open", command=master.run)
        openButton.pack()
        exitButton = ttk.Button(self, text="Exit", command=master.destroy)
        exitButton.pack()
        msgLabel = None  # displays error or validation notification

        # center and set attributes
        self.center()
