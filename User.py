import os
if os.path.exists("C:/Users/hp/OneDrive/Desktop/learn with project/File Handling/intro.txt"):
    print("File Exists!. ")
    print("What you want to perform on file........CHOOSE: ")
    print("1.READ\n2.WRITE\n3.APPEND")
    choose=int(input("Enter your choice: "))
    
    if(choose==1):
        print("reading file")
        file=open("C:/Users/hp/OneDrive/Desktop/learn with project/File Handling/intro.txt","r")
        content=file.read()
        print(content)

    elif(choose==2):
        print("writng file") 
        file=open("C:/Users/hp/OneDrive/Desktop/learn with project/File Handling/intro.txt","w")
        content=input("enter the new content for file: ")
        file.write(content)
        print("content updated successfully!")

    elif(choose==3):
        print("appending file")
        file=open("C:/Users/hp/OneDrive/Desktop/learn with project/File Handling/intro.txt","a")
        content=input("enter data to add on: ")
        file.write(content)
        print("content added successfully!")


else:
    print("file do not exists! ")

    print("Do you want to create a file: ")
    ans=input("enter answer: ")
    if ans=="yes":
        f_name=input("enter the file name: ")
        file=open(f_name,"w+")
        content=input("enter the message: ")
        file.write(content)
        print("content updated.")
            

    else:
        exit    


