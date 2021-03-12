import os
#To travel throught a path with files and subfolders
for folderName, subfolders, filenames in os.walk(r'C:\Users\Bravin\Desktop\Python\Automatic the boring stuff'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: '+ str(subfolders))
    print('The filenames in ' + folderName + ' are: '+ str(filenames))
    print()

    for subfolder in subfloders:
        #Delete files.
        os.unlink(subfolders)
    #To copy a file with a determinate extension.
    for file in filenames:
        if file.endswith('.py'):
            shutil.copy(os.join(folderName, file), os.join(folderName, file + 'backup'))
            
