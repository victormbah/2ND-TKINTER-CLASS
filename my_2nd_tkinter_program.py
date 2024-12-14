import tkinter as tk
from tkinter import messagebox

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vic's Tkinter GUI Program")
        self.root.geometry("500x300")

        # Menubar
        self.menubar = tk.Menu(self.root)
        
        # File menu
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Close Program', font=('Comic Sans MS', 10), command=self.on_closing)
        self.filemenu.add_command(label='Close Without Question', command=exit)
        self.filemenu.add_separator()
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        # Action menu
        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label='Show Message', command=self.show_message)
        self.menubar.add_cascade(label="Action", menu=self.actionmenu)

        # Attach the menubar to the root window
        self.root.config(menu=self.menubar)

        # Label
        self.label = tk.Label(self.root, text="Your Message", font=('Courier', 18))
        self.label.pack(padx=10, pady=10)

        # Textbox
        self.textbox = tk.Text(self.root, height=5, font=('Arial', 10))
        self.textbox.bind('<Control-Return>', self.shortcut)  # Ctrl+Enter to trigger show_message
        self.textbox.pack(padx=10, pady=10)

        # Checkbox
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text='Show Messagebox', font=('Arial', 10), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        # Show Message Button
        self.button = tk.Button(self.root, text='Show Message', font=('Arial', 10), command=self.show_message)
        self.button.pack(padx=10, pady=5)

        # Clear Textbox Button
        self.clearbutton = tk.Button(self.root, text='Clear Message', font=('Comic Sans MS', 10), command=self.clear)
        self.clearbutton.pack(padx=10, pady=5)

        # Handle window close event
        self.root.protocol('WM_DELETE_WINDOW', self.on_closing)

        # Start the main loop
        self.root.mainloop()

    def show_message(self):
        message = self.textbox.get('1.0', tk.END).strip()  # Strip trailing newline
        if self.check_state.get() == 0:
            print(message)
        else:
            messagebox.showinfo(title="Message", message=message)

    def shortcut(self, event):
        self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title='Exit?', message='Do you really want to Exit?'):
            self.root.destroy()

    def clear(self):
        self.textbox.delete('1.0', tk.END)

# Run the GUI
GUI()
