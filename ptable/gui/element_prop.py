from gui.title_icon import TitleIcon
from prop import atomic_sym, atomic_name
from prop import atomic_num, atomic_mass
from prop import electron_config, electronegativity
from prop import melting_point, oxidation_states
from prop import standard_state, year_discovered
import tkinter as tk


class ElementProperties(TitleIcon):
    def __init__(self, root, index_no):
        super().__init__(root)
        
        self.index_no = index_no

        self.element_data = {
            "Symbol": atomic_sym.elist,
            "Atomic Name": atomic_name.elist,
            "Atomic Number": atomic_num.elist,
            "Atomic Mass": atomic_mass.elist,
            "Electron Configuration": electron_config.elist,
            "Electronegativity (Pauling Scale)": electronegativity.elist,
            "Melting Point": melting_point.elist,
            "Oxidation States": oxidation_states.elist,
            "Standard State": standard_state.elist,
            "Year Discovered": year_discovered.elist
            }
        self.properties = list(self.element_data.keys())
        
        self.font = ("Courier", 12) # aligned font

        self.show_element_properties(self.index_no)
    

    def show_element_properties(self, index_no):
        self.frame1 = tk.LabelFrame(self.root, text='ELEMENT PROPERTIES', font=("Helvetica", 28),
                                    fg='gray', padx = 30, pady = 30)
        self.frame1.grid(row=1, column=1, columnspan=2, padx = 30, pady = 30)
        
        for i, property in enumerate(self.properties):
            for j, val in enumerate(self.element_data[property]):
                if index_no == j:
                    self.prop_labels = f"{property:<35} \t {val}"
                    self.label1 = tk.Label(self.frame1, text=self.prop_labels, anchor='w', 
                                        justify="left", pady=3, font=self.font)
            
            self.label1.grid(row=i, column=1, sticky='w')


# #Main application (comment this code)
# if __name__ == "__main__":
#     root = tk.Tk()
#     element_prop = ElementProperties(root, 7)
#     root.mainloop()
