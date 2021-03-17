#importing libraries
import os

count = 0
#imput the desired name you want to be of the files in the folder
# the name will be like
#name1.extension
#name2.extension
#.
#.
#namen.extension

name = str(input())

for i in os.listdir():
  #adding the name with numbers and extension
    os.rename(i,name + str(count)+ '.'+ i.split('.')[-1])
    count+=1
