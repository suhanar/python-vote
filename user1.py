import tkinter as tk
import psycopg2
try:

    connection = psycopg2.connect(user = "postgres",
                                  password = "postgre123",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "usersdb")

    cursor = connection.cursor()
    #sql = "CREATE TABLE user(NAME TEXT NOT NULL,PASSWORD REAL);"
    #cursor.execute(sql)
    def submit():
        cursor_in = connection.cursor()
        sql=("INSERT INTO USERS (NAME,PASSWORD) VALUES (%s,%s)");
        val=(entry_name.get(),entry_pass.get())
        cursor_in.execute(sql,val)
        print("data inserted")
        connection.commit()
        cursor_in.close()

    def submit_del():
        cursor_del = connection.cursor()
        sql=("DELETE FROM USERS WHERE NAME=%s");

        cursor_del.execute(sql,(entry_name_del.get(),))
        print("data deleted")
        connection.commit()
        cursor_del.close()
    def submit_up():
        cursor_up = connection.cursor()
        sql=("UPDATE USERS SET NAME=%s WHERE NAME=%s");

        cursor_up.execute(sql,(entry_name_up.get(),entry_name_upd.get(),))
        print("data updated")
        connection.commit()
        cursor_up.close()
    def selection():
        cursor_sel = connection.cursor()
        sql="SELECT * FROM USERS";
        cursor_sel.execute(sql)
        res = cursor_sel.fetchone()

        lbl_sel["text"]=res




        print("data selected")


        connection.commit()
        cursor_sel.close()



except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)







window = tk.Tk()
#insertion
lbl_name = tk.Label(text="Enter your name ")
lbl_pass = tk.Label(text="Enter your password ")
entry_name = tk.Entry()
entry_pass = tk.Entry()

btn = tk.Button(text="Submit",command=submit)
#deletion
lbl_name_del = tk.Label(text="Enter your name ")

entry_name_del = tk.Entry()


btn_del = tk.Button(text="Submit_DEL",command=submit_del)


#insertion
lbl_name.pack()
entry_name.pack()
lbl_pass.pack()
entry_pass.pack()
btn.pack()

#deletion

lbl_name_del.pack()
entry_name_del.pack()


btn_del.pack()

#update
lbl_name_upd = tk.Label(text="Enter your name for updation ")

entry_name_upd = tk.Entry()

lbl_name_up = tk.Label(text="Enter your name ")

entry_name_up = tk.Entry()


btn_up = tk.Button(text="Submit_UPDATE",command=submit_up)
lbl_name_upd.pack()
entry_name_upd.pack()



lbl_name_up.pack()
entry_name_up.pack()


btn_up.pack()

#selection
lbl_sel = tk.Label(text="Datas goes here")
btn_sel = tk.Button(text="SELECT",command=selection)
lbl_sel.pack()
btn_sel.pack()






window.mainloop()
