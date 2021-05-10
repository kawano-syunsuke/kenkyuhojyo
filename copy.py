import os
import re

ptr = ["\W"]
path ='/home/ihpc/Kawano/test'

for filename in os.listdir(path):   # read files in the directory
 print("++New file is open here!!!!", filename)

 f = open(filename)
 data1 = f.read()
 print(data1)
 lines1 = data1.split('\n')
 print (lines1)
 for line in lines1:
  print("-----",line)
  f.close()
