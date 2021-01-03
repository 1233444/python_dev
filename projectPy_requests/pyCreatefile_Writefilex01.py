#File Oblects
from os import close

with open('ReadWrite.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents=f.read(size_to_read)
    
    #Set where to start reading the file, in the example below will start reading the file from beginning
    #f.seek(0)
    
    # for line in f:
    #     print(line,end='')
    
    
    # f_contents = f.readline()
    # print(f_contents, end='')
    # f_contents = f.readlines()
    # print(f_contents)
    # f_contents = f.read()
    # print(f_contents)
    # pass

# f = open('ReadWrite.txt','r')

print()
# #Print filename
print(f.name)

# #Print mode
print(f.mode)

# f.close()
