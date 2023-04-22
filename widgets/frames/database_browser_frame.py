from tkinter import filedialog, ttk

from .borderless_frame import BorderlessFrame


class DatabaseBrowserFrame(BorderlessFrame):
    def __init__(self, master):
        BorderlessFrame.__init__(self, master)
        # set card size
        EM = master.EM
        master.geometry(f"{24*EM}x{32*EM}")

        # define user interface items
        pathToDatabase = master.get_database_path() or "Select a database file"
        self.databaseEntry = ttk.Entry(self)
        self.databaseEntry.insert(0, pathToDatabase)
        self.databaseEntry.pack()
        self.openButton = ttk.Button(self, text="Open...", command=master.run)
        self.openButton.pack()
        self.browseButton = ttk.Button(self, text="Browse...", command=self.browse)
        self.browseButton.pack()
        self.exitButton = ttk.Button(self, text="Exit", command=master.destroy)
        self.exitButton.pack()
        msgLabel = None  # displays error or validation notification

        # center and set attributes
        self.center()

    def browse(self):
        master = self.master
        path = filedialog.askopenfilename(
            initialdir="/",
            title="Select an MS Access file",
            filetypes=((".accdb files", "*.accdb"),),
        )
        if path != "" and path is not None:
            master.set_database_path(path)
            self.databaseEntry.delete(0, "end")
            self.databaseEntry.insert(0, path)
