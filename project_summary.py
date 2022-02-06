import tkinter as tk 
from tkinter import ttk 

class LabelInput(tk.Frame):
	"""A class that creates a widget containing a label and an input"""
	
	def __init__(self, parent, label='', input_class=ttk.Entry,
                 input_var=None, input_args=None, label_args=None,
                 **kwargs):
		"""
		:param parent: This argument is a reference to the parent widget; 
			all widgets we create will take this as the first argument

		:param label: This the text for the label part of the widget.

		:param input_class: This is the class of the widget we want to create. 
			It should be an actual callable class object, not a string. 
			If left blank, ttk.Entry will be used.

		:param input_var:  This is a Tkinter variable to assign to the input.
			 It's optional, since some widgets don't use variables.

		:param input_args: This is an optional dictionary of any additional
			arguments for the input constructor

		:param label_args: This is an optional dictionary of any additional
			arguments for the label constructor.

		:param **kwargs: Finally, we catch any additional keyword arguments in
			**kwargs. These will be passed to the Frame constructor.
		"""
        super().__init__(parent, **kwargs)

        input_args = input_args or {}
        label_args = label_args or {}
        self.variable = input_var

        if input_class in (ttk.Checkbutton, ttk.Button, ttk.Radiobutton):
        	input_args["text"] = label
        	input_args["variable"] = input_var
        else:
        	self.label = ttk.Label(self, text=label, **label_args)
        	self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))
        	input_args["textvariable"] = input_var

        self.input = input_class(self, **input_args)
        self.input.grid(row=1,column=0, sticky=(tk.W + tk.E))
        self.columnconfigure(0, weight=1)

        # <<<<<<<<<<<< Pick up at Pg. 52 number 10. >>>>>>>>>>>>>>>>>>>>>>





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

