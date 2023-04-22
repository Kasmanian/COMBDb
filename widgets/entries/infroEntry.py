from tkinter import ttk


class InfoEntry(ttk.Entry):
    def __init__(self, master, span=0):
        ttk.Entry.__init__(self, master)
        if span > 0:
            self.configure(state="disabled", width=span)
        self.span = span

    def clear(self):
        self.configure(state="enabled")
        self.delete(0, "end")
        self.configure(state="disabled")

    def enter(self, string: str):
        span = self.span
        self.configure(state="enabled")
        self.delete(0, "end")
        self.text = string
        displayText = string
        if len(string) > span > 6:
            displayText = "..." + string[len(string) - (span - 4) :]
        self.insert(0, displayText)
        self.configure(state="disabled")
