from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import pymysql

class Login:
	def __init__(self,root):
		self.root=root
		self.root.title("Advance Servilance System")
		self.root.geometry("1750x900+100+50")
		self.bg=ImageTk.PhotoImage(file="bg1.jpg")
		self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

		Frame_login=Frame(self.root,bg="white")
		Frame_login.place(x=550,y=250,height=450,width=600)

		title=Label(Frame_login,text="Admin Login",font=("Arial",42,"bold"),fg="blue",bg="white").place(x=90,y=30)
		decs=Label(Frame_login,text="Advance Servilance System Admin Login",font=("Goudy old style",20,"bold"),fg="#d25d17",bg="white").place(x=90,y=100)

		lbl_Email=Label(Frame_login,text="Email Address", font=("Goudy old style",20,"bold"),fg="gray",bg="white").place(x=90,y=140)
		self.txt_email=Entry(Frame_login,font=("times new roman",15),bg="silver")
		self.txt_email.place(x=90,y=180,width=350,height=35)

		lbl_pass=Label(Frame_login,text="Password", font=("Goudy old style",20,"bold"),fg="gray",bg="white").place(x=90,y=220)
		self.txt_Password=Entry(Frame_login,font=("times new roman",15),bg="silver")
		self.txt_Password.place(x=90,y=260,width=350,height=35)

		reg=Button(Frame_login,text="New user.",command=self.register_window, bg="white", fg="#d77337",bd="0", font=("times new roman",12)).place(x=90, y=300)
		Login=Button(Frame_login,text="Login",command=self.login_function,cursor="hand2",fg="white", bg="#d77337",bd="0", font=("times new roman",20)).place(x=220, y=340)

	def register_window(self):
		self.root.destroy()
		import register

	def login_function(self):
		if self.txt_Password.get()=="" or self.txt_email.get()=="":
			messagebox.showerror("Error","All the fields are required", parent=self.root)
		else:
			try:
				con= pymysql.connect(host="localhost",user="root",password="",database="adminlogin")
				cur=con.cursor()
				cur.execute("select * from adminlog where email=%s and password=%s",(self.txt_email.get(),self.txt_Password.get()))
				row=cur.fetchone()
				if row==None:
					messagebox.showerror("Error","Invalid Username and Password",rent=self.root)
				else:
					messagebox.showinfo("Succes", "Welcome",parent=self.root)
					self.root.destroy()
					import Main
					con.close()

			except Exception as es:
  				messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)



root=Tk()
obj=Login(root)
root.mainloop()