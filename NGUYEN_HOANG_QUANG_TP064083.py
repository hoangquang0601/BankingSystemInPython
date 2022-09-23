#NGUYEN HOANG QUANG
#TP064083

import datetime
from datetime import date
from datetime import datetime
from datetime import timedelta

today = date.today()

#Login function to determine which type of user to show relevant menu
def userlogin(): 
      print("******** SMART BANKING SYSTEM *********")
      userid = input("Please enter your user ID: ")
      userpass = input("Please enter your password: ")
      with open("userpass.txt","r") as fh:
            foundrec = "notfound"
            for recline in fh:
                  reclist = recline.strip().split(":") #divide each line inside userpass into a small list called reclist
                  if reclist[0] == userid and reclist[1] == userpass: #compare 1st and 2nd component of reclist to 2 log-in inputs
                        foundrec = reclist
                        break
            if foundrec == "notfound":
                  print("Login not successful...!!!")
            else:
                  print("Login Successful...")
      return foundrec

#Function to automatically generate ID for Admin/User account
def genid(perm):
      #id.txt file should start with 2 ID ADM00000 and USA00000 at first
      #id.txt always contains 2 current IDs for Admin/User account
      with open("id.txt","r") as idfh: 
            rec = idfh.readline()
            reclist = rec.strip().split(":") #create 2 small sub-lists
      #Determine type of account to create
      if perm == "staff":
            pref = "ADM"
            oldid = reclist[0][3:] 
      elif perm == "guess":
            pref = "USA"
            oldid = reclist[1][3:]
      nextid = int(oldid) + 1
      #Based on the length of the nextid to create the whole new ID
      if len(str(nextid)) == 1:
          newid = "0000"+str(nextid)
      elif len(str(nextid)) == 2:
          newid = "000"+str(nextid)
      elif len(str(nextid)) == 3:
          newid = "00"+str(nextid)
      elif len(str(nextid)) == 4:
          newid = "0"+str(nextid)
      elif len(str(nextid)) == 5:
          newid = str(nextid)
      newid = pref+newid
      if perm == "staff":
            reclist[0] = newid
      else:
            reclist[1] = newid
      rec = ":".join(reclist)
      #Write value into id.txt and close to save data
      with open("id.txt","w") as fh:
            fh.write(rec)
      return newid

#Function to create new Account for Admin staff      
def addstaff():
      userid = genid("staff") #calling Genid function above with a staff arguement
      userpass = userid
      #Auto generate User ID & Password then print out
      print("User ID :",userid)
      print("User Password:",userpass)
      usrname = input("Please enter you name :")
      acctype = "2"
      #Write value into userpass.txt and close to save data
      with open("userpass.txt","a") as fh:
            rec = userid+":"+userpass+":"+usrname+":"+acctype+"\n"
            fh.write(rec)
      print("-"*40)
      print("Create Account for", usrname, "Successfully!!!")
      print("="*40)
      
def addguess():
      userid = genid("guess") #calling Genid function above with a guess arguement
      userpass = userid
      print("Guess ID :",userid)
      print("Guess Password:",userpass)
      usrname = input("Enter guess name:")
      dob = input("Enter guess date of birth (dd/mm/yy):")
      address = input("Enter guess home address:")
      phone = input("Enter guess phone number:")
      #Determine type of account to open
      print("1. Saving Account")
      print("2. Current Account")
      typeaccount = input("Please choose type of account to open (1/2):")
      #Based on the chosen type, create an initial amount of money deposit into customer acount
      if typeaccount == "1":
            iniamount = "100"
      else:
            iniamount = "500"
      with open("accountbalance.txt","a") as balfh: #Save initial amount as a current balance inside accountbalance.txt
            rec = userid+":"+usrname+":"+typeaccount+":"+iniamount+"\n"
            balfh.write(rec)
      acctype = "3"
      with open("userpass.txt","a") as fh: #Save all customer information except initial amount and typeaccount
            rec = userid+":"+userpass+":"+usrname+":"+acctype+":"+dob+":"+address+":"+phone+"\n"
            fh.write(rec)
      print("="*40)
      print("Create account for", usrname,"successfully!!!")
      print("="*40)

            
def dispalluser():
      with open("userpass.txt","r") as fh:
            print("="*65)
            print("User ID".ljust(15)+"|"+"User Password".ljust(20)+"|"+"User Name".ljust(15)+"|"+"Account Type")
            print("="*65)
            for rec in fh:
                  reclist = rec.strip().split(":")
                  print(reclist[0].ljust(15)+"|"+reclist[1].ljust(20)+"|"+reclist[2].ljust(15)+"|"+reclist[3])
      print("\n\n\n")
                  
#Menu for default Super User Account     
def superusermenu():
      while True:
            print("SUPER USER MENU")
            print("="*40)
            print("\n\t1. Add new admin staff account")
            print("\t2. Display All user accounts")
            print("\t3. LOGOUT from the system")
            ans = input("Please enter your choice :")
            if ans not in ("1", "2", "3"):
                  print("\n", "="*45, "\n", "*"*10,"Incorrect selection!!!","*"*10, "\n", "*"*10, "Please review again!!!", "*"*10, "\n", "="*45)
                  print("\n")
            if ans == "1":
                  addstaff()
            elif ans == "2":
                  dispalluser()
            elif ans == "3":
                  break

#Function available for Admin account and Guess account            
def updatepassword(logdetails): #define logdetails parameter
      allrec = []
      with open("userpass.txt","r") as fh:
            for rec in fh:
                  reclist = rec.strip().split(":") #transform each line inside userpass.txt into a small list called reclist
                  allrec.append(reclist) #add reclist into allrec list then repeat to the next line inside userpass.txt
      newpass = input("Please enter new Password:")
      ind = -1
      nor = len(allrec)
      for cnt in range(0,nor):
            if logdetails[0] == allrec[cnt][0]: #compare the UserID taken from main menu to the list of IDs inside userpass.txt 
                  ind = cnt
                  break
      if ind >=0:
            allrec[ind][1] = newpass
      with open("userpass.txt","w") as fh:
            nor = len(allrec)
            for cnt in range(0,nor):
                  rec = ":".join(allrec[cnt])+"\n"
                  fh.write(rec)
      print("-"*40)
      print("Update New Password Successfully!!!")
      print("\n")

#function to convert a string into a list
def convert(string):
    listr=[]
    listr[:0]=string
    return listr

#This function available for Admin account to input and check whether a UserID is valid or not
def useridcheck():
      cnt = 1
      while cnt == 1:
            userid = input("Please Enter User ID:")
            useridlist = convert(userid) #convert UserID input into a list of each letter
            pref = useridlist[0] + useridlist[1] + useridlist[2]
            #Input first validation
            if pref != "USA":
                  print("\n", "="*45, "\n", "*"*11,"Incorrect User ID!!!","*"*12, "\n", "*"*11, "Please input again!!!", "*"*11, "\n", "="*45,"\n")
            if pref == "USA":
                  cnt = 0
      allrec = []
      with open("userpass.txt","r") as fh:
            for rec in fh:
                  reclist = rec.strip().split(":")
                  allrec.append(reclist)
      ind = -1
      nor = len(allrec)
      for cnt in range(0,nor):
            if userid == allrec[cnt][0]:
                  ind = cnt
                  break
      #Input second validation
      if ind == -1:
            print("\n", "="*45, "\n", "*"*11,"Incorrect User ID!!!","*"*12, "\n", "*"*11, "Please input again!!!", "*"*11, "\n", "="*45,"\n")
      return allrec[cnt][1], userid, allrec[cnt][2]

#Function only available for Admin account
def updateinfo():
      while True:
            updateid = useridcheck() #call useridcheck function to input UserID
            allrec = []
            with open("userpass.txt","r") as fh:
                  for rec in fh:
                        reclist = rec.strip().split(":")
                        allrec.append(reclist)
            ind = -1
            nor = len(allrec)
            for cnt in range(0,nor):
                  if updateid[1] == allrec[cnt][0]:
                        ind = cnt
                        break
            if ind >= 0:
                  print("="*40)
                  print("Current Information of", updateid[2], ":")
                  print("-"*31)
                  print("Date of Birth:", allrec[cnt][4])
                  print("Address:", allrec[cnt][5])
                  print("Phone number:", allrec[cnt][6])
                  print("="*40)
                  print("\t1. Change DoB")
                  print("\t2. Change address")
                  print("\t3. Change phone number")
                  print("="*40)
                  ans = input("Please enter your choice:")
                  print("-"*40)
                  if ans == "1":
                        newdob = input("Please enter new Date of Birth:")
                        allrec[ind][4] = newdob #Replace old DoB with new one
                        with open("userpass.txt","w") as fh:
                              nor = len(allrec)
                              for cnt in range(0,nor):
                                    rec = ":".join(allrec[cnt])+"\n"
                                    fh.write(rec)
                        print("="*40)
                        print("Update new Date of Birth successfully!!!")
                        print("="*40)
                        break
                  elif ans == "2":
                        newaddress = input("Please enter new Address:")
                        allrec[ind][5] = newaddress
                        with open("userpass.txt","w") as fh:
                              nor = len(allrec)
                              for cnt in range(0,nor):
                                    rec = ":".join(allrec[cnt])+"\n"
                                    fh.write(rec)
                        print("="*40)
                        print("Update new Address successfully!!!")
                        print("="*40)
                        break
                  elif ans == "3":
                        newphone = input("Please enter new Phone Number:")
                        allrec[ind][6] = newphone
                        with open("userpass.txt","w") as fh:
                              nor = len(allrec)
                              for cnt in range(0,nor):
                                    rec = ":".join(allrec[cnt])+"\n"
                                    fh.write(rec)
                        print("="*40)
                        print("Update new Phone Number successfully!!!")
                        print("="*40)
                        break

#Function available for Admin and Guess account
def generatereport(logdetails):
      while True:
            try:
                  startdatestr = input("Please enter startdate (dd/mm/yyyy):")
                  enddatestr = input("Please enter enddate (dd/mm/yyyy):")
                  startdate = datetime.strptime(startdatestr, "%d/%m/%Y") #convert input to datetime format
                  enddate = datetime.strptime(enddatestr, "%d/%m/%Y")
                  deltadate = enddate - startdate
                  deltastr = str(deltadate)
                  delta = deltastr.split(" ")
                  if delta[0] == "0:00:00": #assign value 0 if input same start/end dates
                        delta[0] = 0
                  delta_int = int(delta[0])
                  if delta_int < 0:
                        print("Start date cannot be greater than End date!!!")
                  else:
                        num = int(delta[0]) + 1
                        print("="*48)
                        print("Statement of Account Report for", logdetails[2], ":")
                        print("-"*48)
                        print("Transaction date".ljust(25)+"Type".ljust(15)+"Amount".ljust(15))
                        print("="*48)
                        for cnt in range(0,num): #run a loop to find any record match from startdate and add up by 1
                              nextdate1 = startdate + timedelta(days=cnt)
                              nextdate = datetime.strftime(nextdate1, "%d/%m/%Y")
                              with open("transactiondetail.txt","r") as fh:
                                    foundrec = "notfound"
                                    for recline in fh:
                                          reclist = recline.strip().split(":")
                                          if reclist[0] == logdetails[1] and reclist[1] == nextdate:
                                                print(reclist[1].ljust(25)+reclist[2].ljust(15)+reclist[3].ljust(15))
                        print("="*48)
                  break
            except:
                  print("="*40)
                  print("Wrong date input!!! Please try again!!!")
                  print("="*40)

def adminstaffmenu(logdetails):
      while True:
            print("ADMIN STAFF MENU")
            print("="*40)
            print("\n\t1. Add new Guess account")
            print("\t2. Display All user accounts")
            print("\t3. Updating New Password")
            print("\t4. Updating Guess User Information")
            print("\t5. Generate Account Report")
            print("\t6. LOGOUT from the system")
            ans = input("Please enter your choice :")
            if ans not in ("1", "2", "3", "4", "5", "6"):
                  print("\n", "="*45, "\n", "*"*10,"Incorrect selection!!!","*"*10, "\n", "*"*10, "Please review again!!!", "*"*10, "\n", "="*45)
            if ans == "1":
                  addguess()
            elif ans == "2":
                  dispalluser()
            elif ans == "3":
                  updatepassword(logdetails)
            elif ans == "4":
                  updateinfo()
            elif ans == "5":
                  usercheck = useridcheck()
                  generatereport(usercheck)
            elif ans == "6":
                  break

def deposit(logdetails):
      allrec = []
      with open("accountbalance.txt","r") as depofh:
            for rec in depofh:
                  reclist = rec.strip().split(":")
                  allrec.append(reclist)
      depo = input("Please enter an amount to make deposit:")
      ind = -1
      nor = len(allrec)
      for cnt in range(0,nor):
            if logdetails[0] == allrec[cnt][0]:
                  ind = cnt
                  break
      if ind >=0:
            newbal = int(allrec[ind][3]) + int(depo)
            allrec[ind][3] = str(newbal)
      with open("accountbalance.txt","w") as fh:
            nor = len(allrec)
            for cnt in range(0,nor):
                  rec = ":".join(allrec[cnt])+"\n"
                  fh.write(rec)
      time = today.strftime("%d/%m/%Y")
      with open("transactiondetail.txt", "a") as fh:
            rec = logdetails[0]+":"+time+":"+"Deposit"+":"+depo+"\n"
            fh.write(rec)
      print("-"*40)
      print("Deposit RM", depo, "Successfully into Account!!!")
      print("\n")


def withdraw(logdetails):
      allrec = []
      with open("accountbalance.txt","r") as depofh:
            for rec in depofh:
                  reclist = rec.strip().split(":")
                  allrec.append(reclist)
      wtdr = input("Please enter an amount to make withdrawal:")
      ind = -1
      nor = len(allrec)
      for cnt in range(0,nor):
            if logdetails[0] == allrec[cnt][0]:
                  ind = cnt
                  break
      if ind >=0:
            newbal = int(allrec[ind][3]) - int(wtdr)
            if allrec[ind][2] == "1" and newbal >= 100:
                  allrec[ind][3] = str(newbal)
                  with open("accountbalance.txt","w") as fh:
                        nor = len(allrec)
                        for cnt in range(0,nor):
                              rec = ":".join(allrec[cnt])+"\n"
                              fh.write(rec)
                  time = today.strftime("%d/%m/%Y")
                  with open("transactiondetail.txt", "a") as fh:
                        rec = logdetails[0]+":"+time+":"+"Withdraw"+":"+wtdr
                        fh.write(rec)
                  print("-"*40)
                  print("Withdraw RM", wtdr, "Successfully from Account!!!")
                  print("\n")
            elif allrec[ind][2] == "1" and newbal < 100:
                  print("="*40)
                  print("Cannot execute!!!","\nSaving account must remain at least RM100")
                  print("="*40)
            elif allrec[ind][2] == "2" and newbal >= 500:
                  allrec[ind][3] = str(newbal)
                  with open("accountbalance.txt","w") as fh:
                        nor = len(allrec)
                        for cnt in range(0,nor):
                              rec = ":".join(allrec[cnt])+"\n"
                              fh.write(rec)
                  time = today.strftime("%d/%m/%Y")
                  with open("transactiondetail.txt", "a") as fh:
                        rec = logdetails[0]+":"+time+":"+"Withdraw"+":"+wtdr
                        fh.write(rec)
                  print("-"*40)
                  print("Withdraw RM", wtdr, "Successfully from Account!!!")
                  print("\n")
            else:
                  print("="*40)
                  print("Cannot execute!!!","\nCurrent account must remain at least RM500")
                  print("="*40)



def guessmenu(logdetails):
      while True:
            print("GUESS USER MENU for",logdetails[2])
            print("="*40)
            print("\n\t1. Deposit money into account")
            print("\t2. Withdraw money from account")
            print("\t3. Generate Account Report")
            print("\t4. Updating New Password")
            print("\t5. LOGOUT from the system")
            ans = input("Please enter your choice :")
            if ans not in ("1", "2", "3", "4", "5"):
                  print("\n", "="*45, "\n", "*"*10,"Incorrect selection!!!","*"*10, "\n", "*"*10, "Please review again!!!", "*"*10, "\n", "="*45)
            if ans == "1":
                  deposit(logdetails)
            elif ans == "2":
                  withdraw(logdetails)
            elif ans == "3":
                  generatereport(logdetails)
            elif ans == "4":
                  updatepassword(logdetails)
            elif ans == "5":
                  break




#MAIN LOGIC
#==========
while True:
      loginstat = userlogin()
      if loginstat != "notfound":
            print("Welcome to the System "+loginstat[2]+"!!!")
            print("="*40)
            if loginstat[3] == "1":
                  superusermenu()
            elif loginstat[3] == "2":
                  adminstaffmenu(loginstat)
            elif loginstat[3] == "3":
                  guessmenu(loginstat)
      else:
            print("INVALID LOGIN CREDENTIALS...!!!!")
      ans = input("Press Q to Quit the SYSTEM.. Anyother Key to Continu....")
      if ans == "Q":
            break
      
