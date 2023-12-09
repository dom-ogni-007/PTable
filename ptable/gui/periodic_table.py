from gui.title_icon import TitleIcon
from gui.element_prop import ElementProperties
from prop import atomic_sym
import tkinter as tk
from PIL import Image, ImageTk
import os


class PTableChart(TitleIcon):
    def __init__(self, root):
        super().__init__(root)
        self.root2 = None

        self.layout = [[6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7], 
                       [1,2,0,0,0,0,0,0,0,0,0,0,5,6,6,6,6,7], 
                       [1,2,0,0,0,0,0,0,0,0,0,0,4,5,6,6,6,7], 
                       [1,2,3,3,3,3,3,3,3,3,3,3,4,5,5,6,6,7], 
                       [1,2,3,3,3,3,3,3,3,3,3,3,4,4,5,5,6,7], 
                       [1,2,0,3,3,3,3,3,3,3,3,3,4,4,4,5,6,7], 
                       [1,2,0,3,3,3,3,3,3,3,3,3,4,4,4,4,6,7], 
                       [0,0,0,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8], 
                       [0,0,0,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9]] 
        
        self.elist = [
            'H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne',
            'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca',
            'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
            'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr',
            'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn',
            'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'Hf', 'Ta', 'W', 'Re', 
            'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 
            'Rn', 'Fr', 'Ra', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds',
            'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og', 'La', 'Ce', 
            'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 
            'Tm', 'Yb', 'Lu', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 
            'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr'
            ]


        self.symbol_font = ("Georgia", 13, 'bold')
        self.for_btn_func()
        self.symbol_button()


    def symbol_button(self):

        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()
        self.frame1.lower()


        self.current_folder = os.path.dirname(os.path.abspath(__file__))
        self.image_path = os.path.join(self.current_folder, 'images', 'sub_bg.gif')
        self.bg_image = ImageTk.PhotoImage(Image.open(self.image_path))

        self.label1 = tk.Label(self.frame1, image=self.bg_image)
        self.label1.image = self.bg_image  # Keep a reference to the image
        self.label1.pack()

        # Create a container frame for the buttons
        self.button_container = tk.Frame(self.frame1, bg='#99D4AC')
        self.button_container.place(relx=0.5, rely=0.45, anchor='center')  # Center the button container

        self.btn_list = []
        self.frm_list = []
        for i, x in enumerate(range(118)):
            self.frm = tk.Frame(self.button_container, highlightthickness=1, highlightbackground='black')
            self.frm_list.append(self.frm)

            self.btn = tk.Button(self.frm_list[i], font=self.symbol_font, width=4, height=2,
                                 activeforeground='#BFBFBF', relief='raised', bd=0, fg='white')
            self.btn_list.append(self.btn)


        self.set_color = ['#E3628C', '#8E64E5', '#2C66E2',
                          '#E8743D', '#757575', '#DEDE6D',
                          '#D4AC99', '#99ACD4', '#68E2DD'] # 9 diff button colors

        self.original_colors = [] # List to store the original colors

        self.i = 0
        self.row = 0
        for row in self.layout:
            self.col = 0
            for x in row:
                if x == 1:
                    self.btn_list[self.i].config(text=self.elist[self.i], bg=self.set_color[0])
                    
                elif x == 2:
                    self.btn_list[self.i].config(text=self.elist[self.i], bg=self.set_color[1])

                elif x == 3:
                    self.btn_list[self.i].config(text=self.elist[self.i], bg=self.set_color[2])

                elif x == 4:
                    self.btn_list[self.i].config(text=self.elist[self.i], bg=self.set_color[3])

                elif x == 5:
                    self.btn_list[self.i].config(text=self.elist[self.i], bg=self.set_color[4])

                elif x == 6:
                    self.btn_list[self.i].config(text=self.elist[self.i], bg=self.set_color[5], fg='black')

                elif x == 7:
                    self.btn_list[self.i].config(text=self.elist[self.i], bg=self.set_color[6], fg='black')

                elif x == 8:
                    self.btn_list[self.i].config(text=self.elist[self.i], bg=self.set_color[7], fg='black')

                elif x == 9:
                    self.btn_list[self.i].config(text=self.elist[self.i], bg=self.set_color[8], fg='black')

                if x != 0:
                    self.frm_list[self.i].grid(row=self.row, column=self.col)
                    self.btn_list[self.i].pack()
                    self.btn_list[self.i].config(command=self.btn_func_list[self.i])

                    self.original_color = self.btn_list[self.i].cget("bg")  # Get the original color
                    self.original_colors.append(self.original_color)

                    self.btn_list[self.i].bind("<Enter>", lambda event, i=self.i: self.on_enter(i))
                    self.btn_list[self.i].bind("<Leave>", lambda event, i=self.i: self.on_leave(i))
                
                    self.i += 1

                self.col += 1
                
            self.row += 1

        for btn in self.btn_list:
            btn.lift()


    def on_enter(self, i):
        self.btn_list[i].config(bg='#D9D9D9')
    
    def on_leave(self, i):
        original_color = self.original_colors[i]
        self.btn_list[i].config(bg=original_color)  # Reset to the original color


    def for_btn_func(self):
        self.btn_func_list = []

        for i in range(118):
            def btn_func(symbol=self.elist[i]):
                self.show_prop(symbol)
                    
            self.btn_func_list.append(btn_func)

    def show_prop(self, symbol):
        self.destroy_existing_root2()
        for i, data in enumerate(atomic_sym.elist):
            if symbol == data:
                self.root2 = tk.Toplevel(self.root)
                ElementProperties(self.root2, i)

    def destroy_existing_root2(self):
        if self.root2 is not None:
            self.root2.destroy()
            self.root2 = None  # Set root to None to indicate it has been destroyed


# Main application (comment this code)
# if __name__ == "__main__":
#     root = tk.Tk()
#     ptable_chart = PTableChart(root)
#     root.mainloop()
