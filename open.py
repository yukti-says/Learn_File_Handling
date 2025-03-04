"""
open("file_name/location","mode")
mode tells about what do you want to do with file[read,write,read+write,modify,append]
"""

# file=open("C:\\Users\\hp\\OneDrive\\Desktop\\learn with project\\File Handling\\intro.txt",'r') #file is a object here
# # a variable content
# content=file.read() #through object file,we have accessed read method that will read and save data into content variable
# print(content)

# # till here file is opened but not closed this can cause memory loss or data loss so it is important to close the file 
# file.close()

"""
#write mode on file
file=open("write.txt","w") #created anu.txt file
content=input("enter some data: ")
#for storing the data into file/write in file
file.write(content)
print("data stored successfully!")
# text=file.read()
# print(text)
file.close()
"""

#append mode
with open("C:\\Users\\hp\\OneDrive\\Desktop\\learn with project\\File Handling\\data.txt","a") as file:
    content=input("enter the message: ")
    file.write(content)
    print("content updated.")