"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""


import json
infile = open('school_data.json', 'r')
school_data = json.load(infile) #brings all the data from the json file and converts it into python code

conference_schools = [372, 108, 107, 130]

# Iterate through each school in the data
for school in school_data:
    # Check if the school's conference number matches any of the desired conference numbers
    if 'NCAA' in school and 'NAIA conference number football (IC2020)' in school['NCAA'] \
        and school['NCAA']['NAIA conference number football (IC2020)'] in conference_schools:
        # Print the school information
        print("School Name:", school['instnm'])
        print("Conference Number:", school['NCAA']['NAIA conference number football (IC2020)'])
        print("Conference:", end=" ")
        # Determine and print the conference name based on the conference number
        if school['NCAA']['NAIA conference number football (IC2020)'] == '372':
            print("American Athletic Conference")
        elif school['NCAA']['NAIA conference number football (IC2020)'] == '108':
            print("Big Twelve Conference")
        elif school['NCAA']['NAIA conference number football (IC2020)'] == '107':
            print("Big Ten Conference")
        elif school['NCAA']['NAIA conference number football (IC2020)'] == '130':
            print("Southeastern Conference")
        print()

print("Universities with a graduation rate for women over 75%:")
for school in school_data:
    if 'Graduation rate  women (DRVGR2020)' in school \
            and school['Graduation rate  women (DRVGR2020)'] is not None \
            and school['Graduation rate  women (DRVGR2020)'] > 75:
        print("School Name:", school['instnm'])
        print("Graduation Rate for Women:", school['Graduation rate  women (DRVGR2020)'])
        print()

# Display report for universities with a total price for in-state students living off campus over $50,000
print("Universities with a total price for in-state students living off campus over $50,000:")
for school in school_data:
    if 'Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)' in school \
            and school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] is not None \
            and school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] > 50000:
        print("School Name:", school['instnm'])
        print("Total Price for In-state Students Living Off Campus:", 
            school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'])
        print()