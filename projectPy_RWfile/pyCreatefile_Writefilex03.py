#File Oblects
from os import close

# with open('ReadWrite2.txt', 'w') as f:
#The line below "Pass" mean to do nothing while creating the file
#     Pass

#Create file and wite to the file
# with open('ReadWrite2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')

#Code to copy jpg but need to read and write in bytes
with open('ReadWrite.jpg', 'rb') as rf:
    with open('ReadWrite_copy.jpg','wb') as wf:
        for line in rf:
            wf.write(line)