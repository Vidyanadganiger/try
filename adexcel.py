while(True):
    print("1.new student admission")
    print("2.display all student")
    print("3.search student")
    print("4.update student")
    print("5.delete student")
    print("display coursewise")
    print("no of admission coursewise")
    print("exist")
    choice=int(input("enter your choice"))
    if(choice==1):
        file=open("students2.csv",'a')
        uucms_no=input("enter the uucms number")
        name=input("enter the name of the student")
        print("1.male\n")
        print("2.female\n")
        print("3.both\n")
        gender=input("select the fender")
        if(gender==1):
            gender=="male"
        elif(gender==2):
            gender=="female" 
        elif(gender==3):
            gender=="both"
        else:
            print("enter the crt choice ")
        s=f"{uucms_no},{name},{gender}"
        file.write("s")
        file.close()
        