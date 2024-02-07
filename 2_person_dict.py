person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] #value is a list
person["pets"] = {"dog": "Fido", "cat": "Sox"} #value is another dictionary
#^adding key value pairs to dictionary

#print(person)
print(person)
# print out the name of the second child
print(person["children"][1]) #can index the list in the dict, but must supply key first 

# print out the name of the cat
print(person["pets"]['cat'])
#person[pets] evaluates to dict, 
#first key is pets, second key is cat bc pets is a dict
pet_dictionary = person["pets"]
print(type(pet_dictionary))
print(pet_dictionary['cat'])



# use a loop to print out the names of each child
list_of_children = person["children"]
print(type(list_of_children)) #is a list

for child in list_of_children:
    print(child)

#alternatively 
for child in person['children']:
    print(child)


# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for pet in person['pets']: #cycles through the pet keys
    print(f'the type of pet is {pet} and the name of the pet is: {person["pets"][pet]}')

for i,j in person['pets'].items():
    print(f'the type of pet is {i} and the name of the pet is: {j}')
        