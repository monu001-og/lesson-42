# Progrm to append contents of file in another file

#entering the file names
firstfile = input("Enter the name of the first file")
secondfile = input("Enter the name of the first file")

#opening both files in the read only mode to read initial contents
f1=open(firstfile,'r')
f2=open(secondfile,'r')

#printing the contents of the file before meaning
print('content of first file before appending -\n',f1 read())
print('content of first file before appending -\n',f2 read())

#closing the files
f1.close()
f2.close()

#opening first file in append more and second file in read mode
f1=open(firstfile,'a')
f2=open(secondfile,'r')

#appemding the contents of the second file in the frist file
f1.write(f2.read())

#relocating the cursor of the files at the beginning
f1.seek(0)
f2.seek(0)

#printing the contents of the files after spending
print('opening of first file after spending \n',f1.read())
print('opening of first file after spending \n',f2.read())

#closing the files
f1.close()
f2.close()
