import tkinter as tk

def celcius():
    #Celsius = (Fahrenheit – 32) * 5/9
    value = int(entry_fah.get())
    lbl_cel["text"] = 5/9 * (value - 32)




window = tk.Tk()


window.rowconfigure(2,minsize=50,weight=1)

window.columnconfigure([0,1,2],minsize=50,weight=1)

entry_fah = tk.Entry()
entry_fah.grid(row=0,column=1)

label_fah = tk.Label(master=window,text="*f")
label_fah.grid(row=0,column=2)

btn_cel = tk.Button(master=window,text="Click Me",command=celcius)
btn_cel.grid(row=1,column=1)

lbl_cel = tk.Label(master=window,text="0")
lbl_cel.grid(row=2,column=1)

window.mainloop()
