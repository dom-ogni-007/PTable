from gui.periodic_table import PTableChart
from gui.search_ui import SearchUI
from gui.title_icon import TitleIcon
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import os


class MainMenu(TitleIcon):
    def __init__(self, root):
        super().__init__(root)
        self.main_menu_setup()


    def main_menu_setup(self):
        self.root.geometry("1152x648")

    
        # Set a theme for ttk widgets
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Choose a theme 


        # Create a custom style for the frame
        self.style.configure("MainMenu.TFrame", borderwidth=2, relief="ridge") 

        # Create a frame with the configured style
        self.frame = ttk.Frame(self.root, padding=10, style="MainMenu.TFrame")
        self.frame.pack(expand=True, fill="both")

        # Load the background image (GIF)

        self.current_folder = os.path.dirname(os.path.abspath(__file__))
        self.image_path = os.path.join(self.current_folder, 'images', 'main_bg.gif')
        self.bg_image = ImageTk.PhotoImage(Image.open(self.image_path))

        # Create a label with the background image
        self.bg_label = tk.Label(self.frame, image=self.bg_image)
        self.bg_label.image = self.bg_image  # Keep a reference to the image
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a custom style for the buttons
        self.style.configure("MainMenu.TButton", 
                     font=('Verdana', 14), 
                     foreground='black', 
                     background='light gray',  
                     relief='raised',
                     width=22)

        self.search_btn = ttk.Button(self.frame, text="Search", command=self.search_btn_click, style="MainMenu.TButton")
        self.search_btn.place(relx=0.3, rely=0.5)

        self.chart_btn = ttk.Button(self.frame, text="Periodic Table of Elements", command=self.chart_btn_click, style="MainMenu.TButton")
        self.chart_btn.place(relx=0.57, rely=0.5)

        self.about_btn = ttk.Button(self.frame, text="About", command=self.about_btn_click, style="MainMenu.TButton")
        self.about_btn.place(relx=0.3, rely=0.6)

        self.exit_btn = ttk.Button(self.frame, text="Exit", command=self.exit_btn_click, style="MainMenu.TButton")
        self.exit_btn.place(relx=0.57, rely=0.6)


    def search_btn_click(self):
        self.window1 = tk.Toplevel(self.root)
        self.search_win = SearchUI(self.window1)
        self.window1.mainloop()

    def chart_btn_click(self):
        self.window2 = tk.Toplevel(self.root)
        self.chart_win = PTableChart(self.window2)
        self.window2.mainloop()

    def about_btn_click(self):
        self.msg = '''PTable: A Python Module for \nthe Periodic Table of Elements\n\n\n
Developers:\n
Basagre, Ransford Keanu C.\n
Borral, Jaira Mae U.\n
De Jesus, James Andrei C.\n
Domingo, David Arnold R.\n
Jacinto, Euliemae C.\n

BSCpE 2A - G1
Group No. 6\n
December 2023'''

        messagebox.showinfo(title='About', message=self.msg)

    def exit_btn_click(self):
        # Display a confirmation messagebox
        self.result = messagebox.askokcancel("Exit", "Are you sure you want to exit?")
        if self.result:
            # If the user clicks OK, close the application
            self.root.destroy()

    
# Main application (comment this code)
# if __name__ == "__main__":
#     root = tk.Tk()
#     main_menu = MainMenu(root)
#     root.mainloop()
