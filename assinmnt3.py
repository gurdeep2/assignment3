# assignment 4
#write a program to create a tuple with different data type.
t=(3,4.9,"aish")
print(t)



#2 find the length of tuple.
t=(1,2,3,4)
print(len(t))



#3. find the largest and smallest of a tuple
#for largest
t=(1,2,3,4,7)
print(max(t))
#for smallest
t=(2,3,7)
print(min(t))




#4find the product of all element of tuple
t=(1,2,3,4)
p=1
p=p*t[0]
p=p*t[1]
p=p*t[2]
p=p*t[3]
print(p)


#sets
#1 create two set using user defined values
s1=set(input("enter a number: "))  
print(s1)
s2=set(input("enter a number: "))
print(s2)

#2 calculate difference between two sets.
s1=set([1,2,3])
s2=set([1,2,5])
print(s1-s2)

#3. print the result of intersection of two sets.
s1=set([1,2,3])
s2=set([1,2,5])
print(s1&s2)

#Dictionary
#1. create a dictionary to store name and marks of 10 students by user input.
d={}
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
print(d)


#2. sort the dictionary created in previous question
values=list(d.values())
print()
values.sort()
print(values)

#3.count the number of occurence of each letter in the word "MISSISSIPPI"
#store count of every letter with the letter in a dictionary.
t=list("MISSISSIPPI")
d={}
d['M']=t.count('M')
d['S']=t.count('S')
d['I']=t.count('I')
d['P']=t.count('P')
print(d)


