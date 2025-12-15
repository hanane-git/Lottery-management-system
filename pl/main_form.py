from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import random
from BE.mojodiatha import User
from BE.mojodiatha import Loan
from BE.mojodiatha import Ghorekeshi
from BLL.blravabet import BLuser
from BLL.blravabet import BLloan
from BLL.blravabet import BLGhorekeshi

class MyApp(Frame):
    def __init__(self,screen):
        super().__init__()
        self.master=screen
        self.dic_lbl = {
            "bg":"#FFB5A7",
            "font":20,
            "fg":"#472D30"
        }
        self.dic_btn = {
            "font":20,
            "bg":"#723D46",
            "fg":"#FCD5CE",
            "width":16
        }
        self.dic_txt = {
            "font":20,
            "fg":"#03045E",
            "justify":"left"
        }
        self.style=ttk.Style()
        self.style.configure("Treeview", font=("B Nazanin", 14))
        self.style.configure("Treeview.Heading", font=("B Titr", 16))
        self.create_widgets()
        self.load_table()
        self.load_table2()
        self.get_data()
        self.get_data2()
        self.selected_id=None

    def create_widgets(self):
#mainPage
        self.lbl=Label(self.master,text="WELCOME TO THE LOTTERY",bg="#FFB5A7",fg="#590D22",font=20)
        self.lbl.place(relx=0.35,rely=0.2)

        self.main_mno=Menu(self.master)
        self.master.configure(menu=self.main_mno)

        self.user_mno=Menu(self.main_mno,tearoff=0)
        self.main_mno.add_cascade(label="User",menu=self.user_mno)
        self.user_mno.add_command(label="Add User",command=self.show_frame)
        self.user_mno.add_separator()
        self.user_mno.add_command(label="Exit",command=self.master.destroy)

        self.loan_mno=Menu(self.main_mno,tearoff=0)
        self.main_mno.add_cascade(label="Loan",menu=self.loan_mno)
        self.loan_mno.add_command(label="Add Loan",command=self.show_frame3)

        self.raffle_mno=Menu(self.main_mno,tearoff=0)
        self.main_mno.add_cascade(label="Raffle",menu=self.raffle_mno)
        self.raffle_mno.add_command(label="Raffle",command=self.show_frame4)

        self.about_mno=Menu(self.main_mno,tearoff=0)
        self.main_mno.add_cascade(label="About Us",menu=self.about_mno)
        self.about_mno.add_command(label="about us",command=self.about)

#userFrame
        self.f1=Frame(self.master,bg="#6D2E46",width=700,height=600)

        Label(self.f1,text="Name",**self.dic_lbl).place(relx=0.1,rely=0.1)
        self.tvalname=StringVar()
        self.txtname=Entry(self.f1,textvariable=self.tvalname,**self.dic_txt)
        self.txtname.place(relx=0.2,rely=0.1)

        Label(self.f1,text="Email",**self.dic_lbl).place(relx=0.1,rely=0.2)
        self.tvalmail=StringVar()
        self.txtmail=Entry(self.f1,textvariable=self.tvalmail,**self.dic_txt)
        self.txtmail.place(relx=0.2,rely=0.2)

        Label(self.f1,text="Amount",**self.dic_lbl).place(relx=0.1,rely=0.3)
        self.tvalamount=StringVar()
        self.txtamount=Entry(self.f1,textvariable=self.tvalamount,**self.dic_txt)
        self.txtamount.place(relx=0.2,rely=0.3)

        self.btnsave=Button(self.f1,text="Save",**self.dic_btn,command=self.onclicksave)
        self.btnsave.place(relx=0.6,rely=0.2)

        self.tbl=ttk.Treeview(self.f1,columns=("Amount","Email","Name","ID"),show="headings",height=14)
        self.tbl.place(relx=0.18,rely=0.4)
        self.tbl.column("Amount",width=100,anchor=CENTER)
        self.tbl.heading("Amount",text="Amount")
        self.tbl.column("Email",width=200,anchor=CENTER)
        self.tbl.heading("Email",text="Email")
        self.tbl.column("Name",width=100,anchor=CENTER)
        self.tbl.heading("Name",text="Name")
        self.tbl.column("ID",width=50,anchor=CENTER)
        self.tbl.heading("ID",text="ID")
        self.load_table()

#loanframe
        self.f3=Frame(self.master,bg="#6D2E46",width=700,height=600)

        Label(self.f3,text="Name:",**self.dic_lbl).place(relx=0.05,rely=0.08)
        self.tvalnam=StringVar()
        self.txtnam=Entry(self.f3,textvariable=self.tvalnam,**self.dic_txt)
        self.txtnam.place(relx=0.15,rely=0.08)

        Label(self.f3,text="Amount",**self.dic_lbl).place(relx=0.05,rely=0.18)
        self.tvalamnt=StringVar()
        self.txtamnt=Entry(self.f3,textvariable=self.tvalamnt,**self.dic_txt)
        self.txtamnt.place(relx=0.15,rely=0.18)

        Label(self.f3,text="Installments",**self.dic_lbl).place(relx=0.02,rely=0.28)
        self.tvalinst=StringVar()
        self.txtinst=Entry(self.f3,textvariable=self.tvalinst,**self.dic_txt)
        self.txtinst.place(relx=0.15,rely=0.28)

        self.btncal=Button(self.f3,text="date from",width=10,font=20,bg="#723D46",fg="#FCD5CE",command=self.get_date)
        self.btncal.place(relx=0.02,rely=0.35)
        self.lblcal=Label(self.f3,text="")
        self.lblcal.place(relx=0.18,rely=0.35)

        self.btncal2=Button(self.f3,text="date to",width=10,font=20,bg="#723D46",fg="#FCD5CE",command=self.get_date2)
        self.btncal2.place(relx=0.35,rely=0.35)
        self.lblcal2=Label(self.f3,text="")
        self.lblcal2.place(relx=0.5,rely=0.35)

        self.btnreg=Button(self.f3,text="Register",**self.dic_btn,command=self.onclick)
        self.btnreg.place(relx=0.7,rely=0.05)
        self.btnedit=Button(self.f3,text="Edit",**self.dic_btn,command=self.onclickupdate)
        self.btnedit.place(relx=0.7,rely=0.15)
        self.btndel=Button(self.f3,text="Delete",**self.dic_btn,command=self.onclickdelete)
        self.btndel.place(relx=0.7,rely=0.25)

        self.tbl3=ttk.Treeview(self.f3,columns=("ID","Name","Amount","Installment","Date from","Date to"),show="headings",height=300)
        self.tbl3.place(relx=0,rely=0.45)
        self.tbl3.column("ID",width=50,anchor=CENTER)
        self.tbl3.heading("ID",text="ID")
        self.tbl3.column("Name",width=100,anchor=CENTER)
        self.tbl3.heading("Name",text="Name")
        self.tbl3.column("Amount",width=100,anchor=CENTER)
        self.tbl3.heading("Amount",text="Amount")
        self.tbl3.column("Installment",width=150,anchor=CENTER)
        self.tbl3.heading("Installment",text="Installment")
        self.tbl3.column("Date from",width=150,anchor=CENTER)
        self.tbl3.heading("Date from",text="Date from")
        self.tbl3.column("Date to",width=150,anchor=CENTER)
        self.tbl3.heading("Date to",text="Date to")
        self.tbl3.bind("<ButtonRelease-1>",self.onRowselect)

#Raffle_Frame
        self.f5=Frame(self.master,bg="#6D2E46",width=700,height=600)

        self.btnadd=Button(self.f5,text="Add User",**self.dic_btn,command=self.show_Ruffle)
        self.btnadd.place(relx=0.1,rely=0.15)

        self.lbl5=Label(self.f5,text="Loans:",**self.dic_lbl)
        self.lbl5.place(relx=0.1,rely=0.05)

        self.combo5=ttk.Combobox(self.f5,width=30)
        self.combo5.place(relx=0.2,rely=0.05)

        self.lbl6=Label(self.f5,text="Users:",**self.dic_lbl)
        self.lbl6.place(relx=0.6,rely=0.05)

        self.lstbox=Listbox(self.f5)
        self.lstbox.place(relx=0.7,rely=0.05)

        self.tbl4=ttk.Treeview(self.f5,columns=("Priority","User","Loan"),show="headings",height=300)
        self.tbl4.place(relx=0.13,rely=0.35)
        self.tbl4.column("Priority",width=100,anchor=CENTER)
        self.tbl4.heading("Priority",text="Priority")
        self.tbl4.column("User",width=200,anchor=CENTER)
        self.tbl4.heading("User",text="User")
        self.tbl4.column("Loan",width=200,anchor=CENTER)
        self.tbl4.heading("Loan",text="Loan")

#userpart_functions
    def onclicksave(self):
        if self.tvalname.get()=="":
            messagebox.showerror("Error","Please enter a name")
            self.txtname.focus_set()
        elif self.tvalmail.get()=="":
            messagebox.showerror("Error","Please enter an email")
            self.txtmail.focus_set()
        elif self.tvalamount.get()=="":
            messagebox.showerror("Error","Please enter an amount")
            self.txtamount.focus_set()

        objuser=User(self.tvalname.get(),self.tvalmail.get(),self.tvalamount.get())
        bl_user=BLuser()
        x=bl_user.Add(objuser)
        if x:
            messagebox.showinfo("Result","User Registered")
            users=bl_user.selectAll(User)
            for item in self.tbl.get_children():
                self.tbl.delete(item)
            for user in users:
                self.tbl.insert("","end",values=(user.Amount,user.Email,user.Name,user.ID))
                self.tvalname.set("")
                self.tvalmail.set("")
                self.tvalamount.set("")
                self.load_table()
            

    def load_table(self):
        bl_user=BLuser()
        users=bl_user.selectAll(User)
        for item in self.tbl.get_children():
            self.tbl.delete(item)
        for user in users:
            self.tbl.insert("","end",values=(user.Amount,user.Email,user.Name,user.ID))
            self.tvalname.set("")
            self.tvalmail.set("")
            self.tvalamount.set("")

#loanpart_functions
    def onclick(self):
        if self.tvalnam.get()=="":
            messagebox.showerror("Error","please enter a name")
            self.txtnam.focus_set()
        elif self.tvalamnt.get()=="":
            messagebox.showerror("Error","please enter an amount")
            self.txtamnt.focus_set()
        elif self.tvalinst.get()=="":
            messagebox.showerror("Error","please enter an installment")
            self.txtinst.focus_set()

        objloan=Loan(self.tvalnam.get(),self.tvalamnt.get(),self.tvalinst.get(),self.lblcal.cget("text"),self.lblcal2.cget("text"))
        bl_loan=BLloan()
        x=bl_loan.Add2(objloan)
        if x:
            messagebox.showinfo("Result","Registered")
            loans=bl_loan.readAll(Loan)
            for item in self.tbl3.get_children():
                self.tbl3.delete(item)
            for loan in loans:
                self.tbl3.insert("","end",values=(loan.ID,loan.Name,loan.Amount,loan.Installment,loan.Date_from,loan.Date_to))
                self.tvalnam.set("")
                self.tvalamnt.set("")
                self.tvalinst.set("")
                self.load_table2()
    def load_table2(self):
        bl_loan=BLloan()
        loans=bl_loan.readAll(Loan)
        for item in self.tbl3.get_children():
            self.tbl3.delete(item)
        for loan in loans:
            self.tbl3.insert("","end",values=(loan.ID,loan.Name,loan.Amount,loan.Installment,loan.Date_from,loan.Date_to))

    def onRowselect(self, event):
        selected_item=self.tbl3.selection()
        if selected_item:
            values=self.tbl3.item(selected_item, "values")
            self.selected_id=values[0]
            self.tvalnam.set(values[1])
            self.tvalamnt.set(values[2])
            self.tvalinst.set(values[3])

    def onclickdelete(self):
        if self.selected_id is None:
            messagebox.showwarning("Warning","please select a row")
        else:
            bl_loan=BLloan()
            x=bl_loan.Del(Loan,self.selected_id)
            if x:
                messagebox.showinfo("Result","successfully deleted")
                self.tvalnam.set("")
                self.tvalamnt.set("")
                self.tvalinst.set("")
                self.load_table2()

    def onclickupdate(self):
        if self.selected_id is None:
            messagebox.showinfo("Warning","please select a row")
        else:
            bl_loan=BLloan()
            x=bl_loan.update(Loan,self.selected_id,Name=self.tvalnam.get(),Amount=self.tvalamnt.get(),Installment=self.tvalinst.get())
            if x:
                messagebox.showinfo("Result","successfully updated")
                self.tvalnam.set("")
                self.tvalamnt.set("")
                self.tvalinst.set("")
                self.txtnam.focus_set()
                self.load_table2()
            else:
                  messagebox.showerror("Error","please select a row")

    def get_date(self):
        date=askstring("Date","please enter date like YYYY-MM-DD")
        if date:
            self.lblcal.config(text=date)

    def get_date2(self):
        date2=askstring("Date","please enter date like YYYY-MM-DD")
        if date2:
            self.lblcal2.config(text=date2)

#shuffle_functions
    def random_shuffle(self):
        self.shuffled_list=random.sample(self.lst2,len(self.lst2))
        return self.shuffled_list

    def priority(self):
        return list(range(1,len(self.lst2)+1))

    def show_Ruffle(self):
        priorities=self.priority()
        users=self.random_shuffle()
        loan=self.combo5.get()

        bl_ghore=BLGhorekeshi()

        for item in self.tbl4.get_children():
            self.tbl4.delete(item)
        for p, u in zip(priorities,users):
            self.tbl4.insert('', 'end',values=(p,u,loan))

            objghore=Ghorekeshi(priority=p,user=u,loan=loan)
            bl_ghore.Add2(objghore)

        messagebox.showinfo("Result", "Successfully added")

    def get_data(self):
        bl_loan=BLloan()
        y=bl_loan.readAll(Loan)
        if y:
            self.lst=[]
            for item in y:
                self.lst.append(item.Name)
            self.combo5['values']=self.lst

    def get_data2(self):
        bl_user=BLuser()
        z=bl_user.selectAll(User)
        if z:
            self.lst2=[]
            for item in z:
                self.lst2.append(item.Name)
            for i in self.lst2:
                self.lstbox.insert(END,i)

#Menu_functions
    def about(self):
      self.f1.place_forget()
      self.f3.place_forget()
      self.f5.place_forget()
      for item in self.master.winfo_children():
          item.destroy()
      Label(self.master,text="This lottery is held on every month,\n for more information contact us:\n 09331234567 ",bg="white",font=20).pack(pady=70)

    def show_frame(self):
        self.f3.place_forget()
        self.f5.place_forget()
        self.f1.place(relx=0,rely=0)

    def show_frame3(self):
        self.f1.place_forget()
        self.f5.place_forget()
        self.f3.place(relx=0,rely=0)

    def show_frame4(self):
        self.f1.place_forget()
        self.f3.place_forget()
        self.f5.place(relx=0,rely=0)












