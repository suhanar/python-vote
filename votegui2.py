details ={"first":{"name":"suhu","id":1},
          "second":{"name":"raj","id":2},
          "third":{"name":"manu","id":3},
          "fourth":{"name":"suhan","id":4}



}
dict_al = {}



import tkinter as tk
lst_lion = []
lst_tiger = []
lst_horse = []
def raise_frame():

    top = tk.Toplevel()
    top.title("Register Vote")
    top.geometry("300x300+120+120")
    top.rowconfigure([0,1,2,3],minsize=50,weight=1)

    top.columnconfigure([0,1,2],minsize=50,weight=1)
    home_btn = tk.Button(top,text="Home",command=home,font=("Times New Roman", 8, "bold"),bg="blue")

    home_btn.grid(row=0,column=0)
    lbl_name = tk.Label(top,text="Enter Your Name",font=("Times New Roman", 8, "bold"),bg="green")
    lbl_name.grid(row=1,column=1)
    entry_name =tk.Entry(top)
    entry_name.grid(row=1,column=2)
    lbl_Id = tk.Label(top,text="Enter Your ID",font=("Times New Roman", 8, "bold"),bg="green")
    lbl_Id.grid(row=2,column=1)
    entry_Id =tk.Entry(top)
    entry_Id.grid(row=2,column=2)

    btn_reg = tk.Button(top,text="Submit",command=lambda:register(entry_name,entry_Id),font=("Times New Roman", 8, "bold"),bg="red")
    btn_reg.grid(row=3,column=2)

    top.configure(bg="cyan")

    top.mainloop()

def register(entry_name,entry_id):

    reg_name = entry_name.get()
    reg_id= int(entry_id.get())

    var = tk.IntVar()
    for x in details.copy():
        if(reg_name==details[x]["name"] and reg_id==details[x]["id"]):
            k = details[x].pop("name")
            v = details[x].pop("id")
            print(k)
            print(v)
            dict_al["name"] = k
            dict_al["id"] = v
            print(dict_al)

            del(details[x])
            print(details)
            #print(v)








            top = tk.Toplevel()
            top.title("Vote")
            top.geometry("300x300+120+120")
            top.rowconfigure([0,1,2,3,4,5],minsize=50,weight=1)

            top.columnconfigure([0,1,2],minsize=50,weight=1)
            top.configure(bg="cyan")
            home_btn = tk.Button(top,text="Home",command=lambda:home_des(top),bg="blue")

            home_btn.grid(row=0,column=0)



            btn_lion=tk.Radiobutton(top,text="Vote for Lion Party",command=lambda:count_lion(top,var),value=1,variable=var,font=("Times New Roman", 10, "bold"),bg="green")

            btn_lion.grid(row=1,column=1)
            btn_tiger=tk.Radiobutton(top,text="Vote for tiger party",command=lambda:count_tiger(top,var),value=2,variable=var,font=("Times New Roman", 10, "bold"),bg="green")
            btn_tiger.grid(row=2,column=1)
            btn_horse=tk.Radiobutton(top,text="Vote for horse party",command=lambda:count_horse(top,var),value=3,variable=var,font=("Times New Roman", 10, "bold"),bg="green")
            btn_horse.grid(row=3,column=1)
            btn = tk.Button(top,text="Submit",command=click_me,bg="red")
            btn.grid(row=4,column=1)





            break




    else:

        for x in dict_al:
            print(x)


            if(reg_name==dict_al["name"] and reg_id==dict_al["id"]):

                top = tk.Toplevel()
                top.title("Not Eligible")
                top.geometry("300x300+120+120")
                top.rowconfigure([0,1,2,3,4,5],minsize=50,weight=1)

                top.columnconfigure([0,1,2],minsize=50,weight=1)

                lbl_a=tk.Label(top,text="Already voted ",font=("Times New Roman", 10, "bold"),bg="green")
                lbl_a.grid(row=2,column=1)
                home_btn = tk.Button(top,text="Home",command=home,font=("Times New Roman", 10, "bold"),bg="blue")

                home_btn.grid(row=0,column=0)
                top.configure(bg="cyan")




        else:
            top = tk.Toplevel()
            top.title("Not Eligible")
            top.geometry("300x300+120+120")
            top.rowconfigure([0,1,2,3,4,5],minsize=50,weight=1)

            top.columnconfigure([0,1,2],minsize=50,weight=1)

            lbl=tk.Label(top,text="Sorry You are not eligible vor voting",font=("Times New Roman", 10, "bold"),bg="green")
            lbl.grid(row=2,column=1)

            home_btn = tk.Button(top,text="Home",command=home,font=("Times New Roman", 8, "bold"),bg="blue")

            home_btn.grid(row=0,column=0)
            top.configure(bg="cyan")








def home_des(top):
    top.destroy()
    home()




def click_me():
    top = tk.Toplevel()
    top.title("Voted ")
    top.geometry("300x300+120+120")
    top.rowconfigure([0,1,2,3,4,5],minsize=50,weight=1)

    top.columnconfigure([0,1,2],minsize=50,weight=1)
    lbl = tk.Label(top,text="Your vote saved Thank you for voting",font=("Times New Roman", 10, "bold"),bg="green")
    lbl.grid(row=2,column=1)
    home_btn = tk.Button(top,text="Home",command=home,font=("Times New Roman", 10, "bold"),bg="blue")

    home_btn.grid(row=0,column=0)
    top.configure(bg="cyan")




def count_lion(top,var):






    lst_lion.append(int(1))

    print("lion")
def count_tiger(top,var):



    lst_tiger.append(int(1))
    print("tiger")
def count_horse(top,var):



    lst_horse.append(int(1))
    print("horse")

def see_result(lst_lion,lst_tiger,lst_horse):
    top = tk.Toplevel()
    top.title("See The Result")
    top.geometry("300x300+120+120")
    top.rowconfigure([0,1,2,3,4,5],minsize=50,weight=1)

    top.columnconfigure([0,1,2],minsize=50,weight=1)
    home_btn = tk.Button(top,text="Home",command=home,font=("Times New Roman", 8, "bold"),bg="blue")

    home_btn.grid(row=0,column=0)
    lion_text = "Lion got "+str(sum(lst_lion))
    tiger_text="Tiger got "+str(sum(lst_tiger))
    horse_text = "Horse got "+str(sum(lst_horse))
    lbl_lion = tk.Label(top,text=lion_text,font=("Times New Roman", 12, "bold"),bg="green")
    lbl_tiger = tk.Label(top,text=tiger_text,font=("Times New Roman", 12, "bold"),bg="green")
    lbl_horse = tk.Label(top,text=horse_text,font=("Times New Roman", 12, "bold"),bg="green")
    lbl_lion.grid(row=1,column=1)
    lbl_tiger.grid(row=2,column=1)
    lbl_horse.grid(row=3,column=1)

    if(sum(lst_lion)>sum(lst_tiger) and sum(lst_lion)>sum(lst_horse)):
        lbl_lion1 = tk.Label(top,text="Lion Wins",font=("Times New Roman", 15, "bold"),bg="red")
        lbl_lion1.grid(row=5,column=1)

    elif(sum(lst_tiger)>sum(lst_lion) and sum(lst_tiger)>sum(lst_horse)):
        lbl_lion2 = tk.Label(top,text="Tiger Wins",font=("Times New Roman", 15, "bold"),bg="red")
        lbl_lion2.grid(row=5,column=1)

    elif(sum(lst_horse)>sum(lst_lion) and sum(lst_horse)>sum(lst_tiger)):
        lbl_lion3 = tk.Label(top,text="Horse Wins",font=("Times New Roman", 15, "bold"),bg="red")
        lbl_lion3.grid(row=5,column=1)

    else:
        lbl_lion4 = tk.Label(top,text="Government decide",font=("Times New Roman", 15, "bold"),bg="red")
        lbl_lion4.grid(row=5,column=1)
    top.configure(bg="cyan")


def home_button():
    home()

def click_result():

    top = tk.Toplevel()
    top.title("See The Result")
    top.geometry("300x300+120+120")
    top.rowconfigure([0,1,2,3],minsize=50,weight=1)

    top.columnconfigure([0,1,2],minsize=50,weight=1)
    home_btn = tk.Button(top,text="Home",command=home,font=("Times New Roman", 8, "bold"),bg="blue")

    home_btn.grid(row=0,column=0)


    lbl_pass = tk.Label(top,text="Enter Password",font=("Times New Roman", 8, "bold"),bg="green")
    lbl_pass.grid(row=1,column=1)
    entry_pass = tk.Entry(top)
    entry_pass.grid(row=1,column=2)
    button_pass = tk.Button(top,text="Submit",command=lambda:entry_password(top,entry_pass),font=("Times New Roman", 8, "bold"),bg="red")
    button_pass.grid(row=2,column=2)
    top.configure(bg="cyan")



def entry_password(top,entry_pass):

    password = ["a","b","c"]
    entry_get = entry_pass.get()
    if entry_get in password:
        see_result(lst_lion,lst_tiger,lst_horse)

    else:
        lbl_no = tk.Label(top,text="Password is incorrect",font=("Times New Roman", 8, "bold"),bg="red")
        lbl_no.grid(row=3,column=2)



def exit_window():
    window.destroy()



def home():
    top_h= tk.Toplevel()
    top_h.title("Home")
    top_h.geometry("300x300+120+120")
    top_h.rowconfigure([0,1,2],minsize=50,weight=1)

    top_h.columnconfigure([0,1,2],minsize=50,weight=1)



    btn1 = tk.Button(top_h,text="Register Your Vote",command=raise_frame,font=("Times New Roman", 12, "bold"),bg="yellow",height = 5, width = 15,bd=5)
    btn1.grid(row=0,column=1)
    btn2 = tk.Button(top_h,text="See the result!!!!",command=click_result,font=("Times New Roman", 12, "bold"),bg="yellow",height = 5, width = 15,bd=5)
    btn2.grid(row=1,column=1)
#btn2 = tk.Button(top,text="See the result",command=lambda:see_result(lst_lion,lst_tiger,lst_horse))
#btn2.pack()
    btn3 = tk.Button(top_h,text="Exit",command=exit_window,font=("Times New Roman", 12, "bold"),bg="yellow",height = 5, width = 15,bd=5)
    btn3.grid(row=2,column=1)
    top_h.configure(bg="cyan")







window = tk.Tk()
window.rowconfigure([0,1,2],minsize=50,weight=1)

window.columnconfigure([0,1,2],minsize=50,weight=1)


lbl_wel = tk.Label(master=window,text="Welcome to the Vote App",font=("Times New Roman", 12, "bold"),bg="yellow")
lbl_wel.grid(row=0,column=1)
btn = tk.Button(master=window,text="Start Your Voting by click this button",command=home,bg="red")
btn.grid(row=1,column=1)




window.configure(bg="cyan")
window.geometry("300x300+120+120")
window.mainloop()
