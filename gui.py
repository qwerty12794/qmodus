from tkinter import filedialog
from tkinter import *
from fileObject import FileObject

class Gui:

    def __init__(self):
        self.root = Tk()
        self.main_frame = Frame(self.root, width = 1000, height=720)
        self.main_frame.grid_propagate(False)
        self.main_frame.pack()

        self.text_box_frame = Frame(self.main_frame)
        self.text_box_frame.grid(row=0, column=0)

        self.text_box = Text(self.text_box_frame, width=140, height=40)
        self.text_box.pack()

        self.button_frame = Frame(self.main_frame, width=140, height=40)
        self.button_frame.grid(row=1, column=0)

        self.button = Button(self.button_frame, text='select file', command=self.get_file_name)
        self.button.pack()

        self.file = FileObject(self.text_box)

    def get_file_name(self):
        file_root = Tk()
        file_root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                        filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
        self.file.set_file_name(file_root.filename)
        self.file.set_running(True)
        file_root.destroy()

    def run(self):
        self.file.start()
        self.root.mainloop()
