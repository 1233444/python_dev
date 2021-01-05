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

with open('ReadWrite.txt', 'r') as rf:
    with open('ReadWrite_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)