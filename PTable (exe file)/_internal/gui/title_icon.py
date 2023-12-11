import os

class TitleIcon:
    def __init__(self, root):
        self.root = root
        self.root.title("PTable")
        
        # Get the directory of the current script
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to the logo.ico file
        self.icon_path = os.path.join(self.script_dir, "logo.ico")
        # Set the icon
        self.root.iconbitmap(self.icon_path)
