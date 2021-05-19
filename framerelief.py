import tkinter as tk

border_relief= {

    "flat": tk.FLAT,

    "sunken": tk.SUNKEN,

    "raised": tk.RAISED,

    "groove": tk.GROOVE,

    "ridge": tk.RIDGE,
}
window = tk.Tk()
for relief_name,relief in border_relief.items():
    frame = tk.Frame(master= window,relief = relief,borderwidth=5)
    label = tk.Label(master=frame,text=relief_name)
    frame.pack()
    label.pack()

window.mainloop()
