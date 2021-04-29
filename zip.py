#usr/bin/python3 

import zipfile 

# sloved challenge Recursion
first_foloder = zipfile.ZipFile("recursion.zip","r")
first_foloder.extractall()

for i in reversed(range(0,555)):
    zip_file = zipfile.ZipFile("recursion"+ str(i)+".zip" ,"r")
    zip_file.extractall()

zip_file = zipfile.ZipFile("recursion0.zip" ,"r")
files = zip_file.read('flag.txt').decode('utf8')
print("flag is ==> " ,files)
