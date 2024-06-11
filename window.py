import tkinter as tk
from tkinter import ttk
import subprocess

root = tk.Tk()

width , height = 800 ,500

display_width = root.winfo_screenwidth()
dispaly_height = root.winfo_screenheight()

left = int(display_width/2 - width/2)
top = int(dispaly_height/2 - height/2)

root.geometry(f'{width}x{height}+{left}+{top}')
root.resizable(False,False)

root.title("Password Generator")
root.iconbitmap('9201857.ico')

label= ttk.Label(root,text='Please Click Generate to Get your Password')
label.pack()

def run_script():
    
    script_name = "password.py"

    
    result = subprocess.run(["python", script_name], capture_output=True, text=True)

    
    output_label.config(text=result.stdout)

    
    if result.stderr:
        output_label.config(text=result.stderr)



run_button = tk.Button(root, text="Generate", command=run_script)
run_button.pack(pady=20)

output_label = tk.Label(root, text="", wraplength=400 ,fg="white", bg="black")
output_label.pack(pady=20)


root.mainloop()