#f1=open("ap.txt","x")#create a file
f1=open("ap.txt","r")#file opened in read mode
print(f1.read())# read operation on file
f1=open("ap.txt","w")
f1.write("codetantra")
f1=open("ap.txt","r")#file opened in read mode
print(f1.read())
