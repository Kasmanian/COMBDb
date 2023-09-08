from tkinter import filedialog, ttk

from ..entries import InfoEntry
from .borderless_frame import BorderlessFrame


class DatabaseBrowserFrame(BorderlessFrame):
    def __init__(self, master):
        BorderlessFrame.__init__(self, master)
        # set card size
        EM = master.EM
        master.geometry(f"{24*EM}x{32*EM}")

        # define user interface items
        statusLabelText = "Current COMBDb.accdb file"
        pathToDatabase = master.get_database_path()
        databaseError = master.get_database_error()
        if pathToDatabase is None:
            pathToDatabase = "Select a COMBDb.accdb file"
            statusLabelText = "No database file in path"
        elif databaseError:
            if databaseError["code"] == 2:
                statusLabelText = "Invalid database selected"
        self.statusLabel = ttk.Label(self, text=statusLabelText)
        self.statusLabel.pack()
        self.databaseEntry = InfoEntry(self, int(2 * master.EM))
        self.databaseEntry.enter(pathToDatabase)
        self.databaseEntry.pack()
        self.openButton = ttk.Button(self, text="Open...", command=master.run)
        self.openButton.pack()
        self.browseButton = ttk.Button(self, text="Browse...", command=self.browse)
        self.browseButton.pack()
        self.exitButton = ttk.Button(self, text="Exit", command=master.end)
        self.exitButton.pack()

        # center and set attributes
        self.center()

    def browse(self):
        master = self.master
        path = filedialog.askopenfilename(
            initialdir="/",
            title="Select a COMBDb.accdb file",
            filetypes=((".accdb files", "*.accdb"),),
        )
        if path != "" and path is not None:
            master.set_database_path(path)
            self.databaseEntry.clear()
            self.databaseEntry.enter(path)
