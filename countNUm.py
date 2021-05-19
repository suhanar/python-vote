import tkinter as tk
def decrease():
    value=int(label["text"])
    label["text"] = f"{value-1}"
def increase():
    value=int(label["text"])
    label["text"] = f"{value+1}"



window = tk.Tk()
window.rowconfigure(0,minsize=50,weight=1)

window.columnconfigure([0,1,2],minsize=50,weight=1)

btn_dec = tk.Button(master=window,text="-",command=decrease)

btn_dec.grid(row=0,column=0,sticky="nsew")

label = tk.Label(master=window,text='0')

label.grid(row=0,column=1)

btn_inc = tk.Button(master=window,text="+",command=increase)

btn_inc.grid(row=0,column=2)

window.mainloop()
