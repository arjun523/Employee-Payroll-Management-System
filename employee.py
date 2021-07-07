from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymysql
import time
import os
import tempfile

class EmployeeSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x700+0+0")
        self.root.wm_iconbitmap("icon.ico")
        self.root.config(bg="gray")
        title = Label(self.root,text="Employee Payroll Management System",font=("times new roman",30,"bold"),
                      bg="black",fg="white",anchor="w",padx=10)
        title.place(x=0,y=0,relwidth=1)
        btnShowEmployee=Button(self.root,text="All Employee",command=self.employee_frame,font=("times new roman", 15),
                            bg="gray", fg="white", padx=10).place (x=1200, y=10,height=28,width=130)
        #<-----------Frame1-------------->
        self.var_empcode=StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = IntVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_hiredlocation = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_experience = IntVar()
        self.var_proofid = StringVar() #adhaar card
        self.var_contact= IntVar()
        self.var_status = StringVar()

        frame1= Frame(self.root,bd=3,relief=RIDGE,bg="black")
        frame1.place(x=10,y=70,width=750,height=620)
        title1 = Label (frame1, text="Employee Details", font=("times new roman", 20),
                       bg="dark gray", fg="black", anchor="w", padx=10).place(x=0, y=0, relwidth=1)

        employeeCode= Label(frame1, text="Employee Code", font=("times new roman", 20,'bold'),
                       bg="black", fg="white", padx=10).place(x=10,y=70)
        self.txtCode = Entry (frame1,textvariable=self.var_empcode, font=("times new roman", 15),
                         bg="lightblue", fg="black")
        self.txtCode.place (x=220, y=75, width=200,height=28)
        btnSearch = Button (frame1, text="Search",command=self.search,font=("times new roman", 18),
                            bg="gray", fg="black", padx=10).place (x=440, y=74,height=28)

        #<----------ROW1---------------->
        empDesignation = Label(frame1, text="Designation", font=("times new roman", 20),
                              bg="black", fg="white", padx=10).place (x=10, y=120)
        txtDesignation = Entry(frame1, font=("times new roman", 15),
                                bg="lightblue", fg="black",textvariable=self.var_designation).place (x=170, y=125,width=200)
        empDob = Label (frame1, text="Date Of Birth", font=("times new roman", 18),
                                bg="black", fg="white", padx=10).place (x=390, y=125)
        txtDob = Entry (frame1, font=("times new roman", 15),
                                bg="lightblue", fg="black",textvariable=self.var_dob).place (x=540, y=125,width=200)

        #<-----------ROW2--------------->
        empName = Label (frame1, text="Name", font=("times new roman", 20),
                                bg="black", fg="white", padx=10).place (x=10, y=170)
        txtName = Entry (frame1, font=("times new roman", 15),
                                bg="lightblue", fg="black",textvariable=self.var_name).place (x=170, y=175, width=200)
        empDoj = Label (frame1, text="Joining Date", font=("times new roman", 18),
                        bg="black", fg="white", padx=10).place (x=390, y=175)
        txtDoj = Entry (frame1, font=("times new roman", 15),
                                bg="lightblue", fg="black",textvariable=self.var_doj).place (x=540, y=175, width=200)

        # <-----------ROW3--------------->
        empAge = Label (frame1, text="Age", font=("times new roman", 20),
                         bg="black", fg="white", padx=10).place (x=10, y=220)
        txtAge = Entry (frame1, font=("times new roman", 15),
                         bg="lightblue", fg="black",textvariable=self.var_age).place (x=170, y=225, width=200)
        empExp = Label (frame1, text="Experience", font=("times new roman", 18),
                        bg="black", fg="white", padx=10).place (x=390, y=225)
        txtexp = Entry (frame1, font=("times new roman", 15),
                        bg="lightblue", fg="black",textvariable=self.var_experience).place (x=540, y=225, width=200)

        # <-----------ROW4--------------->
        empGender = Label (frame1, text="Gender", font=("times new roman", 20),
                        bg="black", fg="white", padx=10).place (x=10, y=270)
        txtGender = Entry (frame1, font=("times new roman", 15),
                        bg="lightblue", fg="black",textvariable=self.var_gender).place (x=170, y=275, width=200)
        empProofID = Label (frame1, text="Proof ID", font=("times new roman", 18),
                        bg="black", fg="white", padx=10).place (x=390, y=275)
        txtProofID = Entry (frame1, font=("times new roman", 15),textvariable=self.var_proofid,
                        bg="lightblue", fg="black").place (x=540, y=275, width=200)

        # <-----------ROW5--------------->
        empEmail = Label (frame1, text="Email ID", font=("times new roman", 20),
                           bg="black", fg="white", padx=10).place (x=10, y=320)
        txtEmail = Entry (frame1, font=("times new roman", 15),textvariable=self.var_email,
                           bg="lightblue", fg="black").place (x=170, y=325, width=200)
        empContact = Label (frame1, text="Contact No.", font=("times new roman", 18),
                            bg="black", fg="white", padx=10).place (x=390, y=325)
        txtContact = Entry (frame1, font=("times new roman", 15),textvariable=self.var_contact,
                            bg="lightblue", fg="black").place (x=540, y=325, width=200)

        # <-----------ROW6--------------->
        empHired = Label (frame1, text="Hired Location", font=("times new roman", 18),
                          bg="black", fg="white", padx=10).place (x=10, y=373)
        txtHired = Entry (frame1, font=("times new roman", 15),textvariable=self.var_hiredlocation,
                          bg="lightblue", fg="black").place (x=170, y=375, width=200)
        empStatus = Label (frame1, text="Status", font=("times new roman", 18),
                            bg="black", fg="white", padx=10).place (x=390, y=375)
        txtStatus = Entry (frame1, font=("times new roman", 15),textvariable=self.var_status,
                            bg="lightblue", fg="black").place (x=540, y=375, width=200)

        # <-----------ROW7--------------->
        empAddress = Label (frame1, text="Address", font=("times new roman", 20),
                          bg="black", fg="white", padx=10).place (x=10, y=420)
        self.txtAddress = Text(frame1, font=("times new roman", 15),
                          bg="lightblue", fg="black")
        self.txtAddress.place (x=170, y=425, width=568,height=180)

        # <-----------Frame2-------------->
        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_basicsalary = StringVar()
        self.var_totaldays = StringVar()
        self.var_leavedays = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_netsalary = StringVar()

        frame2 = Frame (self.root, bd=3, relief=RIDGE, bg="black")
        frame2.place (x=770, y=70, width=580, height=300)
        title2 = Label (frame2, text="Employee Salary Details", font=("times new roman", 20),
                        bg="dark gray", fg="black", anchor="w", padx=10).place (x=0, y=0, relwidth=1)

        # <----------ROW1---------------->
        salMonth = Label (frame2, text="Month", font=("times new roman", 18),
                                bg="black", fg="white", padx=10).place (x=10, y=50)
        txtMonth = Entry (frame2, font=("times new roman", 15),textvariable=self.var_month,
                                bg="lightblue", fg="black").place (x=100, y=50, width=50)
        salYear = Label (frame2, text="Year", font=("times new roman", 18),
                        bg="black", fg="white", padx=10).place (x=170, y=50)
        txtYear = Entry (frame2, font=("times new roman", 15),textvariable=self.var_year,
                        bg="lightblue", fg="black").place (x=240, y=50, width=80)
        salBasic = Label (frame2, text="Basic Salary ", font=("times new roman", 18),
                        bg="black", fg="white", padx=10).place (x=330, y=50)
        txtBasic = Entry (frame2, font=("times new roman", 15),textvariable=self.var_basicsalary,
                         bg="lightblue", fg="black").place (x=470, y=50, width=100)

        # <-----------ROW2--------------->
        salDays = Label (frame2, text="Total Days", font=("times new roman", 18),
                         bg="black", fg="white", padx=10).place (x=10, y=100)
        txtDays = Entry (frame2, font=("times new roman", 15),textvariable=self.var_totaldays,
                         bg="lightblue", fg="black").place (x=180, y=100, width=100)
        salLeave = Label (frame2, text="Days of Leave", font=("times new roman", 18),
                        bg="black", fg="white", padx=10).place (x=300, y=100)
        txtLeave = Entry (frame2, font=("times new roman", 15),textvariable=self.var_leavedays,
                        bg="lightblue", fg="black").place (x=470, y=100, width=100)

        # <-----------ROW3--------------->
        salMedical = Label (frame2, text="Medical", font=("times new roman", 18),
                         bg="black", fg="white", padx=10).place (x=10, y=150)
        txtMedical = Entry (frame2, font=("times new roman", 15),textvariable=self.var_medical,
                         bg="lightblue", fg="black").place (x=180, y=150, width=100)
        salPF = Label (frame2, text="Provident Fund", font=("times new roman", 18),
                          bg="black", fg="white", padx=10).place (x=300, y=150)
        txtPF = Entry (frame2, font=("times new roman", 15),textvariable=self.var_pf,
                          bg="lightblue", fg="black").place (x=470, y=150, width=100)

        # <-----------ROW4--------------->
        salConvence = Label (frame2, text="Convence", font=("times new roman", 18),
                         bg="black", fg="white", padx=10).place (x=10, y=200)
        txtConvence = Entry (frame2, font=("times new roman", 15),textvariable=self.var_convence,
                         bg="lightblue", fg="black").place (x=180, y=200, width=100)
        salNet = Label (frame2, text="Net Salary", font=("times new roman", 18),
                          bg="black", fg="white", padx=10).place (x=300, y=200)
        txtNet = Entry (frame2, font=("times new roman", 15),textvariable=self.var_netsalary,
                          bg="lightblue", fg="black").place (x=470, y=200, width=100)

        btnCalculate =Button(frame2,command=self.calculate,text="Calculate",font=("times new roman",18),
                             bg="gray", fg="black", padx=10).place (x=20, y=250,height=30,width=100)
        self.btnSave = Button (frame2,command=self.add, text="Save", font=("times new roman", 18),
                               bg="gray", fg="black", padx=10)
        self.btnSave.place (x=130, y=250, height=30,width=100)
        btnClear = Button (frame2, text="Clear",command=self.clear, font=("times new roman", 18),
                               bg="gray", fg="black", padx=10).place (x=240, y=250, height=30,width=100)
        self.btnUpdate = Button( frame2,text="Update",state=DISABLED,command=self.update,font=("times new roman",18),
                           bg="gray",fg="black",padx=10 )
        self.btnUpdate.place( x=350,y=250,height=30,width=100 )
        self.btnDelete = Button( frame2,text="Delete",state=DISABLED,command=self.delete,font=("times new roman",18),
                           bg="gray",fg="black",padx=10 )
        self.btnDelete.place( x=460,y=250,height=30,width=100 )

        # <-----------Frame3-------------->
        frame3 = Frame (self.root, bd=3, relief=RIDGE, bg="lightgray")
        frame3.place (x=770, y=380, width=580, height=310)

        #<------Calculator Frame------------>
        var_txt = StringVar()
        self.var_operator = ''
        def btnClick(num):
            self.var_operator = self.var_operator + str(num)
            var_txt.set(self.var_operator)
        def result():
            res=str(round(eval(self.var_operator),3))
            var_txt.set(res)
            self.var_operator = ''
        def clear_all():
            var_txt.set('')
            self.var_operator = ''

        calFrame =Frame(frame3,bg="black",bd=3,relief=RIDGE)
        calFrame.place(x=2,y=2,width=250,height=300)
        title3 = Label(calFrame,text="Calculator",font=("times new roman",16),
                       bg="dark gray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        txtResult =Entry(calFrame,bg="lightblue",textvariable=var_txt,font=("times new roman",20,"bold"),justify=RIGHT,state='readonly').place(x=0,y=30,relwidth=1,height=62)
        btnClearAll =Button(calFrame,text="Clear",relief=GROOVE,font=("times new roman",15,),command=clear_all).place(x=0,y=72,height=20,width=60)
        #<------------ROW1-------------->
        btn7= Button(calFrame,bd=2,text="7",font=("times new roman",15,"bold"),command=lambda:btnClick(7)).place(x=0,y=93,width=60,height=50)
        btn8 = Button (calFrame,bd=2, text="8", font=("times new roman", 15, "bold"),command=lambda :btnClick(8)).place (x=62, y=93, width=60, height=50)
        btn9 = Button (calFrame,bd=2, text="9", font=("times new roman", 15, "bold"),command=lambda :btnClick(9)).place (x=124, y=93, width=60, height=50)
        btnDiv = Button (calFrame,bd=2, text="/", font=("times new roman", 15, "bold"),command=lambda :btnClick("/")).place (x=186, y=93, width=60, height=50)
        # <------------ROW2-------------->
        btn4 = Button (calFrame, bd=2, text="4", font=("times new roman", 15, "bold"),command=lambda :btnClick(4)).place (x=0, y=144, width=60,height=50)
        btn5 = Button (calFrame, bd=2, text="5", font=("times new roman", 15, "bold"),command=lambda :btnClick(5)).place (x=62, y=144, width=60,height=50)
        btn6 = Button (calFrame, bd=2, text="6", font=("times new roman", 15, "bold"),command=lambda :btnClick(6)).place (x=124, y=144, width=60,height=50)
        btnMul = Button (calFrame, bd=2, text="*", font=("times new roman", 15, "bold"),command=lambda :btnClick("*")).place (x=186, y=144, width=60,height=50)
        # <------------ROW3-------------->
        btn1 = Button (calFrame, bd=2, text="1", font=("times new roman", 15, "bold"),command=lambda :btnClick(1)).place (x=0, y=195, width=60,height=50)
        btn2 = Button (calFrame, bd=2, text="2", font=("times new roman", 15, "bold"),command=lambda :btnClick(2)).place (x=62, y=195, width=60,height=50)
        btn3 = Button (calFrame, bd=2, text="3", font=("times new roman", 15, "bold"),command=lambda :btnClick(3)).place (x=124, y=195, width=60,height=50)
        btnMin = Button (calFrame, bd=2, text="-", font=("times new roman", 15, "bold"),command=lambda :btnClick("-")).place (x=186, y=195, width=60,height=50)
        # <------------ROW3-------------->
        btn0 = Button(calFrame,bd=2,text="0",font=("times new roman",15,"bold"),command=lambda :btnClick(0)).place(x=0,y=246,width=60,height=50)
        btnDec = Button(calFrame,bd=2,text=".",font=("times new roman",15,"bold"),command=lambda :btnClick(".")).place(x=62,y=246,width=60,height=50)
        btnAdd = Button(calFrame,bd=2,text="+",font=("times new roman",15,"bold"),command=lambda :btnClick("+")).place(x=124,y=246,width=60,height=50)
        btnEqual = Button(calFrame,bd=2,text="=",font=("times new roman",15,"bold"),command=result).place(x=186,y=246,width=60,height=50)

        #<------------Salary Reciept------------->
        salaryFrame = Frame(frame3,bg="black",bd=3,relief=RIDGE)
        salaryFrame.place(x=251,y=2,width=320,height=300)
        title4 = Label(salaryFrame,text="Salary Receipt",font=("times new roman",15),
                       bg="dark gray",fg="black",anchor="w",padx=10).place(x=0,y=0,relwidth=1,height=30)

        salaryFrame2= Frame(salaryFrame,bg="black",bd=2,relief=RIDGE)
        salaryFrame2.place(x=0,y=30,relwidth=1,height=230)

        self.sample = f'''\t Company Name, XYZ\n\t Address: XYZ, Floor 4
------------------------------------------------
 Employee ID\t\t: 
 Salary Of\t\t: Mon-YYYY
 Generated On\t\t: DD-MM-YYYY
------------------------------------------------
 Total Days\t\t: DD
 Working Days\t\t: DD
 Days Of Leave\t\t: DD
 Convence\t\t: Rs.----
 Medical\t\t: Rs.----
 PF\t\t: Rs.----
 Gross Payment\t\t: Rs.-------
 Net Salary\t\t: Rs.-------
------------------------------------------------
This is Computer generated slip,not
required any signature'''
        scroll_y= Scrollbar(salaryFrame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_reciept= Text(salaryFrame2,font=("times new roman",13),bg="black",fg='white',yscrollcommand=scroll_y.set)
        self.txt_salary_reciept.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_reciept.yview)
        self.txt_salary_reciept.insert(END,self.sample)
        self.btnPrint=Button(salaryFrame,text="Print",state=DISABLED,command=self.print,font=("times new roman",20),bg="gray",fg="black")
        self.btnPrint.place(x=180,y=262,height=30,width=100)


    #all functions
    def calculate(self):
        if self.var_month.get()=="" or self.var_year.get()=="" or self.var_basicsalary.get()=="" or self.var_totaldays.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            per_day=int(self.var_basicsalary.get())/int(self.var_totaldays.get())
            work_day=int(self.var_totaldays.get())-int(self.var_leavedays.get())
            sal=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())
            net_sal=sal-deduct+addition
            self.var_netsalary.set(str(round(net_sal,2)))
            #UPDATE RECIEPT
            new_sample = f'''\t Company Name, XYZ\n\t Address: XYZ, Floor 4
------------------------------------------------
 Employee ID\t\t: {self.var_empcode.get()}
 Salary Of\t\t: {self.var_month.get()}-{self.var_year.get()}
 Generated On\t\t: {str(time.strftime("%d-%m-%Y"))}
------------------------------------------------
 Total Days\t\t: {self.var_totaldays.get()}
 Working Days\t\t: {str(int(self.var_totaldays.get())-int(self.var_leavedays.get()))}
 Days Of Leave\t\t: {self.var_leavedays.get()}
 Convence\t\t: Rs.{self.var_convence.get()}
 Medical\t\t: Rs.{self.var_medical.get()}
 PF\t\t: Rs.{self.var_pf.get()}
 Gross Payment\t\t: Rs.{self.var_basicsalary.get()}
 Net Salary\t\t: Rs.{self.var_netsalary.get()}
------------------------------------------------
 This is Computer generated slip,not
 required any signature'''
            self.txt_salary_reciept.delete('1.0',END)
            self.txt_salary_reciept.insert(END,new_sample)

    def search(self):
        try:
            con = pymysql.connect( host="localhost",user="root",password="",db="ems" )
            cur = con.cursor()
            cur.execute( "select * from emp_salary where e_id=%s",(self.var_empcode.get()) )
            row = cur.fetchone()
            if row == None:
                messagebox.showerror( "Error","Invalid Employee Code",parent=self.root )
            else:
                self.var_empcode.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hiredlocation.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_experience.set(row[9])
                self.var_proofid.set(row[10])
                self.var_contact.set(row[11])
                self.var_status.set(row[12])
                self.txtAddress.delete( '1.0',END )
                self.txtAddress.insert(END,row[13])
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_basicsalary.set(row[16])
                self.var_totaldays.set(row[17])
                self.var_leavedays.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_convence.set(row[21])
                self.var_netsalary.set(row[22])
                file_ = open('salary_reciept/'+str(row[23]),'r')
                self.txt_salary_reciept.delete('1.0',END)
                for i in file_:
                    self.txt_salary_reciept.insert(END,i)
                file_.close()
                self.btnSave.config( state=DISABLED )
                self.btnUpdate.config( state=NORMAL )
                self.btnDelete.config( state=NORMAL )
                self.txtCode.config( state='readonly')
                self.btnPrint.config(state=NORMAL)
        except Exception as ex:
            messagebox.showerror( "Error",f"Error due to :{str( ex )}")

    def update(self):
        if self.var_empcode.get()=="" or self.var_netsalary.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","Employee Details are required")
        else:
            try:
                con = pymysql.connect( host="localhost",user="root",password="",db="ems" )
                cur = con.cursor()
                cur.execute( "select * from emp_salary where e_id=%s",(self.var_empcode.get()) )
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror( "Error","This Employee Id is Invalid.Try Again with valid Employee Id",
                                      parent=self.root )
                else:
                    cur.execute("UPDATE `emp_salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`hiredlocation`=%s,`doj`=%s,"
                                "`dob`=%s,`experience`=%s,`proof_id`=%s,`contact`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`basicsalary`=%s,"
                                "`totaldays`=%s,`leavedays`=%s,`medical`=%s,`pf`=%s,`convence`=%s,`netsalary`=%s,`salary_reciept`=%s WHERE `e_id`=%s",
                                (self.var_designation.get(),self.var_name.get(),self.var_age.get(),self.var_gender.get(),self.var_email.get(),
                                 self.var_hiredlocation.get(),self.var_doj.get(),self.var_dob.get(),self.var_experience.get(),self.var_proofid.get(),
                                 self.var_contact.get(),self.var_status.get(),self.txtAddress.get( '1.0',END ),self.var_month.get(),self.var_year.get(),
                                 self.var_basicsalary.get(),self.var_totaldays.get(),self.var_leavedays.get(),self.var_medical.get(),self.var_pf.get(),
                                 self.var_convence.get(),self.var_netsalary.get(),f"salary_reciept_{self.var_name.get()}_{self.var_empcode.get()}.txt",self.var_empcode.get()) )
                    con.commit()
                    con.close()
                    file_=open(f"salary_reciept/salary_reciept_{self.var_name.get()}_{self.var_empcode.get()}.txt",'w')
                    file_.write(self.txt_salary_reciept.get('1.0',END))
                    file_.close()
                    messagebox.showinfo( "Success","Record Updated Successfuly" )
            except Exception as ex:
                messagebox.showerror( "Error",f"Error due to :{str( ex )}")

    def clear(self):
        self.btnSave.config(state=NORMAL)
        self.btnUpdate.config(state=DISABLED)
        self.btnDelete.config(state=DISABLED)
        self.btnPrint.config(state=DISABLED)
        self.txtCode.config(state=NORMAL)

        self.var_empcode.set('')
        self.var_designation.set( '' )
        self.var_name.set( '' )
        self.var_age.set('')
        self.var_gender.set('')
        self.var_email.set('')
        self.var_hiredlocation.set('')
        self.var_doj.set( '')
        self.var_dob.set('')
        self.var_experience.set( '' )
        self.var_proofid.set( '')
        self.var_contact.set( '')
        self.var_status.set( '' )
        self.txtAddress.delete( '1.0',END )
        self.var_month.set('')
        self.var_year.set('' )
        self.var_basicsalary.set('')
        self.var_totaldays.set('')
        self.var_leavedays.set('' )
        self.var_medical.set('')
        self.var_pf.set('')
        self.var_convence.set('' )
        self.var_netsalary.set( '' )
        self.txt_salary_reciept.delete('1.0',END)
        self.txt_salary_reciept.insert(END,self.sample )

    def delete(self):
        if self.var_empcode.get()=="":
            messagebox.showerror("Error","Employee ID required")
        else:
            try:
                con = pymysql.connect( host="localhost",user="root",password="",db="ems" )
                cur = con.cursor()
                cur.execute( "select * from emp_salary where e_id=%s",(self.var_empcode.get()) )
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror( "Error","Invalid Employee ID",parent=self.root )
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                        cur.execute("delete from emp_salary where e_id=%s",(self.var_empcode.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Success","Employee Record Deleted Succesfully")
                        self.clear()
            except Exception as ex:
                messagebox.showerror( "Error",f"Error due to :{str( ex )}" )

    def add(self):
        if self.var_empcode.get()=="" or self.var_netsalary.get()=="" or self.var_name.get()=="":
            messagebox.showerror("Error","Employee Details are required")
        else:
            try:
                con = pymysql.connect( host="localhost",user="root",password="",db="ems" )
                cur = con.cursor()
                cur.execute( "select * from emp_salary where e_id=%s",(self.var_empcode.get()) )
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror( "Error","This Employee Id has already available.Try Again with another Id",
                                      parent=self.root )
                else:
                    cur.execute("Insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (self.var_empcode.get(),self.var_designation.get(),self.var_name.get(),self.var_age.get(),
                                 self.var_gender.get(),self.var_email.get(),self.var_hiredlocation.get(),self.var_doj.get(),self.var_dob.get(),
                                 self.var_experience.get(),self.var_proofid.get(),self.var_contact.get(),self.var_status.get(),
                                 self.txtAddress.get( '1.0',END ),self.var_month.get(),self.var_year.get(),self.var_basicsalary.get(),self.var_totaldays.get(),
                                 self.var_leavedays.get(),self.var_medical.get(),self.var_pf.get(),self.var_convence.get(),self.var_netsalary.get(),f"salary_reciept_{self.var_name.get()}_{self.var_empcode.get()}.txt") )
                    con.commit()
                    con.close()
                    file_=open(f"salary_reciept/salary_reciept_{self.var_name.get()}_{self.var_empcode.get()}.txt",'w')
                    file_.write(self.txt_salary_reciept.get('1.0',END))
                    file_.close()
                    messagebox.showinfo( "Success","Record Added Successfuly" )
                    self.btnPrint.config(state=NORMAL)
            except Exception as ex:
                messagebox.showerror( "Error",f"Error due to :{str( ex )}")

    def show(self):
        try:
            con = pymysql.connect( host="localhost",user="root",password="",db="ems" )
            cur = con.cursor()
            cur.execute( "select * from emp_salary" )
            rows = cur.fetchall()
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def employee_frame(self):
        self.root2 = Toplevel(self.root)
        self.root2.title( "Employee Payroll Management System" )
        self.root2.geometry( "1000x500+120+100" )
        self.root2.config( bg="white" )
        title = Label( self.root2,text="Employee Details",font=("times new roman",30,"bold"),
                       bg="black",fg="white",anchor="w",padx=10 )
        title.pack( side=TOP,fill=X )
        self.root2.focus_force()
        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx = Scrollbar( self.root2,orient=HORIZONTAL )
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack( side=RIGHT,fill=Y )
        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email',
        'hiredlocation', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year',
        'basicsalary', 'totaldays', 'leavedays', 'medical', 'pf', 'convence', 'netsalary', 'salary_reciept'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id',text='EmployeeID')
        self.employee_tree.heading( 'designation',text='Designation' )
        self.employee_tree.heading( 'name',text='Name' )
        self.employee_tree.heading( 'age',text='Age' )
        self.employee_tree.heading( 'gender',text='Gender' )
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hiredlocation',text='Hired Location')
        self.employee_tree.heading( 'doj',text='Date Of Joining' )
        self.employee_tree.heading( 'dob',text='Date of Birth' )
        self.employee_tree.heading( 'experience',text='Experience' )
        self.employee_tree.heading( 'proof_id',text='Proof ID' )
        self.employee_tree.heading( 'contact',text='Contact' )
        self.employee_tree.heading( 'status',text='Status' )
        self.employee_tree.heading( 'address',text='Address' )
        self.employee_tree.heading( 'month',text='Month' )
        self.employee_tree.heading( 'year',text='Year' )
        self.employee_tree.heading( 'basicsalary',text='Basic Salary' )
        self.employee_tree.heading( 'totaldays',text='Total Days' )
        self.employee_tree.heading( 'leavedays',text='Leave Days' )
        self.employee_tree.heading( 'medical',text='Medical' )
        self.employee_tree.heading( 'pf',text='Provident Fund' )
        self.employee_tree.heading( 'convence',text='Convence' )
        self.employee_tree.heading( 'netsalary',text='Net Salary' )
        self.employee_tree.heading( 'salary_reciept',text='Salary Reciept' )
        self.employee_tree['show'] = 'headings'

        self.employee_tree.column( 'e_id',width=100 )
        self.employee_tree.column( 'designation',width=100 )
        self.employee_tree.column( 'name',width=100 )
        self.employee_tree.column( 'age',width=100 )
        self.employee_tree.column( 'gender',width=100 )
        self.employee_tree.column( 'email',width=100)
        self.employee_tree.column( 'hiredlocation',width=100 )
        self.employee_tree.column( 'doj',width=100)
        self.employee_tree.column( 'dob',width=100 )
        self.employee_tree.column( 'experience',width=100 )
        self.employee_tree.column( 'proof_id',width=100 )
        self.employee_tree.column( 'contact',width=100 )
        self.employee_tree.column( 'status',width=100 )
        self.employee_tree.column( 'address',width=300 )
        self.employee_tree.column( 'month',width=100 )
        self.employee_tree.column( 'year',width=100)
        self.employee_tree.column( 'basicsalary',width=100)
        self.employee_tree.column( 'totaldays',width=100 )
        self.employee_tree.column( 'leavedays',width=100 )
        self.employee_tree.column( 'medical',width=100 )
        self.employee_tree.column( 'pf',width=100 )
        self.employee_tree.column( 'convence',width=100 )
        self.employee_tree.column( 'netsalary',width=100 )
        self.employee_tree.column( 'salary_reciept',width=200 )
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config( command=self.employee_tree.yview )
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()

        self.root2.mainloop()

    def print(self):
        fileP = tempfile.mktemp(".txt")
        open(fileP,'w').write(self.txt_salary_reciept.get('1.0',END))
        os.startfile(fileP,'print')


window = Tk()
employeeSysObject = EmployeeSystem(window)

window.mainloop()