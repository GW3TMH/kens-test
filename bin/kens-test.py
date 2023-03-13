#!/usr/bin/python3

import os
import configparser
import tkinter as tk

ProgramName = "Kens Test"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        
        # Default settings
        parent = '400x295+400+400'
        
        # Create the Main window
        self.master.title(ProgramName)
        self.master.geometry(parent)        


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__=="__main__":
	main()

__version__='1.0'
