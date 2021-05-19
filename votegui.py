





import tkinter as tk
lst_lion = []
lst_tiger = []
lst_horse = []
def raise_frame():
    details ={"first":{"name":"suhu","id":1},
              "second":{"name":"raj","id":2},
              "third":{"name":"manu","id":3},
              "fourth":{"name":"suhan","id":4}



    }
    top = tk.Toplevel()
    top.title("Register Vote")
    top.geometry("300x300+120+120")
    home_btn = tk.Button(top,text="Home",command=home)

    home_btn.pack()
    lbl_name = tk.Label(top,text="Enter Your Name")
    lbl_name.pack()
    entry_name =tk.Entry(top)
    entry_name.pack()
    lbl_Id = tk.Label(top,text="Enter Your ID")
    lbl_Id.pack()
    entry_Id =tk.Entry(top)
    entry_Id.pack()

    btn_reg = tk.Button(top,text="Submit",command=lambda:register(details,entry_name,entry_Id))
    btn_reg.pack()

def register(details,entry_name,entry_id):

    reg_name = entry_name.get()
    reg_id= int(entry_id.get())
    dict_al = {}
    var = tk.IntVar()



    for x in details.copy():
        if(reg_name==details[x]["name"] and reg_id==details[x]["id"]):
            k=details[x].pop("name")
            v=details[x].pop("id")
            dict_al["kname"]=k
            dict_al["kid"]=v
            print(dict_al)
            del(details[x])
            #print(details)
            #print(v)





            top = tk.Toplevel()
            top.title("Vote")
            top.geometry("300x300+120+120")
            home_btn = tk.Button(top,text="Home",command=home)

            home_btn.pack()
            '''label = tk.Label(top,text="Successs")
            label.pack()
            lbl_reg = tk.Label(top,text="name")
            lbl_reg.pack()
            lbl_reg1 = tk.Label(top,text="id")
            lbl_reg1.pack()

            lbl_reg["text"] = reg_name
            lbl_reg1["text"] = reg_id'''

            btn_lion=tk.Radiobutton(top,text="Register to Lion Party",command=lambda:count_lion(top,var),value=1,variable=var)

            btn_lion.pack()
            btn_tiger=tk.Radiobutton(top,text="Register to tiger party",command=lambda:count_tiger(top,var),value=2,variable=var)
            btn_tiger.pack()
            btn_horse=tk.Radiobutton(top,text="Register to horse party",command=lambda:count_horse(top,var),value=3,variable=var)
            btn_horse.pack()
            btn = tk.Button(top,text="click",command=click_me)
            btn.pack()





            break
    else:
        top = tk.Toplevel()
        top.title("Not Eligible")
        top.geometry("300x300+120+120")
        lbl=tk.Label(top,text="Sorry You are not eligible vor voting")
        lbl.pack()

        home_btn = tk.Button(top,text="Home",command=home)

        home_btn.pack()


def click_me():
    top = tk.Toplevel()
    top.title("Voted ")
    top.geometry("300x300+120+120")
    lbl = tk.Label(top,text="Your vote saved Thank you for voting")
    lbl.pack()
    home_btn = tk.Button(top,text="Home",command=home)

    home_btn.pack()



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
    home_btn = tk.Button(top,text="Home",command=home)

    home_btn.pack()
    lion_text = "Lion got "+str(sum(lst_lion))
    tiger_text="Tiger got "+str(sum(lst_tiger))
    horse_text = "Horse got "+str(sum(lst_horse))
    lbl_lion = tk.Label(top,text=lion_text)
    lbl_tiger = tk.Label(top,text=tiger_text)
    lbl_horse = tk.Label(top,text=horse_text)
    lbl_lion.pack()
    lbl_tiger.pack()
    lbl_horse.pack()

    if(sum(lst_lion)>sum(lst_tiger) and sum(lst_lion)>sum(lst_horse)):
        lbl_lion1 = tk.Label(top,text="Lion Wins")
        lbl_lion1.pack()

    elif(sum(lst_tiger)>sum(lst_lion) and sum(lst_tiger)>sum(lst_horse)):
        lbl_lion2 = tk.Label(top,text="Tiger Wins")
        lbl_lion2.pack()

    elif(sum(lst_horse)>sum(lst_lion) and sum(lst_horse)>sum(lst_tiger)):
        lbl_lion3 = tk.Label(top,text="Horse Wins")
        lbl_lion3.pack()

    else:
        lbl_lion4 = tk.Label(top,text="Government decide")
        lbl_lion4.pack()

def home_button():
    home()

def click_result():

    top = tk.Toplevel()
    top.title("See The Result")
    top.geometry("300x300+120+120")
    home_btn = tk.Button(top,text="Home",command=home)

    home_btn.pack()


    lbl_pass = tk.Label(top,text="Enter Password")
    lbl_pass.pack()
    entry_pass = tk.Entry(top)
    entry_pass.pack()
    button_pass = tk.Button(top,text="Click",command=lambda:entry_password(top,entry_pass))
    button_pass.pack()


def entry_password(top,entry_pass):

    password = ["a","b","c"]
    entry_get = entry_pass.get()
    if entry_get in password:
        see_result(lst_lion,lst_tiger,lst_horse)

    else:
        lbl_no = tk.Label(top,text="Not Allowed")
        lbl_no.pack()



def exit_window():
    window.destroy()



def home():
    top_h= tk.Toplevel()
    top_h.title("Home")
    top_h.geometry("300x300+120+120")


    btn1 = tk.Button(top_h,text="Register Your Vote",command=raise_frame)
    btn1.pack()
    btn2 = tk.Button(top_h,text="See the result!!!!",command=click_result)
    btn2.pack()
#btn2 = tk.Button(top,text="See the result",command=lambda:see_result(lst_lion,lst_tiger,lst_horse))
#btn2.pack()
    btn3 = tk.Button(top_h,text="Exit",command=exit_window)
    btn3.pack()






window = tk.Tk()
lbl_wel = tk.Label(master=window,text="Welcome to the Vote App")
lbl_wel.pack()
btn = tk.Button(master=window,text="Home",command=home)
btn.pack()




window.geometry("300x300+120+120")
window.mainloop()
