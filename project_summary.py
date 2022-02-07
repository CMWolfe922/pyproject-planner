import tkinter as tk 
from tkinter import ttk 
from app_widgets import LabelInput

class ProjectSummary(tk.Frame):
    """Subclass of the tkinter Frame object. This class will act 
    as a Frame and can take all the same arguments as the tk.Frame class"""

    frm_description = """Fillout project summary form below. This 
    Includes the project name, brief description, the version you're 
    currenlty working on and the authors name (put additional authors in
    the project description)."""
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # Create a dict for keeping track of inputs:
        self.inputs = {}

        # Building Section Project Summary form
        projectsummary = tk.LabelFrame(self, text="Project Summary")

        # Frame description
        self.frm_description_var = tk.StringVar()
        self.frm_description_var.set(self.frm_description)
        frm_description_lbl = ttk.Label(self, textvariable=self.frm_description_var, font=("Helvetica",64,"bold"), wraplength=600)
        frm_description_lbl.grid(row=0, column=0, columnspan=3)

        # Line 1: Input Project Name, Version and Author
        self.inputs['Project Name'] = LabelInput(
        	projectsummary, "Project Name",
        	input_var=tk.StringVar()
        )
        self.inputs['Project Name'].grid(row=1, column=0)
        self.inputs['Version'] = LabelInput(
        	projectsummary, "Version",
        	input_var=tk.StringVar()
        )
        self.inputs['Version'].grid(row=1, column=1)
        self.inputs['Author'] = LabelInput(
        	projectsummary, "Author",
        	input_var=tk.StringVar()
        )
        self.inputs['Author'].grid(row=1, column=2)
        
        # Line 2
        self.project_description = tk.Text(projectsummary)
        self.project_description.grid(row=2, column=0, columnspan=3)
        self.inputs['Summary Description'] = self.project_description.get('1.0', tk.END)

        self.columnconfigure(1, weight=1)

    def write_section_a(self, inputs, filename):

    	with open(filename, "wb") as f: 
    		pass
    	pass


class Application(tk.Tk):
	"""Application Root Window"""

