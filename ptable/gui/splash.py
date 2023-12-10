from gui.title_icon import TitleIcon
from gui.main_menu import MainMenu
import time
import os
import tkinter as tk
from PIL import ImageTk, Image


class Splash(TitleIcon):
    def __init__(self, root):
        super().__init__(root)

        self.win_width = 427
        self.win_height = 250
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coor = (self.screen_width/2)-(self.win_width/2)
        self.y_coor = (self.screen_height/2)-(self.win_height/2)
        self.root.geometry("%dx%d+%d+%d" %(self.win_width, self.win_height,
                                           self.x_coor, self.y_coor))
        self.root.overrideredirect(1)

        self.splash_setup()


    def splash_setup(self):
        tk.Frame(self.root, width=self.win_width, height=self.win_height, bg='#272727').place(x=0, y=0)


        self.current_folder = os.path.dirname(os.path.abspath(__file__))
        self.image_path = os.path.join(self.current_folder, 'images', 'title.png')
        self.title = ImageTk.PhotoImage(Image.open(self.image_path))


        self.label1 = tk.Label(self.root, image=self.title, bg='#272727')
        self.label1.place(x=92, y=55)

        self.label2 = tk.Label(self.root, text='Loading...', fg='white', bg='#272727',
                               font=('Calibri', 11))
        self.label2.place(x=15, y=215)

        # for animation

        self.c1_path = os.path.join(self.current_folder, 'images', 'c1.png')
        self.c2_path = os.path.join(self.current_folder, 'images', 'c2.png')

        self.image_a = ImageTk.PhotoImage(Image.open(self.c2_path))
        self.image_b = ImageTk.PhotoImage(Image.open(self.c1_path))

        self.x1 = 175
        self.x2 = 197
        self.x3 = 218
        self.x4 = 240

        for i in range(2):
            self.l1 = tk.Label(self.root, image=self.image_a, border=0, relief=tk.SUNKEN).place(x=self.x1, y=145)
            self.l2 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN).place(x=self.x2, y=145)
            self.l3 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN).place(x=self.x3, y=145)
            self.l4 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN).place(x=self.x4, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)

            self.l1 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN).place(x=self.x1, y=145)
            self.l2 = tk.Label(self.root, image=self.image_a, border=0, relief=tk.SUNKEN).place(x=self.x2, y=145)
            self.l3 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN).place(x=self.x3, y=145)
            self.l4 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN).place(x=self.x4, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)

            self.l1 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN).place(x=self.x1, y=145)
            self.l2 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN).place(x=self.x2, y=145)
            self.l3 = tk.Label(self.root, image=self.image_a, border=0, relief=tk.SUNKEN).place(x=self.x3, y=145)
            self.l4 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN).place(x=self.x4, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)

            self.l1 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN).place(x=self.x1, y=145)
            self.l2 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN).place(x=self.x2, y=145)
            self.l3 = tk.Label(self.root, image=self.image_b, border=0, relief=tk.SUNKEN).place(x=self.x3, y=145)
            self.l4 = tk.Label(self.root, image=self.image_a, border=0, relief=tk.SUNKEN).place(x=self.x4, y=145)
            self.root.update_idletasks()
            time.sleep(0.5)

        self.root.destroy()
        self.root2 = tk.Tk()
        self.main_menu = MainMenu(self.root2)
        self.root2.mainloop()


# if __name__ == '__main__':
#     root = tk.Tk()
#     splash = Splash(root)
#     root.mainloop()
