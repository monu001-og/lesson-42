#Program to count number of lines in this file
#opening a file
file=open("Codingal.txt","r")
counter=0

#Readig from file
content = file.read()
#splitting content into lines
#and sorting them in a list
CoList=content.split("\n")

for i in CoList:
    if i:
            counter += 1
            
print("This is the number of lines in the file")
print(counter)