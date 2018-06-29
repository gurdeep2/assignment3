# ASSIGNMENT-14 (FILE HANDLING)
# Q.1- Write a Python program to read last n lines of a file
# f=open('new.txt','r')
# content=f.readlines()
# print(content)
# for i in range(len(content)-5,len(content)):
     # print(content[i])

 # Q.2- Write a Python program to count the frequency of words in a file.
# f=open('new.txt','r')
# d={}
# for word in f.read().split():
    # if word not in d:
        # d[word]=1
    # else:
        # d[word]+=1
# for i,j in d.items():
    # print(i,j)

 
 # Q.3- Write a Python program to copy the contents of a file to another file
# with open('new.txt','r') as f1:
     # with open('new2.txt','w') as f2: 
          # for line in f1:
             # f2.write(line)
          
			 

 # Q.4- Write a Python program to combine each line from first file with the corresponding line in second file
# with open('new.txt') as f1, open('new2.txt') as f2:
      # for line1,line2 in zip(f1,f2):
          # print(line1+line2)
 
 # Q.5- Write a Python program to write 10 random numbers into a file.
 # Read the file and then sort the numbers and then store it to another file.
import random
f7=open('new.txt','w')
for i in range(10):
    num=random.randint(1,100)
    f7.write(str(num))
    f7.write("\n")
f7.close()

f7=open('new.txt','r')
l=f7.readlines()
l.sort()
f7.close()


f8=open("sort.txt",'w')
for i in l:
    f8.write(i)
    f8.write("\n")
print(f8)
f8.close()
