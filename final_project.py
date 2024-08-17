from tkinter import *
import time
from tkinter import messagebox
import sqlite3

try:
    conobj=sqlite3.connect(database='bank.sqlite') #cwd
    curobj=conobj.cursor()
    curobj.execute("""create table acn
                   (acn_acno integer primary key autoincrement,
                   acn_name text,acn_pass text,acn_email text,
                   acn_mob text,acn_bal float,acn_opendate text)""")
    print('table created')    
except:
    print('table already exists or something went wrong')
conobj.close()


win=Tk()
win.configure(bg='powder blue')
win.state('zoomed')
win.resizable(width=False,height=False)


lbl_title=Label(win,text='Banking Automation',
                font=('arial',40,'bold','underline'),bg='powder blue')
lbl_title.pack()


date=time.strftime("%d-%m-%Y")
lbl_date=Label(win,text=date,
                font=('arial',22,'bold',),bg='powder blue')
lbl_date.place(relx=.85,rely=.1)

lbl_name=Label(win,text='PROJECT BY MISBAH',
               font=('arial',15,'bold'),bg='powder blue')
lbl_name.place(relx=0,rely=.1)

def main_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def newuser():
        frm.destroy()
        newuser_screen()

    def forgot():
        frm.destroy()
        forgot_screen()

    def login():
        global acn
        acn=e_acn.get()
        pwd=e_pass.get()
        if len(acn)==0 or len(pwd)==0:
            messagebox.showwarning('validation','Empyt field are not allowd')
        else:
            conobj=sqlite3.connect(database='bank.sqlite') 
            curobj=conobj.cursor()
            curobj.execute("""select * from acn where acn_acno=?
                           and acn_pass=?""",(acn,pwd))
            tup=curobj.fetchone()
            conobj.close() 
            if tup==None:
                messagebox.showerror("login","Invalid ACN/PASS")
            else:
                frm.destroy()
                welcome_screen()

    def reset():
        e_acn.delete(0,'end')
        e_pass.delete(0,'end')
        e_acn.focus()

    
        
    lbl_acn=Label(frm,text='ACN',
                  font=("arial",20,'bold'),bg='pink')
    lbl_acn.place(relx=.3,rely=.1)

    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.focus()
    e_acn.place(relx=.35,rely=.1)

    lbl_pass=Label(frm,text='PASS',
                   font=('arial',20,'bold'),bg='pink')
    lbl_pass.place(relx=.3,rely=.2)

    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_pass.place(relx=.35,rely=.2)
    

    btn_login=Button(frm,command=login,text='login',
                     font=('arial',20,'bold'),bd=5)
    btn_login.place(relx=.38,rely=.3)

    btn_reset=Button(frm,command=reset,text='reset',
                     font=('arial',20,'bold'),bd=5)
    btn_reset.place(relx=.47,rely=.3)

    btn_forgot=Button(frm,command=forgot,text='forgot password',
                     font=('arial',20,'bold'),bd=5)
    btn_forgot.place(relx=.37,rely=.43)


    btn_newuser=Button(frm,command=newuser,text='create new account',
                     font=('arial',19,'bold'),bd=5)
    btn_newuser.place(relx=.37,rely=.53)

def newuser_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    def newacn():
        name=e_name.get()
        pwd=e_pass.get()
        email=e_email.get()
        mob=e_mob.get()
        bal=0
        date=time.strftime("%d-%m-%Y")

        conobj=sqlite3.connect(database='bank.sqlite') 
        curobj=conobj.cursor()
        curobj.execute("""insert into acn(acn_name,acn_pass,
        acn_email,acn_mob,acn_bal,acn_opendate)
        values(?,?,?,?,?,?)""",(name,pwd,email,mob,bal,date))

        conobj.commit()
        conobj.close()

        conobj=sqlite3.connect(database='bank.sqlite') 
        curobj=conobj.cursor()
        curobj.execute("select max(acn_acno) from acn")
        tup=curobj.fetchone()
        conobj.close()

        messagebox.showinfo("New Account",f"Account Created,ACN:{tup[0]}")

        
    def reset():
        e_name.delete(0,'end')
        e_pass.delete(0,'end')
        e_email.delete(0,'end')
        e_mob.delete(0,'end')
        e_name.focus()
        
    lbl_name=Label(frm,text='Name',
                   font=('arial',20,'bold'),bg='pink')
    lbl_name.place(relx=.3,rely=.1)
    
    e_name=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_name.focus()
    e_name.place(relx=.4,rely=.1)

    lbl_pass=Label(frm,text='Password',
                   font=('arial',20,'bold'),bg='pink')
    lbl_pass.place(relx=.3,rely=.2)
    
    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_pass.place(relx=.4,rely=.2)

    lbl_email=Label(frm,text='Email',
                   font=('arial',20,'bold'),bg='pink')
    lbl_email.place(relx=.3,rely=.3)
    
    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.4,rely=.3)

    lbl_mob=Label(frm,text='Mob',
                   font=('arial',20,'bold'),bg='pink')
    lbl_mob.place(relx=.3,rely=.4)
    
    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.4,rely=.4)

    btn_submit=Button(frm,command=newacn,text='SUBMIT',
                      font=('arial',20,'bold'),bd=5)
    btn_submit.place(relx=.41,rely=.6)

    btn_reset=Button(frm,command=reset,text='RESET',
                     font=('arial',20,'bold'),bd=5)
    btn_reset.place(relx=.52,rely=.6)
    
    def back():
        frm.destroy()
        main_screen()
    btn_back=Button(frm,command=back,text='BACK',
                     font=('arial',19,'bold'),bd=5)
    btn_back.place(relx=.9,rely=.9)


def forgot_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    def reset():
        e_email.delete(0,'end')
        e_mob.delete(0,'end')
        e_acn.delete(0,'end')
        e_email.focus()
    def back():
        frm.destroy()
        main_screen()

    def forgot():
        email=e_email.get()
        acn=e_acn.get()
        mob=e_mob.get()

        conobj=sqlite3.connect(database="bank.sqlite")
        curobj=conobj.cursor()
        curobj.execute("""select acn_pass from acn
                        where acn_acno=? and acn_email=?
                        and acn_mob=?""",(acn,email,mob))
        tup=curobj.fetchone()
        conobj.close()
        if tup==None:
            messagebox.showerror("Password","Invalid details")
        else:
            messagebox.showinfo("Password",tup[0])
            frm.destroy()
            main_screen()
    
    btn_back=Button(frm,command=back,text='BACK',
                     font=('arial',19,'bold'),bd=5)
    btn_back.place(relx=.9,rely=.9)


    lbl_email=Label(frm,text='Email',
                   font=('arial',20,'bold'),bg='pink')
    lbl_email.place(relx=.3,rely=.1)
    
    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.focus()
    e_email.place(relx=.4,rely=.1)

    lbl_mob=Label(frm,text='Mob',
                   font=('arial',20,'bold'),bg='pink')
    lbl_mob.place(relx=.3,rely=.2)

    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.4,rely=.2)

    lbl_acn=Label(frm,text='Acn',
                   font=('arial',20,'bold'),bg='pink')
    lbl_acn.place(relx=.3,rely=.3)

    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.4,rely=.3)

    btn_submit=Button(frm,command=forgot,text='SUBMIT',
                      font=('arial',20,'bold'),bd=5)
    btn_submit.place(relx=.41,rely=.4)

    btn_reset=Button(frm,command=reset,text='RESET',
                     font=('arial',20,'bold'),bd=5)
    btn_reset.place(relx=.52,rely=.4)
    
def welcome_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)

    conobj=sqlite3.connect(database='bank.sqlite') 
    curobj=conobj.cursor()
    curobj.execute("""select * from acn where acn_acno=?""",(acn,))
    tup=curobj.fetchone()
    conobj.close()

    def logout():
        frm.destroy()
        main_screen()

    def details():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.15,relwidth=.7,relheight=.65)

        conobj=sqlite3.connect(database='bank.sqlite') 
        curobj=conobj.cursor()
        curobj.execute("""select * from acn where acn_acno=?""",(acn,))
        tup=curobj.fetchone()
        conobj.close()

        lbl_wel=Label(ifrm,text='THIS IS DETAILS SCREEN',
                  font=('arial',20,'bold'),bg='white',fg='purple')
        lbl_wel.pack()

        lbl_acn=Label(ifrm,text=f'Account no={tup[0]}',
                  font=('arial',20,'bold'),bg='white')   
        lbl_acn.place(relx=.3,rely=.2)

        lbl_bal=Label(ifrm,text=f'Your acn bal={tup[5]}',
                  font=('arial',20,'bold'),bg='white')   
        lbl_bal.place(relx=.3,rely=.3)

        lbl_date=Label(ifrm,text=f'Acn opendate={tup[6]}',
                  font=('arial',20,'bold'),bg='white')   
        lbl_date.place(relx=.3,rely=.4)

        lbl_pwd=Label(ifrm,text=f'Acn pass={tup[2]}',
                  font=('arial',20,'bold'),bg='white')   
        lbl_pwd.place(relx=.3,rely=.5)

        lbl_email=Label(ifrm,text=f'Acn email={tup[3]}',
                  font=('arial',20,'bold'),bg='white')   
        lbl_email.place(relx=.3,rely=.6)

        lbl_mob=Label(ifrm,text=f'Acn mob no={tup[4]}',
                  font=('arial',20,'bold'),bg='white')   
        lbl_mob.place(relx=.3,rely=.7)
        
    def deposit():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.15,relwidth=.7,relheight=.65)

        def depacn():
            conobj=sqlite3.connect(database='bank.sqlite') 
            curobj=conobj.cursor()
            amt=float(e_amt.get())
            curobj.execute("""update acn set acn_bal=acn_bal+?
            where acn_acno=?""",(amt,acn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Deposit",f"{amt} deposited")
            
        
        lbl_wel=Label(ifrm,text='THIS IS DEPOSIT SCREEN',
                  font=('arial',20,'bold'),bg='white',fg='purple')
        lbl_wel.pack()

        lbl_amt=Label(ifrm,text='Amonunt',
                   font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.2,rely=.2)

        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.35,rely=.2)

        btn_submit=Button(frm,command=depacn,text='SUBMIT',
                      font=('arial',20,'bold'),bd=5)
        btn_submit.place(relx=.48,rely=.4)

    def withdraw():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.15,relwidth=.7,relheight=.65)

        def witacn():
            conobj=sqlite3.connect(database='bank.sqlite') 
            curobj=conobj.cursor()
            amt=float(e_amt.get())
            curobj.execute("""update acn set acn_bal=acn_bal-?
            where acn_acno=?""",(amt,acn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Withdraw",f"{amt} withdraw")
            

        lbl_wel=Label(ifrm,text='THIS IS WITHDRAW SCREEN',
                  font=('arial',20,'bold'),bg='white',fg='purple')
        lbl_wel.pack()

        lbl_amt=Label(ifrm,text='Amonunt',
                   font=('arial',20,'bold'),bg='white')
        lbl_amt.place(relx=.2,rely=.2)

        e_amt=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_amt.place(relx=.35,rely=.2)

        btn_submit=Button(frm,command=witacn,text='SUBMIT',
                      font=('arial',20,'bold'),bd=5)
        btn_submit.place(relx=.48,rely=.4)


    def update():
        ifrm=Frame(frm,highlightbackground='black',highlightthickness=2)
        ifrm.configure(bg='white')
        ifrm.place(relx=.2,rely=.15,relwidth=.7,relheight=.65)

        def updateacn():
            name=e_name.get()
            pwd=e_pass.get()
            email=e_email.get()
            mob=e_mob.get()
            
            conobj=sqlite3.connect(database='bank.sqlite') 
            curobj=conobj.cursor()
            curobj.execute("""update acn set acn_name=?,
                            acn_pass=?,acn_email=?,acn_mob=?
                            where acn_acno=?""",(name,pwd,email,mob,acn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update","profile Update")
            frm.destroy()
            welcome_screen()
                           

        lbl_wel=Label(ifrm,text='THIS IS UPDATE SCREEN',
                  font=('arial',20,'bold'),bg='white',fg='purple')
        lbl_wel.pack()


        lbl_name=Label(ifrm,text='NAME',
                  font=('arial',20,'bold'),bg='white')   
        lbl_name.place(relx=0,rely=.1)

        e_name=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_name.place(relx=0,rely=.2)

        lbl_pass=Label(ifrm,text='PASS',
                       font=('arial',20,'bold'),bg='white')
        lbl_pass.place(relx=.7,rely=.1)

        e_pass=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_pass.place(relx=.7,rely=.2)

        lbl_email=Label(ifrm,text='EMAIL',
                       font=('arial',20,'bold'),bg='white')
        lbl_email.place(relx=0,rely=.5)

        e_email=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_email.place(relx=0,rely=.6)

        lbl_mob=Label(ifrm,text='MOB',
                       font=('arial',20,'bold'),bg='white')
        lbl_mob.place(relx=.7,rely=.5)

        e_mob=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        e_mob.place(relx=.7,rely=.6)


        btn_update=Button(ifrm,command=updateacn,text='UPDATE',
                          font=('arile',20,'bold'),bd=5)
        btn_update.place(relx=.8,rely=.8)


        conobj=sqlite3.connect(database='bank.sqlite') 
        curobj=conobj.cursor()
        curobj.execute("""select * from acn where acn_acno=?""",(acn,))
        tup=curobj.fetchone()
        conobj.close()

        e_name.insert(0,tup[1])
        e_pass.insert(0,tup[2])
        e_email.insert(0,tup[3])
        e_mob.insert(0,tup[4])
        e_name.focus()
        
       

    btn_logout=Button(frm,command=logout,text='LOGOUT',
                     font=('arial',19,'bold'),bd=5)
    btn_logout.place(relx=.9,rely=.9)
    
    
    lbl_wel=Label(frm,text=f'welcom,{tup[1]}',
                  font=('arial',20,'bold'),bg='pink')
    lbl_wel.place(relx=0,rely=0)

    btn_details=Button(frm,command=details,width=12,text='Check details',
                     font=('arial',19,'bold'),bd=5)
    btn_details.place(relx=0,rely=.2)

    btn_deposit=Button(frm,command=deposit,width=12,text='Deposit amt',
                     font=('arial',19,'bold'),bd=5)
    btn_deposit.place(relx=0,rely=.3)

    btn_withdraw=Button(frm,command=withdraw,width=12,text='withdraw amt',
                     font=('arial',19,'bold'),bd=5)
    btn_withdraw.place(relx=0,rely=.4)

    btn_update=Button(frm,command=update,width=12,text='update details',
                     font=('arial',19,'bold'),bd=5)
    btn_update.place(relx=0,rely=.5)
    


main_screen()
win.mainloop()
    





