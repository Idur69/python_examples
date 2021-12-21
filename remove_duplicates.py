## remove duplicate from list


lst = [2,4,5,2,4,2]

print(list(set(lst)))   # by suing set method 


# remove duplicates from two list

lst1 = [1,2,2,1,4,5]
lst2 = [6,7,2,1]
new_lst = list(set(lst1) ^ set(lst2))

print(new_lst)

