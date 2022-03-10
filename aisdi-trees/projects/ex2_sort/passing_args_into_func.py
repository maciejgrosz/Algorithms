
# In Python there is no pass by value nor pass by reference, 
# instead there is so called pass by object reference.
# When passing argument to function, function is passed object's
# reference by value.

def not_changing_list_contents(the_list):
    print("got ", the_list)
    the_list = ['Bua', 'ha', 'ha'] # reference changed to new object
    print("changed to ", the_list)

def changing_list_contents(the_list):
    print("got ", the_list)
    the_list.append(1000) # reference appends element to original object
    print("changed to ", the_list)


list1 = [1, 2, 3]
print("before ", list1)
not_changing_list_contents(list1)
print("after ", list1)

list2 = [2, 3, 4]
print("before ", list2)
changing_list_contents(list2)
print("after ", list2)

##########################################################################

def sorting_the_list(the_list):
    # new_list = the_list # just another reference ...
    new_list = list(the_list) # truly copies (creates new object)
    new_list.sort()

list3 = [19, 8, 27, 66]
print("before ", list3)
sorting_the_list(list3)
print("after ", list3)
