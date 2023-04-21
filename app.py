import tkinter as tk
from tkinter import ttk

import _modules as m
import constants as const
import widgets as tkw
from database import Database


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.__database = Database()
        self.__mainframe = None
        self.title(const.TITLE)
        self.EM = const.EM

        # database validation & login
        self.__inMainloop = False
        self.run()

    def reframe(self, frame):
        if self.__mainframe is not None:
            self.__mainframe.destroy()
        self.__mainframe = frame(self)
        self.__mainframe.pack()

    def run(self):
        # get database
        db = self.__database

        # validate json and grab database path from it
        m.validate_json(const.ENVAR_PATH)
        pathToDatabase = m.read_from_json(
            const.ENVAR_PATH, const.DB_JSON_KEYPATH)

        # validate database file
        if db.connect(pathToDatabase):
            print(f"Connected! Current path is '{pathToDatabase}'")
            # move to login screen
            self.reframe(tkw.LoginFrame)
        else:
            print(f"Not connected! Current path is '{pathToDatabase}'")
            # move to database browser
            self.reframe(tkw.DatabaseBrowserFrame)

        if not self.__inMainloop:
            self.__inMainloop = True
            self.mainloop()


def main():
    App()


if __name__ == '__main__':
    main()
