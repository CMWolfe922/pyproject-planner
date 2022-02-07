import tkinter as tk 
from tkinter import ttk 
# from app_widgets import LabelInput
from datetime import datetime
import os, sys 

class LabelInput(tk.Frame):
    """A class that creates a widget containing a label and an input"""
    
    def __init__(self, parent, label='', input_class=ttk.Entry,
        input_var=None, input_args=None, label_args=None, **kwargs):
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


    def grid(self, sticky=(tk.E + tk.W), **kwargs):
        super().grid(sticky=sticky, **kwargs)

    def get(self):
        if self.variable:
            return self.variable.get()
        elif type(self.input) == tk.Text:
            return self.input.get('1.0', tk.END)
        else:
            return self.input.get()

    def set(self, value, *args, **kwargs):
        if type(self.variable) == tk.BooleanVar:
                self.variable.set(bool(value))
        elif self.variable:
                self.variable.set(value, *args, **kwargs)
        elif type(self.input).__name__.endswith('button'):
            if value:
                self.input.select()
            else:
                self.input.deselect()
        elif type(self.input) == tk.Text:
            self.input.delete('1.0', tk.END)
            self.input.insert('1.0', value)
        else:
            self.input.delete(0, tk.END)
            self.input.insert(0, value)


class ProjectSummary(tk.Frame):
    """Subclass of the tkinter Frame object. This class will act 
    as a Frame and can take all the same arguments as the tk.Frame class"""
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        # Create a dict for keeping track of inputs:
        self.inputs = {}

        # Building Section Project Summary form
        projectsummary = tk.LabelFrame(self, text="Project Summary")

        # Line 1: Input Project Name, Version and Author
        self.inputs['Project Name'] = LabelInput(
            projectsummary, "Project Name",
            input_var=tk.StringVar()
        )
        self.inputs['Project Name'].grid(row=0, column=0)

        self.inputs['Version'] = LabelInput(
            projectsummary, "Version",
            input_var=tk.StringVar()
        )
        self.inputs['Version'].grid(row=0, column=1)

        self.inputs['Author'] = LabelInput(
            projectsummary, "Author",
            input_var=tk.StringVar()
        )
        self.inputs['Author'].grid(row=0, column=2)
        
        # Line 2
        self.inputs['Short Description'] = LabelInput(
            self, "Short Description",
            input_class=tk.Text,
            input_args={"width":50, "height":10}
        )
        self.inputs['Short Description'].grid(sticky=tk.W, row=1, column=0)

        # default the form to reset after being filled out
        self.reset()

    def get(self):
        """Retrieve the data from the form as dictionary"""

        # the data from tkinter variables needs to be retrieved 
        # and saved into regular python objects. 

        data = {}
        for key, widget in self.inputs.items():
            data[key] = widget.get()
        return data

    def reset(self):
        """Resets the form entries"""

        # clear all values 
        for widget in self.inputs.values():
            widget.set('')


class Application(tk.Tk):
    """Application Root Window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("PyProject Planner")
        self.resizable(width=False, height=False)

        ttk.Label(self, text='PyProject Planner', font=("Helvetica", 16)).grid(row=0)

        self.recordform = ProjectSummary(self)
        self.recordform.grid(row=1, padx=10)

        self.savebutton = ttk.Button(self, text="Save", command=self.on_save)
        self.savebutton.grid(sticky=tk.E, row=4, padx=10)

        # Status bar
        self.status = tk.StringVar()
        self.statusbar = ttk.Label(self, textvariable=self.status)
        self.statusbar.grid(sticky=(tk.W + tk.E), row=5, padx=10)

        self.records_saved = 0

    def on_save(self):
        """Handles the save button clicks"""

        # for now we save toa harcoded filename with a datestring.
        # If it doesn't exist, it will be created.
        # otherwise just append to the existing file 

        datestring = datetime.today().strftime("%Y-%m-%d")
        filename = 'project_specifications.txt'
        newfile = not os.path.exists(filename)

        data = self.recordform.get()
        field = [key for key in data.keys()]
        val = [val for val in data.values()]

        def write_project_name(field, val):
            """data at index 0 """

            with open(filename, 'a') as f:
                for line in f:
                    line1 = "="*60 + "\n"
                    line.write(line1)
                    line.write(field +": "+val)
                    line.write(line1)

        write_project_name(field[0], val[1])

        self.recordform.reset()


if __name__ == '__main__':

    app = Application()
    app.mainloop()



if __name__ == '__main__':
    app = Application()
    app.mainloop()