import  os
import subprocess
"""
Creates a bat file to run all apps within the "Apps" subdirectory
"""

# Initiation
f=[]
batfile = "@Echo on\n"

# Create a list of all the files
for (root,   folder, files) in os.walk("Apps"):
	f.extend(files)

# Create the text for the batfile based on the list above
for appnames in f:
	batfile = batfile + ("start /wait Apps\\\""  + appnames + "\" /SILENT \n") 

# Write to bat file
newfile = open("Installation command.bat","w") 
newfile.write(batfile)
newfile.close()

# Open folder containing the bat file 
subprocess.Popen(r'explorer "'+os.getcwd()+'"')