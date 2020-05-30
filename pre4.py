# slicing the array
numbers =[25,544,478,54,63,26,89,78,84]
print(numbers[2:6])
print(numbers[1:]) #introducing only first index
print(numbers[:6]) #introducing the end index 

print(numbers[-3:-1])
print(len(numbers)) # printing the length of list
# adding a number at the end 
numbers.append(45)
print(numbers)

# to sort the list 
numbers.sort()
print(numbers)

name ="masai school"
part_of_name= name[4:8]
print(part_of_name)

first_name="hello"
last_name="there"
fullname=first_name+" "+last_name
print(fullname)
print(last_name)