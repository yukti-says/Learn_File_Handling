"""
with open("C:\\Users\\hp\\OneDrive\\Desktop\\learn with project\\File Handling\\data.txt","w") as file:
    content=input("enter  content to write: ")
    file.write(content)
    print("content saved")
    text=file.read()
    print(text)
"""

#read+write->"r+" mode
with open("C:\\Users\\hp\\OneDrive\\Desktop\\learn with project\\File Handling\\data.txt","w+") as file:
     content=input("enter  content to write: ")
     file.write(content)
     print("content saved")
     text=file.read()
     print(text)
  
 