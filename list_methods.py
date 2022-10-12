# this is the explaination to the lists i.e. what are list , how to add elements to list , how to print list , 
name1="tarun"
name2="vaishu"
name3="sejl"
name4="vaishnavi"
name5="tanu"
print(name1,name2,name3,name4,name5)



# lists 

all_names=["tarun", "vaishu","sejl","vaishnavi","tanu"]

print(all_names)

print(type(all_names))

print(all_names[0],all_names[1],all_names[2],all_names[3],all_names[4])





# we have creted a list 
num=[1,2,3,4,5,6,7,8,9,10]



num.append(5)
 #append means to add the value in list 
print(num)

num.append(2) #this value(2)will be added at the end
print(num)


num.pop(5) # this remove the last value inn the list
# num.pop[0] this is wrong method
print(num)

print(num[1]) # this prints the index  value which is added in the sqaure bracket 
num.pop(2) # this is used to remove the index value in the open brackets 



# insert function is used the value at the specific index such as we are adding the number(434) at index value 2
num.insert(2,434)# this will add the value at index 2 
print(num)

num.insert(0,12)
print(num)

num.remove(5) # remove will delete the value which is added to open brakets i.e. 5 will be removed from the list
# note :- this will not remove the index value 
print(num)

#  here we have created another list 

number=[1,2,3,4,5,6,7,8,9,10]
# del keyword is used to delete multiple values 
del number[2] #this will delete the index value inside the sqaure brakcets
print(number)


# this [0:4] are the index's which will be removed from the list 

del number[0:4] # index 0:4 tells us that value will be removed from index 0-4 only i.e. the output will be 6,7,8,9,10
print(number)


#   the clear function will delete all the values inside a list
# although the list will be there but the all the values will be removed 
number.clear()
print(number)