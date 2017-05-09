import tkinter as tk
from ciphers import *

class gui (tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #text
        self._text = text(parent=self, controller=self, bg="yellow")

        #entry
        self._terminal = terminal(parent=self, controller=self)

        #grid
        self._text.grid(column=0, row=0, sticky="nsew")
        self._terminal.grid(column=0, row=1, sticky="nsew")

        #config
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.grid_columnconfigure(0,weight=1)

class terminal(tk.Entry):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Entry.__init__(self, parent, *args, **kwargs)
        self.controller = controller
        self.text_in = tk.StringVar()
        self.config(textvariable=self.text_in)
        self.bind("<Return>", self.on_enter)

    def on_enter(self, event):
        execution = self.parse(self.text_in.get())
        try:
            text = eval(execution)
        except:
            text = "Please try again."

        self.controller._text.set_text(text)

    def parse(self, statement):

        methods = ["at_bash", "caesar"]

        execution = ""

        #only triggers on spaces
        statement += " "

        while " " in statement:
            #use segment, drop segment from statement
            ministate = statement[0:statement.index(" ")]
            statement = statement[statement.index(" ")+1:]

            #pipe
            if ministate == "|":
                execution = "(" + execution + ")"

            #method
            elif ministate in methods:
                execution = ministate + execution
            
            #string
            elif (ministate[0] == '"') and (ministate[-1] == '"'):
                #validate- must be only single string
                if all (x not in ['"',"'"] for x in ministate[1:-2]):
                    execution = ministate + execution
                else:
                    print("Data not valid- quotes")
            
            #params
            elif (ministate[0] == "(") and (ministate[-1] == ")") and (execution[-1] == ")"):
                if all (x not in ["(", ")"] for x in ministate[1:-2]):
                    execution = execution[:-1]
                    ministate = ministate[1:-1]
                    execution = execution + "," + ministate + ")"
                else:
                    print("Data not valid- parens")

            else:
                print("no")

        return execution

class text(tk.Label):

    def __init__(self, parent, controller, *args, **kwargs):
        tk.Label.__init__(self, parent, *args, **kwargs)
        self.controller = controller
        self.text_out = tk.StringVar()
        self.text_out.set("Hello")
        self.config(textvariable=self.text_out)

    def set_text(self, text):
        self.text_out.set(text)

gui = gui()
gui.geometry("960x540")
gui.mainloop()