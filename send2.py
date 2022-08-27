import os
import shutil

path ="C:/Users/KIIT/Documents/testingDoc/Case Decisions-20220827T144703Z-003/"
dest = 'C:/Users/KIIT/Documents/testingDoc/input'
#we shall store all the file names in this list
filelist = []

for root, dirs, files in os.walk(path):
	for file in files:
        #append the file name to the list
		filelist.append(os.path.join(root,file))

#print all the file names
for name in filelist:
    print(name)
    
for i in filelist:
    shutil.move(i, dest)    
