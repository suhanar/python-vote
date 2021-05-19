import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter",background="blue",foreground="yellow")
greeting.pack()
button = tk.Button(
    text="Click me!",
    width=5,
    height=5,
    bg="blue",
    fg="yellow",
)
button.pack()
entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()


window.mainloop()
