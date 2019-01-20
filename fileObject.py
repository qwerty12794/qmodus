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

    def format_postcode(self, postcode):
        if len(postcode) == 6:
            postcode = postcode[:4] + ' ' + postcode[4:]
        return postcode

    def run(self):
        while True:
            if self.running:
                if self.file_name:
                    with open(self.file_name, 'r', errors='replace') as file:
                        csvReader = csv.reader(file)
                        self.count = 0
                        self.text_box.delete('1.0', END)
                        for row in csvReader:
                            if row:
                                print(row)
                                company = row[0]
                                postcode = row[1]
                                formatted_postcode = self.format_postcode(postcode)
                                query = '(bedrijfsnaam:"{}" AND postcode:"{}")'.format(company, formatted_postcode)
                                self.text_box.insert(END, query)
                                self.text_box.insert(END, '\n')
                                self.count += 1
                        # lines = [x.strip() for x in file]
                        # self.text_box.delete('1.0', END)
                        # print(lines)
                        # for line in lines:
                        #     if line:
                        #         self.count += 1
                        #         splitted_line_list = line.split(',')
                        #         print(splitted_line_list)
                        #         company = splitted_line_list[0]
                        #         if company != '' and 'Column' not in company:
                        #             print(company)
                        #             postcode_string = splitted_line_list[1]
                        #             if postcode_string != '-':
                        #                 #plaats = splitted_line_list[1]
                        #                 postcode_list = postcode_string.split(' ') #normaal
                        #                 # postcode_list = splitted_line_list[1].split(' ') #uitzondering
                        #                 if len(postcode_list) > 1:
                        #                     postcode = postcode_list[0] + ' ' + postcode_list[1]
                        #                 elif len(postcode_list) == 1:
                        #                     postcode_string = postcode_list[0]
                        #                     postcode = postcode_string[:4] + ' ' + postcode_string[4:]
                        #                 else:
                        #                     postcode = '-'
                        #                 #website = splitted_line_list[3]
                        #                 query = '(bedrijfsnaam:"{}" AND postcode:"{}")'.format(company, postcode)
                        #                 self.text_box.insert(END, query)
                        #                 self.text_box.insert(END, '\n')

                        self.set_running(False)
                        self.text_box.insert(END, str(self.count))
                        print(self.count)
                        self.count = 0
