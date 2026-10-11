#! /usr/bin/env python3

from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import subprocess

def calculate(*args):
    try:
        value = expr.get()
        result = subprocess.run(["./cee.sh", value], capture_output=True)
        
        output_box.configure(state="normal")
        output_box.insert(INSERT, result.stdout)
        output_box.insert(INSERT, "\n")
        output_box.configure(state="disabled")
    except ValueError:
        pass

root = Tk()
root.title("Combinatory Expression Evaluator")

mainframe = ttk.Frame(root, padding=(4, 4, 4, 4))
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

ttk.Label(mainframe, text="Enter the Combinatory Expression:").grid(column=1, row=1)

expr = StringVar()
expr_entry = ttk.Entry(mainframe, width=32, textvariable=expr)
expr_entry.grid(column=1, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, row=3, sticky=(N, S))

ttk.Label(mainframe, text="Evaluation:").grid(column=1, row=4)

output_box = ScrolledText(mainframe, height=32, width=128)
output_box.grid(column=1, row=5)
output_box.configure(state="disabled")

"""
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(2, weight=1)
for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)
"""

expr_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
