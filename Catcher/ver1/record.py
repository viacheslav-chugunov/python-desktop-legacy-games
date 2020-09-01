import tkinter


class Record:
    def __init__(self, score=0):
        self.username = ""
        self.count = score
        self.__root = tkinter.Tk()
        self.__entry = tkinter.Entry(self.__root)
        self.__root.title("Record saving")
        self.__root.geometry('100x45+500+300')
        self.__root.resizable(False, False)
        self.__entry.pack()
        self.__button = tkinter.Button(self.__root, text='Save')
        self.__button['command'] = self.__button_clicked
        self.__button.pack()

    def enter(self):
        self.__root.mainloop()
        self.__saveToFile()

    def best(self):
        file = open("files/records", "r")
        records = []
        for line in file:
            line = line.split(" ")
            records.append([int(line[1]), line[0]])
            records.sort(reverse=True)
        return records

    def __button_clicked(self):
        self.username = self.__entry.get()
        self.__root.destroy()

    def __saveToFile(self):
        if self.username != "":
            file = open("files/records", "a")
            file.write(self.username + " ")
            file.write(str(self.count) + "\n")
            file.close()
