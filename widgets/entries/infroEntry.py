from tkinter import ttk


class InfoEntry(ttk.Entry):
    def __init__(self, master):
        ttk.Entry.__init__(self, master)
        self.configure(state="disabled")

    def clear(self):
        self.configure(state="enabled")
        self.delete(0, "end")
        self.configure(state="disabled")
