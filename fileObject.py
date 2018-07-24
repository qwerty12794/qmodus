import csv
import threading
from tkinter import*

class FileObject(threading.Thread):

    def __init__(self, text_box):
        threading.Thread.__init__(self)
        self.file_name = ''
        self.running = True
        self.text_box = text_box
        self.count = 0

    def set_file_name(self, file_name):
        if file_name:
            self.file_name = file_name

    def get_file_name(self):
        return self.file_name

    def print_file_name(self):
        file_name = self.get_file_name()
        print(file_name)

    def set_running(self, bool):
        if bool:
            self.running = True
        else:
            self.running = False


    def run(self):
        while True:
            if self.running:
                if self.file_name:
                    with open(self.file_name, 'r', errors='replace') as file:
                        lines = [x.strip() for x in file]
                        self.text_box.delete('1.0', END)
                        for line in lines:
                            if line:
                                self.count += 1
                                splitted_line_list = line.split(',')
                                print(splitted_line_list)
                                company = splitted_line_list[0]
                                plaats = splitted_line_list[1]
                                postcode_list = splitted_line_list[2].split(' ')
                                if len(postcode_list) > 1:
                                    postcode = postcode_list[0] + ' ' + postcode_list[1]
                                elif len(postcode_list) == 1:
                                    postcode_string = postcode_list[0]
                                    postcode = postcode_string[:4] + ' ' + postcode_string[4:]
                                else:
                                    postcode = '-'
                                website = splitted_line_list[3]
                                query = '(bedrijfsnaam:"{}" handelsnaam:"{}" AND postcode:"{}")'.format(company, company, postcode)
                                self.text_box.insert(END, query)
                                self.text_box.insert(END, '\n')
                                self.set_running(False)
                        print(self.count)
                        self.count = 0
