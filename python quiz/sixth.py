import sys
import random

question_dict = {}	
ls1 =[" 1. java is a ..... language ","A . weekly typed", " B. strongly typed "," C. meoderate typed "," D. none of these ", "B"]
question_dict['1']=ls1
ls1 =[" 2. How many primative data type in java ","A . 6 ", " B. 7 "," C. 8 "," D. 9 ", "C"]
question_dict['2']=ls1
ls1 =[" 3. Which is the following automatic type conversion will be possible ", "A . short to int", " B. byte to int "," C. int to long "," D. long to int", "C"]
question_dict['3']=ls1
ls1 =[" 4. In java , the word true is  ","A . A java Keyword ", " B. A Boolean literal "," C. Same as value 1 "," D. Same as value 0 ", "B"]
question_dict['4']=ls1	
ls1 =[" 5. In java Array is  ","A . Objects", " B. object refrences "," C. primitive data type "," D. none of the above ", "A"]
question_dict['5']=ls1
ls1 =[" 6. When you pass an array to a method , the method recives ...... ","A . A copy of the array ", " B. A copy of the first Element "," C. The refrence of the array  "," D. The length of the array ",  "C"]
question_dict['6']=ls1
	
		
# We can give the function in another .py module and then import in that module and then call the function
username = "avinash"
password= "root"
player_dict ={}
player_report_dict ={}
count = 0

def prepare_player_list():
	ls =[]
	ls.append(raw_input(" Name : "))
	ls.append(raw_input(" class : "))
	ls.append(input(" reg_no : "))
	login_name = raw_input(" login_name : ")	
	ls.append(login_name)
	ls.append(raw_input(" password  : "))
	player_dict[login_name] = ls

def Add_Player():
	no = input("Enter the number of player Admin want to add    ")
	i=1	
	while i<=no:
		prepare_player_list()	
		i=i+1
		print i," player is added successfully."

def Update_Player():
	pl = raw_input(" Enter the name which admin want to update : ")
	print "The old detail of player is : ", player_dict[pl]
	del player_dict[pl]
	print "Update the New detail of player"
	prepare_player_list()
	print pl,"  is updated successfully"

def Delete_Player():
	p = raw_input(" Enter the name which admin want to delete : ")
	print p
	del player_dict[p]
	print p, "  is deleted successfully."
  
def admin_password():
	global password	
	p1 = raw_input("New Password : ")   	
	p2 = raw_input("Confirm New password : ")
	if p1 == p2:
		password = p1	
		return
	else:
		print "password doesn't match . please, Again Enter the  new password"
		admin_password()

def Update_Admin_Profile():
	global username
	global password
	print "old admin username "+username
	print "old password "+password
	username = raw_input("New Admin name : ")
	admin_password()

def add_update_question(n):
	ls =[]
	ques = raw_input(" Enter the Question   :  ")
	ls.append(n+"."+ques)
	ls.append("A."+raw_input(" Enter option A : "))
	ls.append("B."+raw_input(" Enter option B : "))
	ls.append("C."+raw_input(" Enter option C : "))
	ls.append("D."+raw_input(" Enter option D : "))
	ans = raw_input(" Enter Ans:  ")	
	ls.append(ans.upper())	# we change the small case to big case
	question_dict[n] = ls	
	 
def Add_Question():
	n = len(question_dict)
	ns = str(n+1)
	print " Numbers of Question has been added ", n
	add_update_question(ns)
	print " Question has been  added Successfully "
	

def Update_Question():
	n = raw_input(" Enter the question number which we want to update  :  ")
	print "The Question ,options and Ans is : ",question_dict[n]
	del question_dict[n]
	add_update_question(n)
	print " Question has been  updated Successfully "

def Delete_Question():
	n = raw_input(" Enter the question number which we want to delete  :  ")
	print " Question is  ",question_dict[n]
	del question_dict[n]

def Player_Report():
	for key in player_report_dict:
		ls = player_report_dict[key]
		print "Name : "+ls[0]
		print "Marks : ",ls[1]
		print "Number of correct answer : ",ls[2]
		print "Number of incorrect answer  : ",ls[3]   

def Search_Player_Report():
	name = raw_input(" Enter the player name  :  ")
	ls = player_report_dict[name] # we can also use player_report_dict.get(name)
	print "Name : "+ls[0]
	print "Marks : ",ls[1]
	print "Number of correct answer : ",ls[2]
	print "Number of incorrect answer  : ",ls[3]   

def Logout():
	start()


def show_admin_task():
	print " 1. Add Player"
	print " 2. Update Player"
	print " 3. Delete Player"
	print " 4. Update Admin Profile"
	print " 5. Add Question"
	print " 6. Update Question"
	print " 7. Delete Question"
	print " 8. Player Report"
	print " 9. Search Player Report"
	print " 10. Logout"

def admin_login():
	show_admin_task()
	ch = input(" Enter Admin task choice  : ")
	switcher ={
		 1: Add_Player,
		 2: Update_Player,
		 3: Delete_Player,
		 4: Update_Admin_Profile,
	       	 5: Add_Question,
		 6: Update_Question,
		 7: Delete_Question,
		 8: Player_Report,
		 9: Search_Player_Report,
		 10: Logout
	}
	fun = switcher.get(ch ," Invalid choice")
	fun()
	admin_login()
	

def admin_login_check():
	global count
	uname = raw_input(" Admin name  ")
	passwd = raw_input("Password ")
	if username == uname and password == passwd:		
		admin_login()
	else:
		if count== 3:		
			exit()
		else:	
			count=count+1
			print " Either you enterd wrong admin name or password. Re Enter admin name and password"
			admin_login_check()

def player_login(name):
	marks = 0
	correct =0
	incorrect =0
	d =question_dict.copy()	
	k =list(d.keys())
	random.shuffle(k)
	for key in k:
		ls = d[key] # we know that at every dictionary key there is one List is returned
		print ls[0]
		print ls[1]
		print ls[2]
		print ls[3]
		print ls[4]
		ans = raw_input(" Enter the Ans :  ")
		if ls[5] == ans.upper():
			correct = correct +1			
			marks = marks +4
		else:
			marks = marks -1
			incorrect = incorrect+1
	lst = [name,marks,correct,incorrect]
	player_report_dict[name] = lst 
	

def player_login_check():
	login_name = raw_input(" Enter the login name  :  ")
	player_pass = raw_input(" Enter the password : ") 
	ls = player_dict.get(login_name,"No player of this loginname is available ")
	if len(ls) == 0:
		return
	else:
		pwd = ls[4]
		if player_pass == pwd:
			player_login(ls[0])
		else:
			print "password of that player is wrong"
			player_login_check()
	
def exit():
	ch = raw_input(" Do you want to exit the program then ,then press y otherwise anything  :  ")
	if ch == 'y':
		sys.exit(0)
	else:
		start()		 

def start():
	print "1 .Admin"
	print "2 .player"
	print "3 .Exit"
	choice = input("Enter your choice   ")
	switcher ={
		1: admin_login_check,
		2: player_login_check,
		3: exit
	}	
	fun = switcher.get(choice," Invalid Input")
	fun()

start()


