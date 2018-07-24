from tkinter import *
from tkinter import filedialog

class FileImporter:

    def __init__(self):
        self.root = Tk()
        self.root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

        print(self.root.filename)
importer = FileImporter()

