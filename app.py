import tkinter as tk
from tkinter import ttk, TclError

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
        self.inMainloop = False
        self.run()

    def get_database_error(self):
        return self.__database.error

    def get_database_path(self):
        # validate json and get database path from it
        m.validate_json(const.ENVAR_PATH)
        pathToDatabase = m.read_from_json(const.ENVAR_PATH, const.DB_JSON_KEYPATH)
        return pathToDatabase

    def set_database_path(self, path):
        # validate json and set database path
        m.validate_json(const.ENVAR_PATH)
        m.write_to_json(const.ENVAR_PATH, const.DB_JSON_KEYPATH, path)

    def reframe(self, frame):
        if self.__mainframe is not None:
            self.__mainframe.destroy()
        self.__mainframe = frame(self)
        self.__mainframe.pack()

    def run(self):
        # get database and database file path
        db = self.__database
        pathToDatabase = self.get_database_path()

        # validate database file
        if db.connect(pathToDatabase):
            print(f"Connected! Current path is <{pathToDatabase}>")
            # move to login screen
            self.reframe(tkw.LoginFrame)
        else:
            print(f"Not connected! Current path is <{pathToDatabase}>")
            # move to database browser
            self.reframe(tkw.DatabaseBrowserFrame)

        if not self.inMainloop:
            self.inMainloop = True
            self.mainloop()

    def end(self):
        self.__database.close()
        self.destroy()


def main():
    App()


if __name__ == "__main__":
    main()
