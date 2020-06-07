# 8.	Create a new dictionary by concatenating the following two dictionaries:
# a={1:10,2:20}
# b={3:30,4:40}
# Expected Result: {1:10,2:20,3:30,4:40}

# lets create a dictionary.
dict1={1:"satish",
       2:"sarita"}
# print(type(dict1))

dict2={3:"Shrayali",
       4:"shrayana",
       5:"shravani"}
# print(type(dict2))

#so as we all know that the dictionaries are immutable it cannot be changed 
# so we need to crearte a 3 variable and update in that.

dict=dict1.update(dict2)
print(dict)   # output will be none because we have to print the dict1 as we have updated

print(dict1)

# BUT IF WE WANT TO CREATE A NEW DICTORY.
d_update={}
for d in (dict1,dict2):
    d_update.update(d)   #putting all the d in the new dictories just like append which is not in dictionary.

print(d_update)



