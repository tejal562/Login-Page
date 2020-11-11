from tkinter import *


def connection(user, passw):
    host = 'localhost'
    user = 'root'
    pw = 'tejal123'
    port = 3306
    db = 'tutorial'
    conn = sql.connet(host=host, user=user, password=pw, port=port, db=db)
    query = "select id form login where username = s and password = s"
    vals = (user,passw)
    cur = conn.cursor()
    cur.execute(query,vals)
    result = cur.fetchall()
    conn.close()
    return result
                      

def check():
    u_name =  un.get()
    pass_word  = pw.get()
    data = connection(u_name, pass_word)
    if len(data) > 0:
         messagebox.showinfo(title= "hello root", message = "welcome....youe login sucessful")
    else:
       messagebox.showinfo(title= "hello user", message = "plz enter correct information")
     
            

    
root = Tk()
un = StringVar()
pw = StringVar()

root.geometry("300x250")
root.title("TEJAL JADHAV")
t = Lable(root, text = "Login Form", fomt = ('arial', 14),db = 15)
t.pack()
form = Frame(root)
form.pack(side = TOP, fill = X)
nameL = Lable(form, text = "Username:",Ifont = ('arial', 14), bd = 15)
passL = Lable(form, text = "Password:", font = ('arial', 14), bd = 15)
nameL.grid(row = 1, sticky = w)
passL.grid(row = 2, sticky = w)
nameE = Entry(form, textvariable = un)
passE = Entry(form, textvariable = pw, show = "*")
nameE.grid(row =1, column = 2)
passE.grid(row =2, column = 2)
login = Button(root,text = "Login" ,command = check)
login.pack()

root.mainloop()


