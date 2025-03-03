print("\t\t\t\t VIRTUAL OFFICE \t\t")
print("\t\t\t\t************************\t\t")
print()
from playsound import playsound
playsound(r'E:\Class 12\Term - 2 (2021-22)\Computer Science\Cs Board Projects\Cs Project (2021-22)\Music\Grateful_320(PagalWorld).mp3',False)
startup = -1
L = [(5555, 'Hello'), (1012, 'admin@123'), (3101, 'Viswa5')]
project = {}
submit_prg = {}
a = 2
resig = {}
query = {}
food = {"Pizza": [("Cheese", 150), ("Panner", 175), ("Mushroom", 200)], "Burger": [("Veg", 125), ("Zinger", 190)],
        "Cakes": [("Blackforest", 75), ("Choco Truffle", 80)],
        "Milkshake": [("Chocolate", 50), ("Vanilla", 40), ("Strawberry", 45)],
        "Beverages": [("Coffee", 30), ("Tea", 25)]}
Office = {(1,"THEBOSS"):["*******",25,10000000.0,"Boss"],
          (1012, "admin@123"): ["Sachin", 10, 25000.0, "Employee"],
          (1013, "bvm999"): ["Abinav", 9, 15000.0, "Employee"],
          (3965, "Helo"): ["Rajesh", 12, 50000.0, "Interviewer"],
          (5663, "LM\\bwhu"): ["Gowtham", 6, 21000.0, "Interviewer"],
          (9092, "y]UeuQsd"): ["Parasu", 11, 35000.0, "Interviewer"],
          (2873, "zaNzOfsf"): ["Vimal", 10, 28000.0, "Interviewer"],
          (3101, 'Viswa5'): ['viswajit ram', 2, 100000.0, 'Employee'],
          (5555,"Hello"):["Shagil",10,50000.0,"Project Manager"],
          (1111,"Happy"):["Selva",15,100000.0,"Client"],
          (1234,"ueghuweh"):["Yashwanth",12,50000.0,"Project Manager",0],
          (3645,"ifheihwge"):["Akhil",15,50000.0,"Project Manager",0],
          (9876,"sudhjefe"):["Bharathi",10,50000.0,"Project Manager",0],
          (7645,"Copy"):["Atlee",10,50000.0,"Project Manager",0],
          (7652,"jegjghweg"):["Suresh",23,100000.0,"Client"],
           (4657,"udjhfjds"):["Dinesh",20,100000.0,"Client"],
          (8992, 'XsmYQbGM'): ['Vedha', 4, 10000.0,"Employee"],
          (8693, 'NSwzbHX]'): ['Pranav', 2, 10000.0,"Employee"],
          (7302, 'T^qPXAUq'): ['Ankit', 3, 10000.0,"Employee"],
          (4808, 'pyJnojdm'): ['Guna', 4, 10000.0, 'Employee'],
          (6095, 'qGitS^zz'): ['Salman', 3, 10000.0, 'Employee']}

interview = {1: ['Mukesh', 'Kodambakkam,2nd Cross Street Chennai', 'Project Manager', 8778575342, 'MBA,BA', '-', "1",
                 "10-12-1999"],
             2: ['Gopinath', 'Pallikaranai , Grace United Chennai', 'Pt Teacher', 767657867, 'PHD', '-', "3",
                 "15-3-1996"]}
new_project={1: ['Delivery', 2,'2 weeks' ], 2: ['Walmart',15 , '1 month']}

Off_Emp = {(1012, "admin@123"): ["Sachin", 5, 10000.0, "Employee"],
           (1013, "bvm999"): ["Abinav", 9, 10000.0, "Employee"],
           (3101, 'Viswa5'): ['viswajit ram', 2, 100000.0, 'Employee'],
           (8992, 'XsmYQbGM'): ['Vedha', 4, 10000.0,"Employee"],
          (8693, 'NSwzbHX]'): ['Pranav', 2, 10000.0,"Employee"],
          (7302, 'T^qPXAUq'): ['Ankit', 3, 10000.0,"Employee"],
           (4808, 'pyJnojdm'): ['Guna', 4, 10000.0, 'Employee'],
           (6095, 'qGitS^zz'): ['Salman', 3, 10000.0, 'Employee']}

Off_Interviewer = {(3965, "Helo"): ["Rajesh", 12, 50000.0, "Interviewer"],
                   (5663, "LM\\bwhu"): ["Gowtham", 6, 21000.0, "Interviewer"],
                   (9092, "y]UeuQsd"): ["Parasu", 11, 35000.0, "Interviewer"],
                   (2873, "zaNzOfsf"): ["Vimal",  10, 28000.0, "Interviewer"]}

Off_Pm = {(5555,"Hello"):["Shagil",10,50000.0,"Project Manager",0],
                (1234,"ueghuweh"):["Yashwanth",12,50000.0,"Project Manager",0],
                (3645,"ifheihwge"):["Akhil",15,50000.0,"Project Manager",0],
                (9876,"sudhjefe"):["Bharathi",10,50000.0,"Project Manager",0],
                (7645,"Copy"):["Atlee",10,50000.0,"Project Manager",0]}

Off_Client = {(1111,"Happy"):["Selva",15,100000.0,"Client"],
                      (7652,"jegjghweg"):["Suresh",23,100000.0,"Client"],
                      (4657,"udjhfjds"):["Dinesh",20,100000.0,"Client"]}

look_prg = {(1012): ["Sachin", 10],
           (1013): ["Abinav", 9]}

b = len(interview)
while startup != 0:
    print("*********** \t Office Lobby\t ***********")
    print("Press # to Go and Get Application Form ")
    print("Press @ to Go into The Office ")
    print("Press X to Exit the Office ")
    choice = input()
    if choice == "#":
        b = len(interview)
        print("******** \t Application Form \t ********")
        name = input("Name : ")
        dob = input("Date of Birth : ")
        address = input("Address : ")
        desi = input("Designation : ")
        ph = int(input("Phone Number : "))
        resume = input("Resume : ")
        ex = int(input("Years Of Experience : "))
        add = input("Additional Info : ")
        interview[b + 1] = [name, address, desi, ph, resume, add, ex, dob]
        print("Application form Sent Successfully !! ")
        startup = 1
    elif choice == "@":
        t = ()
        ID = int(input("Office ID : "))
        pwd = input("Password :")
        t += (ID, pwd)
        if t in Office:
            print("Welcome Back ", Office[t][0], " !!!!")
            print("********* Inside the Office ************ ")
            print("G => General ")
            print("E=> To Enter Employee Room ")
            print("I => To Enter Interviewer Room ")
            print("C => To Enter Client Room ")
            print("P => To Enter Project Manager Room")
            print("B => To Enter Boss Office ")
            print("$ => To Enter Food Canteen ")
            print("X = > To Get Back to the Lobby ")
            ch = input("Enter your Choice : ")
            while ch != "X":
                if ch == "E":
                    e_ch = 0
                    print("********* Employee room ************ ")
                    while e_ch != 5:
                        print("1.Look for a Project")
                        print("2.View Your Profile")
                        print("3.Look for Other's Profile")
                        print("4. Resign Work ")
                        print("5.Exit the Office")
                        e_ch = int(input("Enter Your Choice : "))
                        if e_ch == 1:
                            print("Notified to All Project Managers !!")
                            print("Soon You will Be Working in a Project !! ")
                            look_prg[t[0]] = [Off_Emp[t][0],Off_Emp[t][1]]
                        elif e_ch == 2:
                            print("ID :  ", t[0])
                            print("Password : ",t[1])
                            print("*Note : Meant to be Confidential !! ")
                            print("Name: ", Off_Emp[t][0])
                            print("Years of Experience: ", Off_Emp[t][1])
                            print("Salary: ", Off_Emp[t][2])
                            print("Status: ", Off_Emp[t][3])
                        elif e_ch == 3:
                            search = int(input("Enter the ID to be Searched : "))
                            for i in Office:
                                if search == i[0]:
                                    print("ID :  ", search)
                                    print("Name: ", Office[i][0])
                                    print("Years of Experience: ", Office[i][1])
                                    print("Status: ", Office[i][3])
                                    break
                            else:
                                print("Office ID not Found !!")
                        elif e_ch == 4 :
                            print("Resignation Letter ")
                            name = input("Name : ")
                            print("Reason : ")
                            reason = input()
                            resig[t]=[name,reason]
                            print("Letter Sent to Boss !! ")
                    else:
                        print(" You are Now Back in the Lobby !!!")
                        break

                elif ch == "I":
                    i_ch = 0
                    if t in Off_Interviewer:
                        print("*********** \t Interviewer Room \t ***********")
                        while i_ch != 4:
                            print("1. View All Candidates ")
                            print("2. Select  a Candidate ")
                            print("3. Check No. of Waiting Applicants ")
                            print("4. Exit the Office ")
                            i_ch = int(input("Enter Your Choice : "))
                            if i_ch == 1:
                                print("SNO. ", "\t", "\t", " Name", "\t", "Designation", "\t", "Resume")
                                for i in interview:
                                    print(i, "\t", end="\t")
                                    print(interview[i][0], end="'\t")
                                    print(interview[i][2], end="'\t")
                                    print(interview[i][4])
                            elif i_ch == 2:
                                inp = int(input("Enter the SNo. of the Candidate : "))
                                if inp in interview:
                                    print("Name : ", interview[inp][0])
                                    print("Designation : ", interview[inp][2])
                                    print("Resume : ", interview[inp][4])
                                    print("A.Accept or R.Reject ")
                                    ar = input()
                                    if ar == "A":
                                        strt = -1
                                        while strt != 0:
                                            t1 = ()
                                            import random

                                            ID = random.randint(1000, 9999)
                                            s = ""
                                            for i in range(8):
                                                a = random.randint(65, 122)
                                                s += chr(a)
                                            pwd = s
                                            t1 += (ID, pwd)
                                            if t1 in Off_Emp:
                                                strt = 1
                                            else:
                                                strt = 0
                                        sal = float(input("Enter Salary : "))
                                        status = input("Enter Status : ")
                                        print("Credentials of Newly Added Candidate : ",[t1,interview[inp][0], interview[inp][6], sal,status])
                                        Office[t1] = [interview[inp][0], interview[inp][6], sal,status]
                                        if status == "Employee":
                                            Off_Emp[t1] = [interview[inp][0], interview[inp][6], sal, status]
                                        elif status == "Project Manager":
                                            count = 0
                                            Off_Pm[t1] = [interview[inp][0],  interview[inp][6], sal, status, count]
                                        elif status == "Client":
                                            Off_Client[t1] = [interview[inp][0],  interview[inp][6], sal, status]
                                        print("Notified To the Candidate And Added to the Office !!!")
                                        if inp in interview:
                                            del interview[inp]
                                    elif ar == "R":
                                        if inp in interview:
                                            del interview[inp]
                                        print("Candidate Rejected !! ")
                            elif i_ch == 3:
                                print("No. of Waiting Applicants : ", len(interview))
                        else:
                            startup = 1
                            break
                    else:
                        print("Only Interviewers Are Permitted Into this Room !!!! ")
                        print("You are Now Back in the Lobby !! ")
                        pass
                    break
                elif ch == "C":
                     if t in Off_Client :
                         print("*********** \t Client Room \t ***********")
                         c_ch=0
                         while c_ch!=4 :
                             a = len(new_project)
                             print("1.Create New Project ")
                             print("2.Delete a Project")
                             print("3.Examine All Completed Projects ")
                             print("4.Exit the Office ")
                             c_ch = int(input("Enter Your Choice : "))
                             if c_ch == 1:
                                 c_name=input("Enter the Project Name : ")
                                 c_count=int(input("No Employees required : "))
                                 c_time=input("Enter the Estimated time : ")
                                 a = a + 1
                                 new_project[a]=[c_name,c_count,c_time]
                                 print("The Project has been Created Successfully !!!!")
                                 print("Notified To Project Managers !! ")
                             elif c_ch == 2:
                                 name1=input("Enter the Project Name to be Deleted : ")
                                 for i in new_project :
                                     if new_project[i][0]==name1 :
                                         del new_project[i]
                                         print("Deleted Successfully !!")
                                         break
                                 else:
                                     print("Project Name not Found !!!")
                             elif c_ch == 3:
                                 L = []
                                 print("All Completed Projects :")
                                 for i in submit_prg :
                                     print("Project Name : ",i)
                                 examine = input("Enter the Project Name to Examine : ")
                                 if examine in submit_prg :
                                     print("Project Name : ",examine)
                                     print("Project Manager Handled : ",submit_prg[examine][0])
                                     pm = submit_prg[examine][0]
                                     print("Team Members : ",end = "")
                                     for k in submit_prg[examine][1]:
                                         L += k
                                         print(k,end = ", ")
                                     print(" ")
                                     print("Estimated Time : ",submit_prg[examine][2])
                                     for i in submit_prg :
                                         if i == examine :
                                             del submit_prg[examine]
                                             break
                                     result = input("S.Success or  F.Failure ")
                                     if result == "S" :
                                         print("2 Points Increased for the Project Manager for this Successfull Project !!! ")
                                         for i in Off_Pm :
                                             if Off_Pm[i][0]==pm :
                                                 Off_Pm[i][4]+=2  
                                     else :
                                         print("-2 Points Deducted for the Project Manager for this Unsuccessfull Project !!!! ")
                                         for i in Off_Pm :
                                             if Off_Pm[i][0]==pm :
                                                 Off_Pm[i][4]-=2
                         else :
                             print("You Are Now Back in the Lobby !! ")
                             break
                     else :
                         print("Only Clients Are Permitted Into this Room !!!! ")
                         print("You are Now Back in the Lobby !! ")
                         break

                    
                elif ch == "P":
                    if t in Off_Pm:
                        print("*********** \t Project Manager Room \t ***********")
                        p_ch=0
                        while p_ch!=4 :
                            print("1.Available Projects")
                            print("2.Select a New Project")
                            print("3.Status Of Current Project")
                            print("4.Exit the Office")
                            p_ch=int(input("Enter Your Choice :"))
                            if p_ch==1:
                                print("All Projects Available :")
                                for i in new_project:
                                    print("Project No.",i)
                                    print("Project Name : ",new_project[i][0])
                                    print("Employees Required : ",new_project[i][1])
                                    print("Estimated Time : ",new_project[i][2])
                                    print()
                            elif p_ch==2:
                                for status in project :
                                    if project[status][0]==Off_Pm[t][0]:
                                        Go = 1
                                        print("You are Already In a Project !! ")
                                        break
                                else :
                                    Go = 0
                                if Go == 0 :
                                    enter=input("Enter the Project Name to Select : ")
                                    for i in new_project:
                                        if new_project[i][0]==enter:
                                            print("You Have Selected Project Name :",enter)
                                            print("Employees Required :",new_project[i][1])
                                            print("Estimated Time : ",new_project[i][2])
                                            project[enter]=[Off_Pm[t][0],[],new_project[i][1],new_project[i][2]]
                                    for j in new_project :
                                            if new_project[j][0]==enter:
                                                del new_project[j]
                                                break
                            elif p_ch == 3 :
                                for status in project :
                                  if project[status][0]==Off_Pm[t][0]:
                                      Go = 1
                                      break
                                else :
                                    Go = 0
                                    print("No Current Projects Handling !! ")
                                if Go == 1 :
                                    for i in project :
                                        if project[i][0] == Off_Pm[t][0]:
                                            print("Currect Project : ",i)
                                            a = i
                                            print("Team Members : ",project[i][1])
                                            b = project[i][1]
                                            print("No. of Team Members Required : ",project[i][2])
                                            print("Estimated Time : ",project[i][3])
                                            c = project[i][3]
                                            break
                                    if project[i][2]!= len(project[i][1]):
                                        print("*Note : No. of Team Members Not Met !!! ")
                                        print("Press A to Add Members ")
                                        chumma = input()
                                        if chumma == "A" :
                                            print("Available Employees ")
                                            print()
                                            print("ID ","\t","Name","\t","Experience")
                                            for k in look_prg :
                                                print(k,end = "\t")
                                                print(look_prg[k][0],end = "\t")
                                                print(look_prg[k][1])
                                            for j in range(project[i][2]):
                                                print("Team Member No.",j+1)
                                                ids = int(input("Enter the Office ID of the Employee : "))
                                                for h in Off_Emp :
                                                    if ids == h[0]:
                                                        project[i][1]+=[Off_Emp[h][0]]
                                                        print("Added To Project !! ")
                                                        break
                                                for b in look_prg :
                                                    if b == ids :
                                                        del look_prg[b]
                                                        break
                                                    
                                                else :
                                                    print("ID Not Found !!! ")
                                    else :
                                        print(" Submit the Project to Client (Y or N) ")
                                        Pm_choice = input()
                                        if Pm_choice == "Y" :
                                            submit_prg[a]=[Off_Pm[t][0],b,c]
                                            print("Sent To the Client Successfully !!! ")
                                            for i in project :
                                                if i == a :
                                                    del project[i]
                                                    break
                                        else :
                                            continue
                                                
                        else :
                            print("You are Now Back in the Lobby !!! ")
                            break
                    else :
                        print("Only Project Managers Are Permitted Into this Room !!!! ")
                        print("You are Now Back in the Lobby !! ")
                        break
                    
                elif ch == "B":
                    if t == (1,"THEBOSS"):
                        pas = input("Enter The Most Secured Password : ")
                        if pas == "Valimai Update":
                            b_ch = 0
                            while b_ch != 7 :
                                print("$$$$$$$$$$$ \t THE BOSS \t $$$$$$$$$$$")
                                print("1.View Query Sheet ")
                                print("2. Update Top Workers List ")
                                print("3. Increament & Decrement in Salaries ")
                                print("4. Sack a Person from Office ")
                                print("5. Leading Project Managers ")
                                print("6. View Resignation Letters ")
                                print("7. To Get Back To Your Rolls Royce ")
                                b_ch = int(input("Enter Your Choice : "))
                                if b_ch == 1 :
                                    print("Queries ")
                                    for i in query :
                                        print("ID : ",i)
                                        print("Name : ",query[i][0])
                                        print("Query : ",query[i][1])
                                        print()
                                elif b_ch == 2 :
                                    L = []
                                    print("Best Project Manager of this Month ")
                                    enter = int(input("Enter the Office ID : "))
                                    for i in Off_Pm :
                                        if i[0]==enter :
                                            print("ID : ",i[0])
                                            print("Pass : ",i[1])
                                            print("Name :",Off_Pm[i][0])
                                            print("Years Of Experience : ",Off_Pm[i][1])
                                            print("Salary : ",Off_Pm[i][2])
                                            print("Status : ",Off_Pm[i][3])
                                            print("Successfull Projects : ",Off_Pm[i][4])
                                            print("A. Add or R. Reject ")
                                            boss = input()
                                            if boss == "A" :
                                                L +=[i]
                                            else :
                                                L +=[None]
                                            break
                                        else :
                                            print("ID not Found !! ")
                                    print("Best Employee of this Month ")
                                    enter = int(input("Enter the Office ID : "))
                                    for i in Off_Emp :
                                        if i[0]==enter:
                                            print("ID : ",i[0])
                                            print("Pass : ",i[1])
                                            print("Name :",Off_Emp[i][0])
                                            print("Years Of Experience : ",Off_Emp[i][1])
                                            print("Salary : ",Off_Emp[i][2])
                                            print("Status : ",Off_Emp[i][3])
                                            print("A.Add or R.Reject")
                                            boss = input()
                                            if boss == "A" :
                                                L +=[i]
                                            else :
                                                L +=[None]
                                            break
                                    print("Discovered Youth of this Month ")
                                    enter = int(input("Enter the Office ID : "))
                                    for i in Off_Emp :
                                        if i[0]==enter:
                                            print("ID : ",i[0])
                                            print("Pass : ",i[1])
                                            print("Name :",Off_Emp[i][0])
                                            print("Years Of Experience : ",Off_Emp[i][1])
                                            print("Salary : ",Off_Emp[i][2])
                                            print("Status : ",Off_Emp[i][3])
                                            print("A.Add or R.Reject")
                                            boss = input()
                                            if boss == "A" :
                                                L+=[i]
                                            else :
                                                L +=[None]
                                            break
                                        else :
                                            print("ID not Found !! ")
                                elif b_ch == 3 :
                                    enter = int(input("Enter the ID of the Person to be Searched : "))
                                    for i in Office :
                                        if i[0]==enter:
                                            print("ID : ",i[0])
                                            print("Pass : ",i[1])
                                            print("Name :",Office[i][0])
                                            print("Years Of Experience : ",Office[i][1])
                                            print("Salary : ",Office[i][2])
                                            print("Status : ",Office[i][3])
                                            print("I.Increase or D.Decrease")
                                            boss = input()
                                            if boss == "I" :
                                                per = int(input("Enter the Percent of Increament : "))
                                                a = (per/100)*Office[i][2]
                                                Office[i][2]+=a
                                                print("Increased Salary of ",Office[i][0],"to ---> ",Office[i][2])
                                            else :
                                                  per = int(input("Enter the Percent of Decreament : "))
                                                  a = (per/100)*Office[i][2]
                                                  Office[i][2]-=a
                                                  print("Decreased Salary of ",Office[i][0],"to ---> ",Office[i][2])
                                            break
                                    
                                elif b_ch == 4 :
                                    enter = int(input("Enter the Office ID of the Person : "))
                                    for i in Office :
                                        if i[0]==enter:
                                            print("ID : ",i[0])
                                            print("Pass : ",i[1])
                                            print("Name :",Office[i][0])
                                            print("Years Of Experience : ",Office[i][1])
                                            print("Salary : ",Office[i][2])
                                            print("Status : ",Office[i][3])
                                            d = Office[i][3]
                                            break
                                        
                                    print("Are you Sure You Wanna Sack this Person ? (Y or N)")
                                    boss = input()
                                    if boss == "Y" :
                                        for k in Office :
                                            if k[0]==enter :
                                                del Office[k]
                                                break
                                        if d == "Employee" :
                                            for k in Off_Emp :
                                                if k[0]==enter :
                                                    del Off_Emp[k]
                                                    break
                                        elif d == "Project Manager" :
                                            for k in Off_Pm :
                                                if k[0]==enter :
                                                    del Off_Pm[k]
                                                    break
                                        elif d == "Client" :
                                            for k in Off_Client :
                                                if k[0]==enter :
                                                    del Off_Client[k]
                                                    break
                                        elif d == "Interviewer" :
                                            for k in Off_Interviewer:
                                                if k[0]==enter :
                                                    del Off_Interviewer[k]
                                                    break         
                                        print("Person Sacked !!!")
                                    else :
                                        print("Aborted ")
                                    
                                elif b_ch == 5 :
                                    lead = []
                                    for i in Off_Pm :
                                        lead +=[Off_Pm[i][4]]
                                    for i in range(len(lead)):
                                        t = i
                                        for j in range(i+1,len(lead)):
                                            if lead[j]>lead[t]:
                                                t = j
                                        lead[i],lead[t]=lead[t],lead[i]
                                    eq = []
                                    for i in range(len(lead)):
                                        print("No. ",i+1)
                                        for j in Off_Pm :
                                            if Off_Pm[j][4]==lead[i]:
                                                if Off_Pm[j][0] not in eq :
                                                    print("ID : ",j[0])
                                                    print("Name : ",Off_Pm[j][0])
                                                    print("Successfull Projects : ",Off_Pm[j][4])
                                                    eq +=[Off_Pm[j][0]]
                                                    break
                                                else :
                                                    continue
                                elif b_ch == 6 :
                                    print("Resignation Letters : ")
                                    print()
                                    for i in resig :
                                        print("ID : ",i[0])
                                        print("Name : ",resig[i][0])
                                        print("Reason : ",resig[i][1])
                                        print()
                            else :
                                print("Back in Your Luxurious Rolls Royce To Home $$$ ")
                                break

                    else:
                        print("Only One Man THE BO$$ Is Allowed in this Room !!! ")
                        print("You are Now Back in the Lobby !!! ")
                        break
                
                elif ch == "G" :
                    print("********** \t General \t ***********")
                    g_ch =0
                    while g_ch != 4 :
                        print("1. Query Sheet ")
                        print("2. Check Top Workers List ")
                        print("3. View a Profile ")
                        print("4. Exit the Office ")
                        g_ch = int(input("Enter Your Choice : "))
                        if g_ch == 1 :
                            print("\/\/\/\/\/\/\/\/\/\/\/\ \t Query Sheet \t /\/\/\/\/\/\/\/\/\/\/\/ ")
                            print("Name : ",Office[t][0])
                            print("Your Queries : ")
                            Query = input()
                            query[t]=[Office[t][0],Query]
                            print("Query Sent to The Boss !!! ")
                        elif g_ch == 2 :
                            print("[][][][][][][][][][][] Top Workers Of the Month [][][][][][][][][][][]")
                            print("******* Best Project Manager ******")
                            print("ID : ",L[0][0])
                            print("Name : ",Off_Pm[L[0]][0])
                            print("Successfull Projects : ",Off_Pm[L[0]][4])
                            print("******* Best Employee ******")
                            print("ID : ",L[1][0])
                            print("Name : ",Off_Emp[L[1]][0])
                            print("******* Discovered Youth ******")
                            print("ID : ",L[2][0])
                            print("Name : ",Off_Emp[L[2]][0])
                        elif g_ch == 3 :
                            search = int(input("Enter the ID to be Searched : "))
                            for i in Office:
                                if search == i[0]:
                                    print("ID :  ", search)
                                    print("Name: ", Office[i][0])
                                    print("Years of Experience: ", Office[i][1])
                                    print("Status: ", Office[i][3])
                                    break
                            else:
                                print("Office ID not Found !!")
                    
                    else :
                        print("You Are Now Back in the Lobby !!! ")
                        break
                elif ch == "$":
                    print("********** \t Food Canteen \t ***********")
                    print("Available Foods : ")
                    for i in food:
                        print(i)
                    print()
                    print("Enter the Respective Food To Go Thru : ")
                    print("Or Press X To Go Back To Lobby ")
                    f = input()
                    if f in food:
                        print("Item", "\t", "Price")
                        for i in food[f]:
                            print(i[0], "\t", i[1])
                        item = input("Enter the Item : ")
                        qty = int(input("Enter the Quantity : "))
                        for i in food[f]:
                            if i[0] == item:
                                pr = i[1]
                                break
                        print("You ate ", qty, "Delicious", item, " ", f, "for : ₹", pr * qty)
                    elif f == "X":
                        break
                    else:
                        print("Food Item Not Available !!! ")
            else:
                startup = 1
            t = ()
        else:
            print(" Invalid Credentials !! ")
        startup = 1
    elif choice == "X":
        startup = 0
else:
    print("Thank You !! ")








