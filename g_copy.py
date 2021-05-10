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
       num = re.sub("\\D","",line)           
       i = int(num) + 5
       if i <= 500:
        with open(filename, encoding="cp932") as f:
         line = f.read()
        line = line.replace("<width>"+str(num)+"</width>","<width>"+str(i)+"</width>")
        with open(filename, mode="w", encoding="cp932") as f:
         f.write(line)
        print(line)
       if i <= 500:
        print("-----",i)
       
       
      elif 'height' in line :
       print("-----",line)
       num = re.sub("\\D","",line)          
       i = int(num) + 5
       if i <= 500:
        with open(filename, encoding="cp932") as f:
         line = f.read()
        line = line.replace("<height>"+str(num)+"</height>","<height>"+str(i)+"</height>")
        with open(filename, mode="w", encoding="cp932") as f:
         f.write(line)
       if i <= 500:
        print("-----",i)

       
      elif 'xmin' in line :
       print("-----",line)
       num = re.sub("\\D","",line)           
       i = int(num) + 5
       if i <= 500:
        with open(filename, encoding="cp932") as f:
         line = f.read()
        line = line.replace("<xmin>"+str(num)+"</xmin>","<xmin>"+str(i)+"</xmin>")
        with open(filename, mode="w", encoding="cp932") as f:
         f.write(line)
        print(line)
       if i <= 500:     
        print("-----",i)
	

      elif 'ymin' in line :
       print("-----",line)
       num = re.sub("\\D","",line)           
       i = int(num) + 5
       if i <= 500:
        with open(filename, encoding="cp932") as f:
         line = f.read()
        line = line.replace("<ymin>"+str(num)+"</ymin>","<ymin>"+str(i)+"</ymin>")
        with open(filename, mode="w", encoding="cp932") as f:
         f.write(line)
       if i <= 500:
        print("-----",i)


      elif 'xmax' in line :
       print("-----",line)
       num = re.sub("\\D","",line)           
       i = int(num) + 5
       if i <= 500:
        with open(filename, encoding="cp932") as f:
         line = f.read()
        line = line.replace("<xmax>"+str(num)+"</xmax>","<xmax>"+str(i)+"</xmax>")
        with open(filename, mode="w", encoding="cp932") as f:
         f.write(line)
       if i <= 500:	
        print("-----",i)


      elif 'ymax' in line :
       print("-----",line)
       num = re.sub("\\D","",line)           
       i =int(num) + 5
       if i <= 500:
        with open(filename, encoding="cp932") as f:
         line = f.read()
        line = line.replace("<ymax>"+str(num)+"</ymax>","<ymax>"+str(i)+"</ymax>")
        with open(filename, mode="w", encoding="cp932") as f:
         f.write(line)
       if i <= 500:       
        print("-----",i)

      
     f.close()
 else:
     print("F",filename)

