import os
import re

ptr = ["\W"]
path ='/home/ihpc/Kawano/test/'

for filename in os.listdir(path):   # read files in the directory
     print("++", filename)

    f = open(filename)
       data1 = f.read()
        print(data1)
         #lines1 = data1.split('\n')
          #print type(lines1)
           for line in data1:
                 print("-----",line)
f.close()
                   
