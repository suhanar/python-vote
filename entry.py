import tkinter as tk
window = tk.Tk()
label = tk.Label(text="Name")
label.pack()
entry = tk.Entry()
entry.pack()
textWid=tk.Text()
textWid.insert(tk.END,"the end")
textWid.pack()


window.mainloop()
