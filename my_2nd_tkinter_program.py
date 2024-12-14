import tkinter as tk

class VIEW:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Your Messeage", font=('Courier',18))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=('Arial',10))
        self.textbox.pack(padx=10, pady=10)

        self.check = tk.Checkbutton(self.root, text='')


        self.root.mainloop()

    