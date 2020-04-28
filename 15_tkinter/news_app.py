import tkinter as tk
from parser import NVParser

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.parser = NVParser("http://nv.ua/allnews.html")
        self.data = self.parser.work()
        self.entry_list = list()
        self.pack()
        self.create_main_canvas()
        self.create_refresh()
        self.create_widgets()

    def refresh(self):
        for entry in self.entry_list:
            entry.destroy()
        self.create_widgets()

    def create_main_canvas(self):
        self.main_canvas = tk.Canvas(self, width=800, height=800)
        self.main_canvas.pack()
        self.frame = tk.Frame(self.main_canvas, bg='#80c1ff', bd=5)
        self.frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.8, anchor='n')

    def create_refresh(self):
        refresh_button = tk.Button(self.frame, text="Refresh", command=self.refresh, bg='#80c1ff')
        refresh_button.pack(side='top', pady=10)

    def create_widgets(self):
        entry = tk.Frame(self.frame, bg='#FFFFFF', bd=1, padx=10)
        entry.pack(side='top')
        row = 0
        for data in self.data:
            if row < 5:
                text = f"{data['tag']} - {data['date']}\n{data['headline']}"
                label = tk.Label(entry, height=4, bg='#FFFFFF', text=text, wraplength=500, justify='left')
                label.pack(side='top', anchor='w')
                row += 1
                self.entry_list.append(entry)


root = tk.Tk()
app = Application(master=root)
app.mainloop()
