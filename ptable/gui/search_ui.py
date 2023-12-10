from prop import atomic_sym, atomic_name
from prop import atomic_num, atomic_mass
from prop import atomic_radius, boiling_point
from prop import chem_group, density
from prop import electron_affinity, electron_config
from prop import electronegativity, ionization_energy
from prop import melting_point, oxidation_states
from prop import standard_state, year_discovered
from gui.element_prop import ElementProperties
from gui.title_icon import TitleIcon
import tkinter as tk
from tkinter import ttk


class SearchUI(TitleIcon):
    def __init__(self, root):
        super().__init__(root)
        self.root2 = None
        
        self.element_data = {
            "Symbol": atomic_sym.elist,
            "Atomic Name": atomic_name.elist,
            "Atomic Number": atomic_num.elist,
            "Atomic Mass": atomic_mass.elist,
            "Atomic Radius (van der Waals)": atomic_radius.elist,
            "Boiling Point": boiling_point.elist,
            "Chemical Group Block": chem_group.elist,
            "Density": density.elist,
            "Electron Affinity": electron_affinity.elist,
            "Electron Configuration": electron_config.elist,
            "Electronegativity (Pauling Scale)": electronegativity.elist,
            "Ionization Energy": ionization_energy.elist,
            "Melting Point": melting_point.elist,
            "Oxidation States": oxidation_states.elist,
            "Standard State": standard_state.elist,
            "Year Discovered": year_discovered.elist
            } 
        
        #self.font = ("Courier", 12)
        self.window_setup()


    def selected_combobox_option(self, event):
        self.selected_data = self.combo_var.get()
        self.update_listbox(self.selected_data)
        self.entry_var.set("Search here...")  

    def update_listbox(self, selected_data):
        self.treeview.delete(*self.treeview.get_children()) # Clear existing items
        
        if selected_data == 'Symbol':
            for data in self.element_data[selected_data]:
                self.treeview.insert("", "end", text=data)
        else:
            for i, data in enumerate(self.element_data[selected_data]):
                self.treeview.insert("", "end", text=data, values=(atomic_sym.elist[i],))
            
    def update_listbox_from_search(self, event):
        self.search_listbox = self.entry_var.get().lower()
        self.treeview.delete(*self.treeview.get_children())  # Clear existing items
        self.selected_data = self.combo_var.get()
        
        for i, data in enumerate(self.element_data[self.selected_data]):
            if self.search_listbox in data.lower():
                if self.selected_data == 'Symbol':
                    self.treeview.insert("", "end", text=data)
                else:
                    self.treeview.insert("", "end", text=data, values=(atomic_sym.elist[i],))
        
    def selected_listbox(self, event):
        if self.treeview.selection():
            self.win_new_entry = self.treeview.item(self.treeview.selection())["text"][:]
            self.entry_var.set(self.win_new_entry)
        else:
            # Handle the case when no item is selected
            self.entry_var.set("Search here...")  

    def destroy_existing_root2(self):
        if self.root2 is not None:
            self.root2.destroy()
            self.root2 = None  # Set root to None to indicate it has been destroyed
    
    def on_search_click(self):
        if self.treeview.selection():
            self.destroy_existing_root2()
            self.root2 = tk.Toplevel(self.root)

            self.selected_data = self.combo_var.get()

            for i, data in enumerate(self.element_data['Symbol']):
                if self.selected_data == 'Symbol':
                    self.selected_text = self.treeview.item(self.treeview.selection())['text'][:]
                    if data == self.selected_text:
                        ElementProperties(self.root2, i)
                else:
                    self.selected = self.treeview.item(self.treeview.selection())['values'][0]
                    if data == self.selected:
                        ElementProperties(self.root2, i)


    def clear_placeholder(self, event):
        if self.entry_var.get() == "Search here...":
            self.entry_var.set("")

    def restore_placeholder(self, event):
        if not self.entry_var.get():
            self.entry_var.set("Search here...")

    
    def window_setup(self):
        self.win_frame = tk.LabelFrame(self.root, text="Search", 
                                       font=("Helvetica", 48), fg="gray", width=500, 
                                       height=250, padx=20, pady=20)
        self.win_frame.grid(row=0, column=0, padx=20, pady=20)

        self.entry_var = tk.StringVar()
        self.win_entry = tk.Entry(self.win_frame, textvariable=self.entry_var, width=35)
        self.win_entry.grid(row=0, column=1, rowspan=2, padx=20, pady=20, ipady=3)
        self.win_entry.bind('<KeyRelease>', self.update_listbox_from_search)

        self.entry_var.set("Search here...")

        self.win_entry.bind("<FocusIn>", self.clear_placeholder)
        self.win_entry.bind("<FocusOut>", self.restore_placeholder)


        self.win_label = tk.Label(self.win_frame, text="Search by...")
        self.win_label.grid(row=0, column=3)

        self.combo_var = tk.StringVar()
        self.win_combobox = ttk.Combobox(self.win_frame, values=list(self.element_data.keys()), 
                                         textvariable=self.combo_var, state='readonly', width=30)
        self.win_combobox.grid(row=1, column=3)
        self.win_combobox.set("Symbol")
        self.win_combobox.bind('<<ComboboxSelected>>', self.selected_combobox_option)

        self.treeview = ttk.Treeview(self.win_frame, columns=("Element"), selectmode='browse',
                                     show='tree headings', height=10)
        self.treeview.heading("#0", text="Result")
        self.treeview.heading("Element", text="Element")
        self.treeview.column("#0", width=200, minwidth=200, anchor="w")
        self.treeview.column("Element", width=65,minwidth=65 , anchor="w")
        self.treeview.grid(row=2, column=1, rowspan=2)
        self.treeview.bind('<ButtonRelease-1>', self.selected_listbox)

        self.scrollbar = tk.Scrollbar(self.win_frame, orient=tk.VERTICAL, 
                                      command=self.treeview.yview,
                                      activebackground='black', bd=10)
        self.scrollbar.grid(row=2, column=2, sticky='ns', rowspan=2)
        self.treeview.config(yscrollcommand=self.scrollbar.set)

        self.win_button = tk.Button(self.win_frame, text="View", width=12,
                                    bd=3, command=self.on_search_click, relief='raised',
                                    font=('Calibri', 13, 'bold'))
        self.win_button.grid(row=3, column=3)

        self.text1 = "Select an item from the list and click 'View' \nto show the full properties of the element."
        self.label1 = tk.Label(self.win_frame, text=self.text1, anchor='s',
                               foreground='black')
        self.label1.grid(row= 2, column=3, sticky='S')


# Main application (comment this code)
# if __name__ == "__main__":
#     root = tk.Tk()
#     search_ui = SearchUI(root)
#     root.mainloop()
