#python program to read and write in a file 
#display the mennu to user to which opretion to do
file=None
def showMenu():
#print menu
    print("1.--new student--")
    print("2.--display all--")
    print("3.--search--")
    print("4.--update student--")
    print("5.--delete--")
    print("6.--display coursewise--")
    print("7.--display number of student coursewise--")
    print("8.--exit--")
#frist opretion to read the data of new student 
def newStudent():
    global file
    #read the uucms no of student
    uucmsno=input("enter uucmsno")
    #read name of the student
    name=input("enter the name")
    #select the gender of the student by giving the choice
    print("1.male\n")
    print("2.female\n")
    gender=int(input("select the gender"))
    if(gender==1):
        gender="male"
        print("male")
    else:
        if(gender==2):
            gender="female"
            print(f"female")
        else:
            print(f"enter the correct choice")
    print("***1.BCA***")
    print("***2.BSC***")
    print("***3.BCOM***")
    print("***4.BBA***")
    print("***5.BA***")
    #select the course of student to giving choice
    course=int(input("select your course"))
    if(course==1):
        course="BCA"
        print("BCA")
    elif(course==2):
            course="BSC"
            print("BSC")
    elif(course==3):
            course="BCOM"
            print("BCOM")
    elif(course==4):
        course="BBA"
        print("BBA")
    elif(course==5):
        course="BA"
        print("BA")
        #read the sem of the student
    sem=int(input("enter the sem"))
    #read the fees 0f the student
    fees=int(input("enter the fees"))
    #open the file in append mode to store the value 
    file=open("student3.csv","a")
    #all value store in one variable 
    s=f"{uucmsno},{name},{gender},{course},{sem},{fees}\n"
    #add data to the file
    file.write(s)
    #close the file
    file.close()
    print("student record added successfully")
# this is 2nd opretion this opretion is display the all records of student    
def displayAll():
    global file
    import csv
    #open file in read mood 
    file=open("student3.csv","r")
    #store data in one variable 
    data=file.read()
    #separate the data by split function
    lines=data.split("\n")
    #remove the space 
    lines=lines[0:len(lines)-1]
    print("student list is as follows")
    #give the colum name of data
    print("uucmsno\tname\tgender\tcourse\tsem\tfees\t")
    #display data one by one using the loop
    for l in lines:
        s=l.split(",")
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t")
    file.close()
#3rd opretion this opretion is display only user need data
def search():
    global file
    import csv
    #open file in read mood 
    file=open("student3.csv","r")
    uucmsno=input("enter the uucms")
    #store the data in one variable 
    data=file.read()
    #separate the data by split function
    lines=data.split("\n")
    #take oned variable to check the data is in list or not 
    m=None
    #check the data is in the list
    for x in lines:
        s=x.split(",")
        if(s[0]==uucmsno):
            m=x
            break
    if(m==None):
        print(f"no data found")
    else:
        print(m)
    file.close()
#4th opretion this opretion is update the data
def update():
    global file
    import csv
    #open file in read mood 
    f=open("student3.csv","r")
    #store the data in one variable 
    csvr=csv.reader(f)
    #take one variable to apply tha condition
    found=0
    #create the one emty list
    ml=[]
    uucmsno=input("enter the uucmsno")
    #check the data is there or not if there than update by take new data by user 
    for r in csvr:
        if(r[0]==uucmsno):
            r[1]=name=input("enter the name")
            print("1.male\n")
            print("2.female\n")
            r[2]=int(input("select the gender"))
            if(r[2]==1):
                r[2]="male"
                print("male")
            else:
                if(r[2]==2):
                    r[2]="female"
                    print(f"female")
                else:
                    print(f"enter the correct choice")
            print("***1.BCA***")
            print("***2.BSC***")
            print("***3.BCOM***")
            print("***4.BBA***")
            print("***5.BA***")
            r[3]=int(input("select your course"))
            if(r[3]==1):
                r[3]="BCA"
                print("BCA")
            elif(r[3]==2):
                r[3]="BSC"
                print("BSC")
            elif(r[3]==3):
                r[3]="BCOM"
                print("BCOM")
            elif(r[3]==4):
                r[3]="BBA"
                print("BBA")
            elif(r[3]==5):
                r[3]="BA"
                print("BA")
            r[4]=int(input("enter the sem"))
            r[5]=int(input("enter the fees"))
            print(r)
            #if data is there than add 1 to the found
            found=1
        #data append to the list
        ml.append(r)
    f.close()
    #check there is data is in list 
    if found==0:
        print("data not found")
    else:
        #if data in the list open file in write mood 
        f=open("student3.csv","w",newline='')
        #store the data in one variable
        csvw=csv.writer(f) 
        csvw.writerows(ml)
        print("file modified successfully")
        f.close      
#5th opretion this is delete the data 
def delete():
    global file
    import csv
    #open file in read mood 
    f=open("student3.csv","r")
    #store the data in one variable
    csvr=csv.reader(f)
    #take one variable to apply tha condition
    found=0
    #create the one emty list
    ml=[]
    #check the data is there or not if there than delete the data
    uucmsno=input("enter the uucms no to which student data you want delete")
    for r in csvr:
        if(r[0]!=uucmsno):
            ml.append(r)
        else:
            found=1 
    f.close()
    # check the is in or not
    if found==0:
        print("data not found")
    else:
        #data is in than open file in write mood 
        f=open("student3.csv","w",newline='')
        #store the data in one variable
        csvr=csv.writer(f)
        csvr.writerows(ml)
        print("record deleted successfully")    
        f.close() 
#6th opretion this is display by course  
def coursedisplay():
    import csv
    #read the course
    course=input("enter the course\n")
    #open file in read mood
    csvr=csv.reader(open('student3.csv','r'))
    #check tha data is im or not 
    for row in csvr:
        if course==row[3]:
            print(row)
        else:
            print("no data")    
#call the function                     
while(True):
    showMenu()
    choice=int(input("enter the choice"))
    if(choice==1):
        newStudent()
    elif(choice==2):
        displayAll()
    elif(choice==3):
        search()
    elif(choice==4):
        update()
    elif(choice==5):
        delete()
    elif(choice==6):
        coursedisplay()
    elif(choice==7):
        break
    else:
        print("invalid choice")
            