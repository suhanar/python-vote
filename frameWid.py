import tkinter as tk
window = tk.Tk()

frame_a=tk.Frame()
frame_b=tk.Frame()
label_a = tk.Label(master=frame_a,text="This is Frame A")
label_b = tk.Label(master=frame_b,text="This is Frame B")

frame_a.pack()
frame_b.pack()
label_a.pack()
label_b.pack()

window.mainloop()
