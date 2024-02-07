import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}
# name of dict is phonebook and there are 3 key values
'''

print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(len(phonebook))

mydictionary = {} #to create an empty dictionary

mydictionary = dict(m=8, n=9) # m & n are the keys and 8,9 are the values 
# dict is a function, so you have to use regular parentheses
# keys will always be strings

print(mydictionary) 

print()
print('*****  end section 1 ********')
print()




print()
print('*****  start section 2 - search dictionary ********')
print()

name = 'Chris'

if name in phonebook:
    print(f"Name: {name} Phone Number: {phonebook[name]}") #don't need quotes around name bc its a variable
else:
    print(f"{name} is not in the phonebook")

#phone = phonebook['Chris'] #dictionaries are case sensitive, if key isn't in dictionary you get 'key error'
#print(phone)


print()
print('*****  end section 2 ********')
print()


print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)

phonebook["Joe"] = '555-0123' #doesn't exist in dictionary, so it is added to it
phonebook["Chris"] = '555-4444'

#can't update key or change it but you can add to it. 

print(phonebook)

print()
print('*****  end section 3 ********')
print()


print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

print(phonebook)

del phonebook["Chris"] #chris is no longer in the dictionary. 

print(phonebook)

print()
print('*****  end section 4 ********')
print()




print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

#defualt for dicitionary to iterate through will always be the keys

for key in phonebook:
    print(f'The key is: {key} and the value is {phonebook[key]}')

for value in phonebook.values():
    print(value)
#dictionaries have a method called .values that allows you to iterate through all the values of the dictionary. 

for key, vlaue in phonebook.items():
    print(f'The key is {key} and the value is {value}')

for item_tuple in phonebook.items():
    print(item_tuple)

print()
print('*****  end section 5 ********')
print()




print()
print('*****  start section 6 - using get and clear ********')
print()

phone = phonebook.get('Chris', '555-5555')
print(phone)


phonebook.clear() #clears out all key values in dict, you're left with an empty dict
print(phonebook)
#since chris does exist in dict, we get his phone#, otherwise we'd get the default # (555-5555)

print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()

print(phonebook)
remove = phonebook.pop('Chris', 'not found')
print(remove)
print(phonebook)


print()
print('*****  end section 7 ********')
print()


print()
print('*****  start section 8 - using popitem ********')
print()
#randomly select key vaue pair

print(phonebook)
a = phonebook.popitem()
print(a)
print(phonebook)



print()
print('*****  end section 8 ********')
print()

'''

print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)
print(list_of_keys)

random_key = random.choice(list_of_keys)
print(random_key)

print(phonebook[random_key])

print(phonebook[random.choice(list(phonebook))]) #same way to do what's above, just in one line of code. 

print()
print('*****  end section 9 ********')
print()
