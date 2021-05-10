
import os
import re
path ='/home/ihpc/Kawano/test1/'


for filename in os.listdir(path):
 print("++New file is open here!!!!", filename)

 if 'xml' in filename :
     print("ture",filename)
     f = open(filename)
     data1 = f.read()
     #print(data1)
     lines1 = data1.split('\n')
     #print type(lines1)
     for line in lines1:
      if   'width'  in line :
       print("-----",line)
       pattern = '(?<=\>)[^]]+(?=\<)'
       result = re.search(pattern, line)
       i = int(result)
       print(i)
       
      elif 'height' in line :
       print("-----",line)
       pattern = '(?<=\>)[^]]+(?=\<)'
       result = re.search(pattern, line)
       print(result)
       
      elif 'xmin' in line :
       print("-----",line)
       pattern = '(?<=\>)[^]]+(?=\<)'
       result= re.search(pattern, line)
       print(result)	

      elif 'ymin' in line :
       print("-----",line)
       pattern = '(?<=\>)[^]]+(?=\<)'
       result = re.search(pattern, line)
       print(result)

      elif 'xmax' in line :
       print("-----",line)
       pattern = '(?<=\>)[^]]+(?=\<)'
       result = re.search(pattern, line)
       print(result)

      elif 'ymax' in line :
       print("-----",line)
       pattern = '(?<=\>)[^]]+(?=\<)'
       result = re.search(pattern, line)
       print(result)


      
     f.close()
 else:
     print("F",filename)

