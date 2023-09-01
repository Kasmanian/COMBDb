from tkinter import ttk


class BorderlessFrame(ttk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

    def center(self):
        # get app
        app = self.master

        # set most updated window values
        app.update_idletasks()

        # get total visible width and positional x
        width = app.winfo_width()
        frame_width = app.winfo_rootx() - app.winfo_x()
        total_width = width + 2 * frame_width
        x = app.winfo_screenwidth() // 2 - total_width // 2

        # get window height and positional x
        height = app.winfo_height()
        header_height = app.winfo_rooty() - app.winfo_y()
        window_height = height + header_height + frame_width
        y = app.winfo_screenheight() // 2 - window_height // 2

        # set app to center
        app.geometry("{}x{}+{}+{}".format(width, height, x, y))
        app.deiconify()
