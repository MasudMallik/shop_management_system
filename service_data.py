from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import mysql.connector as sql
from tabulate import tabulate
import matplotlib.pyplot as plt
import sqlite3


global ow_b,l,l1,own,staf,cust,ex,own_name,own_pass
own_name="masud"
own_pass="abc123"
root=Tk()
root.title("abc_service center")
root.geometry("500x400")
# root.maxsize(500,400)
root.minsize(500,400)
l=Label(root,text="welcome to abc service center",font=20)
l.grid(row=0,column=0,padx=100,pady=10)
l1=Label(root,text="****************************************",font=20)
l1.grid(row=1,column=0,padx=100,pady=10)

#start of owner section

my_db=sql.connect(host="localhost",user="admin",password="root",database="abc_service")
cur=my_db.cursor()
def ow_back1():
    global ow_b,l,l1,own,staf,cust,ex,ow_name,ow_name1,ow_pass,ow_pass1,sub,f1
    f1.destroy()
    ow_name.destroy()
    ow_name1.destroy()
    ow_pass.destroy()
    ow_pass1.destroy()
    sub.destroy()
    ow_b.destroy()
    ex.destroy()
    l=Label(root,text="welcome to abc service center",font=20)
    l.grid(row=0,column=0,padx=100,pady=10)
    l1=Label(root,text="****************************************",font=20)
    l1.grid(row=1,column=0,padx=100,pady=10)
    own=Button(root,text="Owner",height=3,width=50,bg="yellow",fg="red",command=owner)
    own.grid(row=2,column=0,pady=10,padx=90)
    staf=Button(root,text="Staff",height=3,width=50,bg="yellow",fg="red",command=staff)
    staf.grid(row=3,column=0,pady=10)
    cust=Button(root,text="Customer",height=3,width=50,bg="yellow",fg="red",command=customer)
    cust.grid(row=4,column=0,pady=10)
    ex=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
    ex.grid(row=5,column=0,padx=30)
def ow_back2():
    global ow_b,l,l1,own,staf,cust,ex,ow_name1,ow_name,ow_pass1,ow_pass,f1,sub,show_details,l2,add_staff,del_staff,ow_b1

    if True:
        l.destroy()
        l1.destroy()
        ow_b1.destroy()
        own.destroy()
        staf.destroy()
        cust.destroy()
        ex.destroy()
        show_details.destroy()
        l2.destroy()
        add_staff.destroy()
        del_staff.destroy()
        ow_b.destroy()

    
    root.title("owner_login")
    f1=Label(root,text="Owner Login:",font=10)
    f1.grid(row=0,column=0,pady=10,padx=50)
    ow_name1=Label(root,text="Enter your name: ",font=7)
    ow_name1.grid(row=1,column=0,pady=20)
    ow_name=Text(root,height=2,width=30)
    ow_name.grid(row=1,column=1)
    ow_pass1=Label(root,text="Enter your password: ",font=7)
    ow_pass1.grid(row=2,column=0,pady=20)
    ow_pass=Text(root,height=2,width=30)
    ow_pass.grid(row=2,column=1)
    ow_b=Button(root,text="Back",height=2,width=8,command=ow_back1)
    ow_b.grid(row=3,column=0,pady=10,padx=1)
    sub=Button(root,text="SUBMIT",height=2,width=7,command=check)
    sub.grid(row=3,column=1,pady=10)
    ex=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
    ex.grid(row=4,column=0,pady=10)

def ow_back3():
    global ow_b1,show_details,l2,add_staff,del_staff,ex
    global ow_b,l,l1,own,staf,cust,ex,ow_name1,ow_name,ow_pass1,ow_pass,f1,sub
    global ow1,done,pen,l1,box,ow_b3,ex11,save,data_vis,opt,sh
    sh.destroy()
    ow1.destroy()
    done.destroy()
    pen.destroy()
    l1.destroy()
    box.destroy()
    ow_b3.destroy()
    ex11.destroy()
    save.destroy()
    data_vis.destroy()
    opt.destroy()
    root.title("details")
    l2=Label(root,text="Choose option: ",font=7)
    l2.grid(row=0,column=0)

    show_details=Button(root,text="Show Details",height=3,width=50,bg="yellow",fg="red",command=details)
    show_details.grid(row=2,column=0,pady=10,padx=90)


    add_staff=Button(root,text="Add Staff",command=add_staff_det,bg="yellow",fg="red",height=3,width=50)
    add_staff.grid(row=3,column=0,pady=10)


    del_staff=Button(root,text="Remove Staff",height=3,width=50,bg="yellow",fg="red",command=del_staff_det)
    del_staff.grid(row=4,column=0,pady=10)


    ex=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
    ex.grid(row=6,column=0,padx=30)

    ow_b1=Button(root,text="Back",height=2,width=8,command=ow_back2)
    ow_b1.grid(row=5,column=0,pady=10,padx=1)
def show():
    global opt
    k=opt.get()
    if k=="choose option":
        messagebox.showerror("ERROR","Choose options first!!")
    elif k=="products":
        cur.execute("SELECT product_type,COUNT(*) AS total_num from customer group by product_type")
        p=cur.fetchall()
        df=pd.DataFrame(p,columns=["product_type","total_num"])
        head=df["product_type"]
        data=df["total_num"]
        plt.pie(data, labels=head, autopct='%1.1f%%')
        plt.title("overall product came for service")
        plt.show()
    elif k=="rush week":
        cur.execute("SELECT DAY(time_of_submit) from customer")
        da=cur.fetchall()
        week1=[]
        week2=[]
        week3=[]
        week4=[]
        data_for_bar=[]
        for j in da:
            for i in j:
                if i<=7:
                    week1.append(i)
                elif i >7 and i<=14:
                    week2.append(i)  
                elif i >14 and i<=21:
                    week3.append(i)
                else:
                    week4.append(i)
        data_for_bar.append(len(week1)) 
        data_for_bar.append(len(week2))
        data_for_bar.append(len(week3)) 
        data_for_bar.append(len(week4)) 
        plt.bar([2,4,6,8],data_for_bar) 
        plt.xticks([2,4,6,8],["week1","week2","week3","week4"])
        plt.xlabel("-----weeks----")
        plt.ylabel("----number of customers----")
        plt.text(2,data_for_bar[0]+0.5,str(data_for_bar[0]))
        plt.text(4,data_for_bar[1]+0.5,str(data_for_bar[1]))
        plt.text(6,data_for_bar[2]+0.5,str(data_for_bar[2]))
        plt.text(8,data_for_bar[3]+0.5,str(data_for_bar[3]))
        plt.title("number of customer per week")
        plt.show()    
def save_data():

    df = pd.read_sql_query("SELECT * FROM customer", my_db)
    df.to_excel("output.xlsx", index=False, engine='openpyxl')  
    my_db.close()



def details():
    global ow_b1,show_details,l2,add_staff,del_staff,ex
    global ow_b,l,l1,own,staf,cust,ex,ow_name1,ow_name,ow_pass1,ow_pass,f1,sub
    global ow1,done,pen,l1,box,ow_b3,ex11,save,data_vis,opt,sh
    root.geometry("500x450")
    ow_b1.destroy()
    show_details.destroy()
    l2.destroy()
    add_staff.destroy()
    del_staff.destroy()
    ex.destroy()
    cur.execute("SELECT COUNT(*) FROM customer")
    work=cur.fetchone()[0]
    ow1=Label(root,text=f"Total number of work: {work}",font=4)
    ow1.grid(row=0,column=0,padx=3,pady=3)
    cur.execute("SELECT COUNT(*) FROM customer WHERE status='complete'")
    com=cur.fetchone()[0]
    done=Label(root,text=f"Total work complete: {com}",font=4)
    done.grid(row=1,column=0,padx=3,pady=3)
    cur.execute("SELECT COUNT(*) FROM customer WHERE status='pending'")
    pend=cur.fetchone()[0]
    pen=Label(root,text=f"Total pending work: {pend}",font=4)
    pen.grid(row=2,column=0,padx=3,pady=3)
    cur.execute("SELECT staff_id,COUNT(*) AS no_of_work FROM details GROUP BY staff_id;")
    row=cur.fetchall()
    head=["staff_id","no_of_work"]
    l1=Label(root,text="performance of the staff:",font=4)
    l1.grid(row=3,column=0,padx=5,pady=5)
    box=Text(root,height=9,width=30)
    box.insert(1.0,tabulate(row, headers=head, tablefmt="psql"))
    box["state"]=DISABLED
    box.grid(row=4,column=0,padx=5,pady=5)
    data_vis=Label(root,text="data visualization: ",font=3)
    data_vis.grid(row=5,column=0)
    value=["products","rush week"]
    opt=ttk.Combobox(root,values=value)
    opt.grid(row=5,column=1)
    opt.set("choose option")
    sh=Button(root,text="show charts",command=show,height=2,width=9)
    sh.grid(row=6,column=0)
    save=Button(root,text="Save",command=save_data,height=2,width=9)
    save.grid(row=6,column=1,padx=5,pady=5)
    ow_b3=Button(root,text="Back",height=2,width=8,command=ow_back3)
    ow_b3.grid(row=7,column=0,padx=5,pady=5)
    ex11=Button(root,text="exit",height=2,width=8,command=root.destroy)
    ex11.grid(row=7,column=1,padx=5,pady=5)

def back_to_main():
    global l1,st_name,staff_name,guardian,guardian_name,ph,ph_num,aadher,aadher_num,staff_id,staff_id_l,password,password_l,ex,ow_b11,submit
    global ow_b1,show_details,l2,add_staff,del_staff,ex
    global ow_b,l,l1,own,staf,cust,ex,ow_name1,ow_name,ow_pass1,ow_pass,f1,sub
    l1.destroy()
    st_name.destroy()
    staff_name.destroy()
    guardian.destroy()
    guardian_name.destroy()
    ph.destroy()
    ph_num.destroy()
    aadher.destroy()
    aadher_num.destroy()
    staff_id.destroy()
    staff_id_l.destroy()
    password.destroy()
    password_l.destroy()
    ex.destroy()
    ow_b11.destroy()
    submit.destroy()
    

    root.title("details")
    l2=Label(root,text="Choose option: ",font=7)
    l2.grid(row=0,column=0)

    show_details=Button(root,text="Show Details",height=3,width=50,bg="yellow",fg="red",command=details)
    show_details.grid(row=2,column=0,pady=10,padx=90)


    add_staff=Button(root,text="Add Staff",command=add_staff_det,bg="yellow",fg="red",height=3,width=50)
    add_staff.grid(row=3,column=0,pady=10)


    del_staff=Button(root,text="Remove Staff",height=3,width=50,bg="yellow",fg="red",command=del_staff_det)
    del_staff.grid(row=4,column=0,pady=10)


    ex=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
    ex.grid(row=6,column=0,padx=30)

    ow_b1=Button(root,text="Back",height=2,width=8,command=ow_back2)
    ow_b1.grid(row=5,column=0,pady=10,padx=1)
    

def add_details():
    global staff_name,guardian_name,ph_num,aadher_num,staff_id,password
    data=[]
    try:
        name=staff_name.get(1.0,END).strip()
        if name=="":
            raise NameError("Name not given")
        else:
            for i in name:
                if not (i.isalpha() or i.isspace()):
                    raise NameError("enter proper name")
        gname=guardian_name.get(1.0,END).strip()
        if gname=="":
            raise NameError("guardian Name not given")
        else:
            for i in gname:
                if not (i.isalpha() or i.isspace()):
                    raise NameError("enter proper guardian name")
        phn=ph_num.get(1.0,END).strip()
        if phn=="":
            raise NameError("Contact number not given")
        elif not len(phn)==10:
            messagebox.showwarning("Warning","not exactly 10 digit")
        else:
            for i in phn:
                if not i.isdigit():
                    raise NameError("enter proper contact number")
        ad=aadher_num.get(1.0,END).strip()
        if ad=="":
            raise NameError("aadher number not given")
        elif not len(ad)==12:
            messagebox.showwarning("Warning","not exactly 12 digit")
        else:
            for i in ad:
                if not i.isdigit():
                    raise NameError("enter proper aadher number")
        st=staff_id.get(1.0,END).strip()
        if st=="":
            raise NameError("staff id not given")
        else:
            for i in st:
                if not i.isdigit():
                    raise NameError("please enter staff id")
        ps=password.get(1.0,END).strip()
        if ps=="":
            messagebox.showwarning("Warning","please enter a password")
    except NameError as e:
        messagebox.showwarning("Warning",e)
    except Exception as e:
        messagebox.showerror("ERROR",e)
    else:
       if (name and gname and phn and ad and st and ps):
            per=messagebox.askokcancel("confirmation","do you want to add ??")
            if per==True:
                data.append(name)
                data.append(gname)
                data.append(phn)
                data.append(ad)
                data.append(st)
                data.append(ps)
                n_data=tuple(data)
                print(n_data)
                cur.execute("INSERT INTO staff(name,guardian_name,contact,aadhar_num,staff_id,password)VALUES(%s,%s,%s,%s,%s,%s)",n_data)
                my_db.commit()
                staff_name.delete(1.0,END)
                guardian_name.delete(1.0,END)
                ph_num.delete(1.0,END)
                aadher_num.delete(1.0,END)
                staff_id.delete(1.0,END)
                password.delete(1.0,END)
                messagebox.showinfo("Data entry","Succesfully staff aded")


def add_staff_det():
    global ow_b1,show_details,l2,add_staff,del_staff,ex
    global l1,st_name,staff_name,guardian,guardian_name,ph,ph_num,aadher,aadher_num,staff_id,staff_id_l,password,password_l,ex,ow_b11,submit
    global ow_b,l,l1,own,staf,cust,ex,ow_name1,ow_name,ow_pass1,ow_pass,f1,sub
    ow_b1.destroy()
    show_details.destroy()
    l2.destroy()
    add_staff.destroy()
    del_staff.destroy()
    ex.destroy()
    root.title("add new staff")
    l1=Label(root,text="add new staff",font=7)
    l1.grid(row=0,column=1,padx=3,pady=3)
    st_name=Label(root,text="Name: ",font=7)
    st_name.grid(row=1,column=0,padx=3,pady=3)
    staff_name=Text(root,height=2,width=30)
    staff_name.grid(row=1,column=1,padx=3,pady=3)
    guardian=Label(root,text="Guardian name: ",font=7)
    guardian.grid(row=2,column=0,padx=3,pady=3)
    guardian_name=Text(root,height=2,width=30)
    guardian_name.grid(row=2,column=1,padx=3,pady=3)
    ph=Label(root,text="Contact no: ",font=7)
    ph.grid(row=3,column=0,padx=3,pady=3)
    ph_num=Text(root,height=2,width=30)
    ph_num.grid(row=3,column=1,padx=3,pady=3)
    aadher=Label(root,text="Aadhar number: ",font=7)
    aadher.grid(row=4,column=0,padx=3,pady=3)
    aadher_num=Text(root,height=2,width=30)
    aadher_num.grid(row=4,column=1,padx=3,pady=3)
    staff_id_l=Label(root,text="Staff id: ",font=7)
    staff_id_l.grid(row=5,column=0,padx=3,pady=3)
    staff_id=Text(root,height=2,width=30)
    staff_id.grid(row=5,column=1,padx=3,pady=3)
    password_l=Label(root,text="Password: ",font=7)
    password_l.grid(row=6,column=0,padx=3,pady=3)
    password=Text(root,height=2,width=30)
    password.grid(row=6,column=1,padx=3,pady=3)

    ex=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
    ex.grid(row=7,column=2,padx=30)
    submit=Button(root,text="Add staff",height=2,width=7,fg="red",bg="white",command=add_details)
    submit.grid(row=7,column=0,padx=30)

    ow_b11=Button(root,text="Back",height=2,width=8,command=back_to_main)
    ow_b11.grid(row=7,column=1,pady=10,padx=1)

def back_from_remove():
   global ow_b,l,l1,own,staf,cust,ex,ow_name1,ow_name,ow_pass1,ow_pass,f1,sub
   global ow_b1,show_details,l2,add_staff,del_staff,ex
   global l12,t,rem_l,rem,t,r,b,ex,back
   global ow_b,l,l1,own,staf,cust,ex,ow_name1,ow_name,ow_pass1,ow_pass,f1,sub
   l12.destroy()
   t.destroy()
   rem.destroy()
   rem_l.destroy()
   t.destroy()
   r.destroy()
   b.destroy()
   ex.destroy()
   back.destroy()
   root.title("details")
   root.geometry("500x400")
   #root.maxsize(500,400)
   root.minsize(500,400)
   l2=Label(root,text="Choose option: ",font=7)
   l2.grid(row=0,column=0)

   show_details=Button(root,text="Show Details",height=3,width=50,bg="yellow",fg="red",command=details)
   show_details.grid(row=2,column=0,pady=10,padx=90)
   add_staff=Button(root,text="Add Staff",command=add_staff_det,bg="yellow",fg="red",height=3,width=50)
   add_staff.grid(row=3,column=0,pady=10)
   del_staff=Button(root,text="Remove Staff",height=3,width=50,bg="yellow",fg="red",command=del_staff_det)
   del_staff.grid(row=4,column=0,pady=10)
   ex=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
   ex.grid(row=6,column=0,padx=30)
   ow_b1=Button(root,text="Back",height=2,width=8,command=ow_back2)
   ow_b1.grid(row=5,column=0,pady=10,padx=1)
    

def remove():
    global rem,t
    try:
        staff_to_rem=rem.get(1.0,END).strip()
        cur.execute(f"SELECT COUNT(*) from staff where staff_id={staff_to_rem}")
        k=cur.fetchone()[0]
        if staff_to_rem=="":
            raise NameError("Staff id not given")
        elif k==0:
            raise ValueError(f"staff_id:{staff_to_rem}not exist")
    except NameError as e:
        messagebox.showwarning("WARNING",e)
    except ValueError as e:
        messagebox.showerror("ERROR",e)
    except Exception as e:
        messagebox.showerror("ERROR",e)
    else:
        cur.execute(f"DELETE from staff where staff_id={staff_to_rem}")
        my_db.commit()
        t["state"]=NORMAL
        t.delete(1.0,END)
        cur.execute("SELECT * from staff")
        data=cur.fetchall()
        head=["sl_no","name","guardian_name","contact","aadhar_num","staff_id","password"]
        t.insert(1.0,tabulate(data,headers=head,tablefmt="psql"))
        t["state"]=DISABLED
        rem.delete(1.0,END)
        messagebox.showinfo("INFO",f"staff id: {staff_to_rem} succesfully removed")
    
def del_staff_det():
    global ow_b,l,l1,own,staf,cust,ex,ow_name1,ow_name,ow_pass1,ow_pass,f1,sub
    global ow_b1,show_details,l2,add_staff,del_staff,ex
    global l12,t,rem_l,rem,t,r,b,ex,back
    global ow_b,l,l1,own,staf,cust,ex,ow_name1,ow_name,ow_pass1,ow_pass,f1,sub
    ow_b1.destroy()
    show_details.destroy()
    l2.destroy()
    add_staff.destroy()
    del_staff.destroy()
    ex.destroy()
    root.title("remove staff")
    root.geometry("800x450")
    root.maxsize(800,450)
    cur.execute("SELECT COUNT(*) from staff")
    num=cur.fetchone()[0]
    l12=Label(root,text=f"Total number of staff: {num} ",font=5)
    l12.grid(row=0,column=0,padx=5,pady=5)
    cur.execute("SELECT * from staff")
    data=cur.fetchall()
    head=["sl_no","name","guardian_name","contact","aadhar_num","staff_id","password"]
    t=Text(root,height=10,width=100)
    t.grid(row=1,column=0)
    t.insert(1.0,tabulate(data,headers=head,tablefmt="psql"))
    t["state"]=DISABLED
    r=Label(root,text="remove staff: ",font=3)
    r.grid(row=2,column=0)
    rem_l=Label(root,text="enter the staff id to remove: ",font=3)
    rem_l.grid(row=3,column=0)
    rem=Text(root,height=2,width=10)
    rem.grid(row=4,column=0)
    
    b=Button(root,text="Remove",height=2,width=7,fg="yellow",bg="green",command=remove)
    b.grid(row=5,column=0,padx=30)

    back=Button(root,text="Back",height=2,width=8,command=back_from_remove)
    back.grid(row=6,column=0,pady=10,padx=1)

    ex=Button(root,text="Exit",height=2,width=8,command=root.destroy)
    ex.grid(row=7,column=0,pady=10,padx=1)

    
def ow_main():
    global ow_b,l,l1,own,staf,cust,ex,ow_name1,ow_name,ow_pass1,ow_pass,f1,sub
    global ow_b1,show_details,l2,add_staff,del_staff,ex
    global ow_b,l,l1,own,staf,cust,ex,ow_name1,ow_name,ow_pass1,ow_pass,f1,sub
    f1.destroy()
    ow_name1.destroy()
    ow_name.destroy()
    ow_pass.destroy()
    ow_pass1.destroy()
    ow_b.destroy()
    sub.destroy()
    ex.destroy()
    root.title("details")
    l2=Label(root,text="Choose option: ",font=7)
    l2.grid(row=0,column=0)

    show_details=Button(root,text="Show Details",height=3,width=50,bg="yellow",fg="red",command=details)
    show_details.grid(row=2,column=0,pady=10,padx=90)


    add_staff=Button(root,text="Add Staff",command=add_staff_det,bg="yellow",fg="red",height=3,width=50)
    add_staff.grid(row=3,column=0,pady=10)


    del_staff=Button(root,text="Remove Staff",height=3,width=50,bg="yellow",fg="red",command=del_staff_det)
    del_staff.grid(row=4,column=0,pady=10)


    ex=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
    ex.grid(row=6,column=0,padx=30)

    ow_b1=Button(root,text="Back",height=2,width=8,command=ow_back2)
    ow_b1.grid(row=5,column=0,pady=10,padx=1)
    
def check():
    global own_name,own_pass
    try:
        name=ow_name.get(1.0,END).strip().lower()
        passw=ow_pass.get(1.0,END).strip()
        if name=="":
            raise NameError("please enter name")
        elif passw=="":
            raise ValueError("please enter password")
    except NameError as e:
        messagebox.showerror("warning",e)
    except ValueError as v:
        messagebox.showerror("warning",v)
    else:
        if name==own_name and passw==own_pass:
            messagebox.showinfo("Login"," Succesfully Done")
            ow_main()
        else:
            messagebox.showwarning("LOgin","Please enter a valid name and password")


def owner():
    global ow_b,l,l1,own,staf,cust,ex,ow_name1,ow_name,ow_pass1,ow_pass,f1,sub
    l.destroy()
    l1.destroy()
    own.destroy()
    staf.destroy()
    cust.destroy()
    ex.destroy()
    
    root.title("owner_login")
    f1=Label(root,text="Owner Login:",font=10)
    f1.grid(row=0,column=0,pady=10,padx=50)
    ow_name1=Label(root,text="Enter your name: ",font=7)
    ow_name1.grid(row=1,column=0,pady=20)
    ow_name=Text(root,height=2,width=30)
    ow_name.grid(row=1,column=1)
    ow_pass1=Label(root,text="Enter your password: ",font=7)
    ow_pass1.grid(row=2,column=0,pady=20)
    ow_pass=Text(root,height=2,width=30)
    ow_pass.grid(row=2,column=1)
    ow_b=Button(root,text="Back",height=2,width=8,command=ow_back1)
    ow_b.grid(row=3,column=0,pady=10,padx=1)
    sub=Button(root,text="SUBMIT",height=2,width=7,command=check)
    sub.grid(row=3,column=1,pady=10)
    ex=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
    ex.grid(row=4,column=0,pady=10)

#end of owner section
#start of staff section
def st_back1():
    global l,l1,own,staf,cust,ex
    global sl1,st_log_id_l,st_log_id,st_log_pass,st_log_pass_l,ow_b,sub_st,exs1
    sl1.destroy()
    st_log_id_l.destroy()
    st_log_id.destroy()
    st_log_pass.destroy()
    st_log_pass_l.destroy()
    ow_b.destroy()
    sub_st.destroy()
    exs1.destroy()
    l=Label(root,text="welcome to abc service center",font=20)
    l.grid(row=0,column=0,padx=100,pady=10)
    l1=Label(root,text="****************************************",font=20)
    l1.grid(row=1,column=0,padx=100,pady=10)
    own=Button(root,text="Owner",height=3,width=50,bg="yellow",fg="red",command=owner)
    own.grid(row=2,column=0,pady=10,padx=90)
    staf=Button(root,text="Staff",height=3,width=50,bg="yellow",fg="red",command=staff)
    staf.grid(row=3,column=0,pady=10)
    cust=Button(root,text="Customer",height=3,width=50,bg="yellow",fg="red",command=customer)
    cust.grid(row=4,column=0,pady=10)
    ex=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
    ex.grid(row=5,column=0,padx=30)
def st_back2():
    global l,l1,own,staf,cust,ex
    global sl1,st_log_id_l,st_log_id,st_log_pass,st_log_pass_l,ow_b,sub_st,exs1
    global st1,pen,list_of_pending,det,sel,cch,up,st_1,exs2
    root.geometry("500x400")
    st1.destroy()
    pen.destroy()
    list_of_pending.destroy()
    det.destroy()
    sel.destroy()
    cch.destroy()
    up.destroy()
    st_1.destroy()
    exs2.destroy()
    root.title("Login page")
    sl1=Label(root,text="Staff login page: ",font=5)
    sl1.grid(row=0,column=1,padx=3,pady=3)
    st_log_id_l=Label(root,text="Enter staff id: ",font=3)
    st_log_id_l.grid(row=1,column=0,padx=10,pady=10)
    st_log_id=Text(root,height=2,width=30)
    st_log_id.grid(row=1,column=1,padx=10,pady=10)
    st_log_pass_l=Label(root,text="Enter Password: ",font=3)
    st_log_pass_l.grid(row=2,column=0,padx=10,pady=10)
    st_log_pass=Text(root,height=2,width=30)
    st_log_pass.grid(row=2,column=1,padx=10,pady=10)

    ow_b=Button(root,text="Back",height=2,width=8,command=st_back1)
    ow_b.grid(row=3,column=1,pady=10,padx=10)
    sub_st=Button(root,text="Submit",height=2,width=8,command=check_staff)
    sub_st.grid(row=4,column=1,padx=10,pady=10)
    exs1=Button(root,text="Exit",height=2,width=8,command=root.destroy)
    exs1.grid(row=5,column=1,padx=10,pady=10)


def update():
    global ch,case_id_1,list_of_pending,det,id_staff
    k=ch.get()
    if k==1:
        cur.execute(f"UPDATE customer SET status='complete' where case_id={case_id_1}")
        my_db.commit()
        det.delete(1.0,END)
        list_of_pending.delete(0,END)
        cur.execute("SELECT case_id FROM customer where status='pending'")
        for i,value in enumerate(cur):
            list_of_pending.insert(i,value)
        cur.execute("INSERT INTO details(staff_id,case_id,date_of_service)VALUES(%s,%s,now())",(id_staff,case_id_1))
        my_db.commit()
        det.delete(1.0,END)
        messagebox.showinfo("INFO","succesfully data updated ")

    print(k)


def ins_data():
    global list_of_pending,det,case_id_1
    k=list_of_pending.curselection()
    l=list_of_pending.get(k[0])
    case_id_1=l[0]
    det.delete(1.0,END)
    hed=["product_type","product_details"]
    cur.execute(f"SELECT product_type,product_details FROM customer where case_id={case_id_1}")
    data=cur.fetchall()
    det.insert(1.0,tabulate(data,headers=hed,tablefmt="psql"))
def work():
    global sl1,st_log_id_l,st_log_id,st_log_pass,st_log_pass_l,ow_b,sub_st,exs1
    global st1,pen,list_of_pending,det,sel,cch,up,st_1,exs2,ch
    id_staff=st_log_id.get(1.0,END).strip()
    root.geometry("750x500")
    sl1.destroy()
    st_log_id.destroy()
    st_log_id_l.destroy()
    st_log_pass.destroy()
    st_log_pass_l.destroy()
    ow_b.destroy()
    sub_st.destroy()
    ex.destroy()
    exs1.destroy()
    root.title(f"staff-id:{id_staff}")
    st1=Label(root,text="Details: ",font=4)
    st1.grid(row=0,column=1,padx=4,pady=4)
    pen=Label(root,text="Pending works: ",font=3)
    pen.grid(row=0,column=0,padx=1,pady=3)
    list_of_pending=Listbox(root,height=16,width=22)
    list_of_pending.grid(row=1,column=0)
    cur.execute("SELECT case_id FROM customer where status='pending'")
    for i,value in enumerate(cur):
        list_of_pending.insert(i,value)
    det=Text(root,height=10,width=60)
    det.grid(row=1,column=1)
    sel=Button(root,text="show",height=2,width=8,command=ins_data)
    sel.grid(row=2,column=0,padx=3,pady=3)
    ch=IntVar()
    cch=Checkbutton(root,text="succesfully done",variable=ch)
    cch.grid(row=2,column=1,padx=3,pady=3)
    up=Button(root,text="Update data",command=update,height=2,width=8)
    up.grid(row=3,column=1)
    st_1=Button(root,text="Back",height=2,width=8,command=st_back2)
    st_1.grid(row=3,column=2,pady=3,padx=3)
    exs2=Button(root,text="Exit",height=2,width=8,command=root.destroy)
    exs2.grid(row=4,column=1,pady=3,padx=3)


def check_staff():
    global sl1,st_log_id_l,st_log_id,st_log_pass,st_log_pass_l,ow_b,sub_st,exs1,id_staff
    try:
        id_staff=st_log_id.get(1.0,END).strip()
        pass_staff=st_log_pass.get(1.0,END).strip()
        if id_staff=="":
            messagebox.showwarning("WARNING","staff id not given")
        elif pass_staff=="":
            messagebox.showwarning("WARNING","Password  not given")
    except Exception as e:
        messagebox.showerror("Error",e)
    else:
        cur.execute(f"SELECT COUNT(*) FROM staff where staff_id={id_staff} and password={pass_staff}")
        k=cur.fetchone()[0]
        if k==0:
            messagebox.showerror("ERROR","please enter correct id and password")
        else:
            messagebox.showinfo("INFO","Succesfully logged in")
            work()

def staff():
    global l,l1,own,staf,cust,ex
    global sl1,st_log_id_l,st_log_id,st_log_pass,st_log_pass_l,ow_b,sub_st,exs1
    l.destroy()
    l1.destroy()
    own.destroy()
    staf.destroy()
    cust.destroy()
    ex.destroy()
    root.title("Login page")
    sl1=Label(root,text="Staff login page: ",font=5)
    sl1.grid(row=0,column=1,padx=3,pady=3)
    st_log_id_l=Label(root,text="Enter staff id: ",font=3)
    st_log_id_l.grid(row=1,column=0,padx=10,pady=10)
    st_log_id=Text(root,height=2,width=30)
    st_log_id.grid(row=1,column=1,padx=10,pady=10)
    st_log_pass_l=Label(root,text="Enter Password: ",font=3)
    st_log_pass_l.grid(row=2,column=0,padx=10,pady=10)
    st_log_pass=Text(root,height=2,width=30)
    st_log_pass.grid(row=2,column=1,padx=10,pady=10)

    ow_b=Button(root,text="Back",height=2,width=8,command=st_back1)
    ow_b.grid(row=3,column=1,pady=10,padx=10)
    sub_st=Button(root,text="Submit",height=2,width=8,command=check_staff)
    sub_st.grid(row=4,column=1,padx=10,pady=10)
    exs1=Button(root,text="Exit",height=2,width=8,command=root.destroy)
    exs1.grid(row=5,column=1,padx=10,pady=10)
#end of staff
#start of customer
def cust_back1():
    global ow_b,l,l1,own,staf,cust,ex
    global s2,show_status,repair,exc1,cu_b
    s2.destroy()
    show_status.destroy()
    repair.destroy()
    exc1.destroy()
    cu_b.destroy()
    l=Label(root,text="welcome to abc service center",font=20)
    l.grid(row=0,column=0,padx=100,pady=10)
    l1=Label(root,text="****************************************",font=20)
    l1.grid(row=1,column=0,padx=100,pady=10)
    own=Button(root,text="Owner",height=3,width=50,bg="yellow",fg="red",command=owner)
    own.grid(row=2,column=0,pady=10,padx=90)
    staf=Button(root,text="Staff",height=3,width=50,bg="yellow",fg="red",command=staff)
    staf.grid(row=3,column=0,pady=10)
    cust=Button(root,text="Customer",height=3,width=50,bg="yellow",fg="red",command=customer)
    cust.grid(row=4,column=0,pady=10)
    ex=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
    ex.grid(row=5,column=0,padx=30)

def back_from_status():
    global s2,show_status,repair,exc1,cu_b
    global c1,case_l,case_check,sub_s,but,exc2
    c1.destroy()
    case_l.destroy()
    case_check.destroy()
    sub_s.destroy()
    but.destroy()
    exc2.destroy()
    root.title("details")
    s2=Label(root,text="Choose option: ",font=7)
    s2.grid(row=0,column=0)
    show_status=Button(root,text="Show Status",height=3,width=50,bg="yellow",fg="red",command=status)
    show_status.grid(row=1,column=0,pady=10,padx=90)
    repair=Button(root,text="Repair a Product",command=report,bg="yellow",fg="red",height=3,width=50)
    repair.grid(row=2,column=0,pady=10)
    exc1=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
    exc1.grid(row=4,column=0,padx=30)
    
    cu_b=Button(root,text="Back",height=2,width=8,command=cust_back1)
    cu_b.grid(row=3,column=0,pady=10,padx=1)

def status_s():
    global case_check
    try:
        k=case_check.get(1.0,END).strip()
        if k=="":
            messagebox.showwarning("WARNING","Please enter the Case id")
        else:
            cur.execute(f"SELECT COUNT(*) from customer where case_id={k}")
            l=cur.fetchone()[0]
            if l==0:
                raise ValueError("case id not match")
    except ValueError as e:
        messagebox.showerror("ERROR",e)
    except Exception as e:
        messagebox.showerror("Error",e)
    else:
        cur.execute(f"SELECT status from customer where case_id={k}")
        ti=cur.fetchone()[0]
        messagebox.showinfo("INFO",f"status: {ti}")

def status():
    global ow_b,l,l1,own,staf,cust,ex
    global s2,show_status,repair,exc1,cu_b
    global c1,case_l,case_check,sub_s,but,exc2
    s2.destroy()
    show_status.destroy()
    repair.destroy()
    exc1.destroy()
    cu_b.destroy()
    root.title("__Check status__")
    c1=Label(root,text="Check status of your product",font=5)
    c1.grid(row=0,column=0,padx=4,pady=4)
    case_l=Label(root,text="Enter Your Case Id: ",font=3)
    case_l.grid(row=1,column=0,padx=4,pady=4)
    case_check=Text(root,height=3,width=10)
    case_check.grid(row=1,column=1,padx=4,pady=4)
    sub_s=Button(root,text="Check",height=3,width=8,command=status_s)
    sub_s.grid(row=2,column=0,padx=5,pady=5)
    but=Button(root,text="Back",height=3,width=8,command=back_from_status)
    but.grid(row=3,column=0,padx=5,pady=5)
    exc2=Button(root,text="Exit",height=3,width=8,command=root.destroy)
    exc2.grid(row=4,column=0,padx=5,pady=5)

def back_from_report():
    global s2,show_status,repair,exc1,cu_b
    global c12,cus_name_l,cus_name,cus_ph,cus_ph_l,cus_email_l,cus_email,product,product_l,deta_l,deta,back_c,exc13,add
    root.geometry("500x400")
    c12.destroy()
    cus_name_l.destroy()
    cus_name.destroy()
    cus_ph.destroy()
    cus_ph_l.destroy()
    cus_email_l.destroy()
    cus_email.destroy()
    product.destroy()
    product_l.destroy()
    deta_l.destroy()
    deta.destroy()
    back_c.destroy()
    exc13.destroy()
    add.destroy()
    root.title("details")
    s2=Label(root,text="Choose option: ",font=7)
    s2.grid(row=0,column=0)
    show_status=Button(root,text="Show Status",height=3,width=50,bg="yellow",fg="red",command=status)
    show_status.grid(row=1,column=0,pady=10,padx=90)
    repair=Button(root,text="Repair a Product",command=report,bg="yellow",fg="red",height=3,width=50)
    repair.grid(row=2,column=0,pady=10)
    exc1=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
    exc1.grid(row=4,column=0,padx=30)
    
    cu_b=Button(root,text="Back",height=2,width=8,command=cust_back1)
    cu_b.grid(row=3,column=0,pady=10,padx=1)

def submit_for_case():
    global cus_name,cus_ph,cus_email,product,deta
    try:
        name=cus_name.get(1.0,END).strip()
        if name=="":
            raise NameError("name not given")
        else:
            for i in name:
                if not (i.isalpha() or i.isspace()):
                    raise NameError("enter proper name")
        contact=cus_ph.get(1.0,END).strip()
        if contact=="":
            raise NameError("contact number not given")
        elif not len(contact)==10:
            raise ValueError("contact number not exactly 10 digit")
        else:
            for i in contact:
                if not i.isdigit():
                    raise ValueError("enter proper contact number")
        mail=cus_email.get(1.0,END).strip()
        if mail=="":
            raise NameError("email not given")
        elif not mail.endswith("@gmail.com") or mail.endswith(".in"):
            raise NameError("enter propoper mail")
        type=product.get(1.0,END).strip()
        if type=="":
            raise NameError("Enter the product type")
        details=deta.get(1.0,END).strip()
        if details=="":
            raise NameError("enter the details of the product")
    except NameError as e:
        messagebox.showwarning("WARNING",e)
    except ValueError as e:
        messagebox.showerror("ERROR",e)
    except Exception as e:
        messagebox.showwarning("WARNING",e)
    else:
        k=messagebox.askokcancel("save","want to add the details ??")
        if k==True:
            data=[]
            data.append(name)
            data.append(contact)
            data.append(mail)
            data.append(type)
            data.append(details)
            new=tuple(data)
            cur.execute("INSERT INTO customer(name,contact_no,email_id,product_type,product_details,time_of_submit)VALUES(%s,%s,%s,%s,%s,now())",new)
            my_db.commit()
            cus_name.delete(1.0,END)
            cus_ph.delete(1.0,END)
            cus_email.delete(1.0,END)
            product.delete(1.0,END)
            deta.delete(1.0,END)
            cur.execute("SELECT case_id FROM customer WHERE name = %s", (name,))
            kk = cur.fetchone()[0]
            messagebox.showinfo("INFO",f"your report succesfylly submited and case id is: {kk}.\n please remember case id for future need ")
                
def report():
    global ow_b,l,l1,own,staf,cust,ex
    global s2,show_status,repair,exc1,cu_b
    global c12,cus_name_l,cus_name,cus_ph,cus_ph_l,cus_email_l,cus_email,product,product_l,deta_l,deta,back_c,exc13,add
    root.geometry("600x500")
    s2.destroy()
    show_status.destroy()
    repair.destroy()
    exc1.destroy()
    cu_b.destroy()
    root.title("Add New Case")
    c12=Label(root,text="LODGE NEW CASE: ")
    c12.grid(row=0,column=1,padx=3,pady=3)
    cus_name_l=Label(root,text="Name: ",font=7)
    cus_name_l.grid(row=1,column=0,padx=3,pady=3)
    cus_name=Text(root,height=2,width=30)
    cus_name.grid(row=1,column=1,padx=3,pady=3)
    cus_ph_l=Label(root,text="Contact Number: ",font=7)
    cus_ph_l.grid(row=2,column=0,padx=3,pady=3)
    cus_ph=Text(root,height=2,width=30)
    cus_ph.grid(row=2,column=1,padx=3,pady=3)
    cus_email_l=Label(root,text="Email id: ",font=7)
    cus_email_l.grid(row=3,column=0,padx=3,pady=3)
    cus_email=Text(root,height=2,width=30)
    cus_email.grid(row=3,column=1,padx=3,pady=3)
    product_l=Label(root,text="Product Type(laptop,ph etc): ",font=7)
    product_l.grid(row=4,column=0,padx=3,pady=3)
    product=Text(root,height=2,width=30)
    product.grid(row=4,column=1,padx=3,pady=3)
    deta_l=Label(root,text="Problem Details: ",font=5)
    deta_l.grid(row=5,column=0,padx=3,pady=3)
    deta=Text(root,height=7,width=30)
    deta.grid(row=5,column=1,padx=3,pady=3)
    back_c=Button(root,text="Back",height=2,width=8,command=back_from_report)
    back_c.grid(row=6,column=0,pady=10,padx=10)
    add=Button(root,text="Submit",height=2,width=8,command=submit_for_case)
    add.grid(row=6,column=1,padx=10,pady=10)
    exc13=Button(root,text="Exit",height=2,width=8,command=root.destroy)
    exc13.grid(row=7,column=0,padx=10,pady=10)
   

def customer():
    global ow_b,l,l1,own,staf,cust,ex
    global s2,show_status,repair,exc1,cu_b
    l.destroy()
    l1.destroy()
    own.destroy()
    staf.destroy()
    cust.destroy()
    ex.destroy()
    root.title("details")
    s2=Label(root,text="Choose option: ",font=7)
    s2.grid(row=0,column=0)
    show_status=Button(root,text="Show Status",height=3,width=50,bg="yellow",fg="red",command=status)
    show_status.grid(row=1,column=0,pady=10,padx=90)
    repair=Button(root,text="Repair a Product",command=report,bg="yellow",fg="red",height=3,width=50)
    repair.grid(row=2,column=0,pady=10)
    exc1=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
    exc1.grid(row=4,column=0,padx=30)
    
    cu_b=Button(root,text="Back",height=2,width=8,command=cust_back1)
    cu_b.grid(row=3,column=0,pady=10,padx=1)

own=Button(root,text="Owner",height=3,width=50,bg="yellow",fg="red",command=owner)
own.grid(row=2,column=0,pady=10,padx=90)


staf=Button(root,text="Staff",height=3,width=50,bg="yellow",fg="red",command=staff)
staf.grid(row=3,column=0,pady=10)


cust=Button(root,text="Customer",height=3,width=50,bg="yellow",fg="red",command=customer)
cust.grid(row=4,column=0,pady=10)


ex=Button(root,text="Exit",height=2,width=7,fg="red",bg="white",command=root.destroy)
ex.grid(row=5,column=0,padx=30)

root.mainloop()