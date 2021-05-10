import os
import re

ptr = ["\W"]
path ='/home/ihpc/Kawano/test/'

for filename in os.listdir(path):
     pattern = re.compile(filename)

      for line in open(filename):

            line = f.readline()

             while line:
                     print(line)
                         line = f.readline()

                         f.close()
