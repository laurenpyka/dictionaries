student = {
    "Name": "Lauren",
    "Age": 21,
    "Major": "MIS",
    "Hobbies": ["working out", "spending time with friends", "reading"]    
}

#add 'state' key value pair
student["State"] = "Texas"

#update the age 
student['Age'] += 1

#iterate over key value pairs and print them
for key, value in student.items():
    print(f'{key}: {value}')