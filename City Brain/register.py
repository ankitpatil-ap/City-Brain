from tkinter import * 
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pymysql


class Register:
  	def __init__(self,root):
  		self.root=root
  		self.root.title("Admin Registeration")
  		self.root.geometry("1350x700+0+0")


  		self.bg=ImageTk.PhotoImage(file="rbg.jpg")
  		bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

  		self.left=ImageTk.PhotoImage(file="sbg.jpg")
  		left=Label(self.root,image=self.left).place(x=25,y=100,width=400,height=500)


  		frame1=Frame(self.root,bg="white")
  		frame1.place(x=550,y=100,width=700,height=500)
		
  		sign_in=Label(self.root, text="Sign In If your are Existing User", font=("times new roman",20,'bold'),fg="green").place(x=32,y=290)



  		title=Label(frame1,text="REGISTER HERE", font=("times new roman",20,"bold"),bg="white",fg="Blue").place(x=200,y=30)
#name and lname

  		
  		f_name=Label(frame1, text="First Name", font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
  		self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
  		self.txt_fname.place(x=50,y=130,width=250)

  		L_name=Label(frame1, text="Last Name", font=("|times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
  		self.txt_Lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
  		self.txt_Lname.place(x=370,y=130,width=250)
#contact and  email
  		contact=Label(frame1, text="Contact No", font=("|times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
  		self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
  		self.txt_contact.place(x=50,y=200,width=250)

  		email=Label(frame1, text="Email", font=("|times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
  		self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
  		self.txt_email.place(x=370,y=200,width=250)

#contact and  email
  		password=Label(frame1, text="Password", font=("|times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
  		self.txt_Password=Entry(frame1,font=("times new roman",15),bg="lightgray")
  		self.txt_Password.place(x=50,y=270,width=250)

  		cpass=Label(frame1, text="Conform Password", font=("|times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
  		self.txt_cpass=Entry(frame1,font=("times new roman",15),bg="lightgray")
  		self.txt_cpass.place(x=370,y=270,width=250)
#registern btn
#contact and  email
  		self.btn_img=ImageTk.PhotoImage(file="Register.png")
#contact and  email
  		btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=230,y=350)

		
  		btn_login=Button(self.root,text="Sign In",font=("times new roman",20,'bold') ,bd=0, cursor="hand2",command=self.login_window, fg="blue").place(x=120,y=430, width=180)

  	#def clear(self):
  		#self.txt_fname.delete(0,END)
  		#self.txt_Lname.delete(0,END)
  		#self.txt_contact.delete(0,END)
  		#self.txt_email.delete(0,END)
  		#self.txt_Password.delete(0,END)
  		#self.txt_cpass.delete(0,END)
  		#self.cmb_quest.current(0)

  	def login_window(self):
  		self.root.destroy()
  		import signin
		

  	def register_data(self):
  		if self.txt_fname.get()== "" or self.txt_Lname.get()== "" or self.txt_contact.get()== "" or self.txt_email.get()== "" or self.txt_Password.get()== "" or self.txt_cpass.get()== "":
  			messagebox.showerror("Error"," All the Fields are required",parent=self.root)
  		elif self.txt_Password.get()!=self.txt_cpass.get():
  			messagebox.showerror("Error","Password and conform password should be same.",parent=self.root)
  		else:
  			try:
  				con= pymysql.connect(host="localhost",user="root",password="",database="adminlogin")
  				cur=con.cursor()
  				cur.execute("select* from adminlog where email=%s",self.txt_email.get())
  				row=cur.fetchone()
  				#print(row)
  				if row!=None:
  					messagebox.showerror("Error","User Already Exist, Please try another email.",parent=self.root)
  				else:
  					cur.execute("insert into adminlog(f_name, l_name, contact, email , password) values(%s,%s,%s,%s,%s)",

  					         		(self.txt_fname.get(),
  										self.txt_Lname.get(),
  										self.txt_contact.get(),
  										self.txt_email.get(),
  										self.txt_Password.get()
  										))
  					con.commit()
  					con.close()
  				messagebox.showinfo("Success"," Registraion Successful",parent=self.root)
  				#self.clear()
  			except Exception as es:
  				messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)






root=Tk()
obj=Register(root)
root.mainloop()
