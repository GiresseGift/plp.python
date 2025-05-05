# A list of numbers
my_list1 = [10, 20, 30, 40]
print("before append:", my_list1)

# append a num 'list'
my_list1.append(15)

# after appending number
print("after append:", my_list1)

my_list2 = [50, 60, 70]
print("my second list2:", my_list2)

# join 2 lists
my_list1.extend(my_list2)
print("list after append:", my_list1)

# deleting one number from the lists
del my_list1[-1]
print("lists after delete:", my_list1)

# sorting the list ascending order
my_list1.sort()
print("after ascending order list:", my_list1)

# print the value of 30 in my_list1
print("value of index:", my_list1[3])


#Output
#Number before append
#number after append
#2 list after expand 
# deleting the last element
