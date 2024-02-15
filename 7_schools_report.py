"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:

School Name: Auburn University
Conference Number: 130

School Name: Baylor University
Conference Number: 108

School Name: East Carolina University
Conference Number: 372

School Name: Indiana University-Bloomington
Conference Number: 107

School Name: Iowa State University
Conference Number: 108

School Name: Kansas State University
Conference Number: 108

School Name: Louisiana State University and Agricultural & Mechanical College
Conference Number: 130

School Name: Michigan State University
Conference Number: 107

School Name: Mississippi State University
Conference Number: 130

School Name: Northwestern University
Conference Number: 107

School Name: Ohio State University-Main Campus
Conference Number: 107

School Name: Oklahoma State University-Main Campus
Conference Number: 108

School Name: Purdue University-Main Campus
Conference Number: 107

School Name: Rutgers University-New Brunswick
Conference Number: 107

School Name: Southern Methodist University
Conference Number: 372

School Name: Temple University
Conference Number: 372

School Name: Texas A & M University-College Station
Conference Number: 130

School Name: Texas Christian University
Conference Number: 108

School Name: Texas Tech University
Conference Number: 108

School Name: The Pennsylvania State University
Conference Number: 107

School Name: The University of Alabama
Conference Number: 130

School Name: The University of Tennessee-Knoxville
Conference Number: 130

School Name: The University of Texas at Austin
Conference Number: 108

School Name: Tulane University of Louisiana
Conference Number: 372

School Name: United States Naval Academy
Conference Number: 372

School Name: University of Arkansas
Conference Number: 130

School Name: University of Central Florida
Conference Number: 372

School Name: University of Cincinnati-Main Campus
Conference Number: 372

School Name: University of Florida
Conference Number: 130

School Name: University of Florida-Online
Conference Number: 130

School Name: University of Georgia
Conference Number: 130

School Name: University of Houston
Conference Number: 372

School Name: University of Illinois Urbana-Champaign
Conference Number: 107

School Name: University of Iowa
Conference Number: 107

School Name: University of Kansas
Conference Number: 108

School Name: University of Kentucky
Conference Number: 130

School Name: University of Maryland-College Park
Conference Number: 107

School Name: University of Memphis
Conference Number: 372

School Name: University of Michigan-Ann Arbor
Conference Number: 107

School Name: University of Minnesota-Twin Cities
Conference Number: 107

School Name: University of Mississippi
Conference Number: 130

School Name: University of Missouri-Columbia
Conference Number: 130

School Name: University of Nebraska-Lincoln
Conference Number: 107

School Name: University of Oklahoma-Norman Campus
Conference Number: 108

School Name: University of South Carolina-Columbia
Conference Number: 130

School Name: University of South Florida
Conference Number: 372

School Name: University of Wisconsin-Madison
Conference Number: 107

School Name: Vanderbilt University
Conference Number: 130

School Name: West Virginia University
Conference Number: 108

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
            if 'Graduation rate  women (DRVGR2020)' in school \
                    and school['Graduation rate  women (DRVGR2020)'] is not None \
                    and school['Graduation rate  women (DRVGR2020)'] > 75:
                print("School Name:", school['instnm'])
                print("Graduation Rate for Women:", school['Graduation rate  women (DRVGR2020)'],"%")
                print()
for school in school_data:
    # Check if the school's conference number matches any of the desired conference numbers
    if 'NCAA' in school and 'NAIA conference number football (IC2020)' in school['NCAA'] \
        and school['NCAA']['NAIA conference number football (IC2020)'] in conference_schools:
            if 'Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)' in school \
                    and school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] is not None \
                    and school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] > 50000:
                total_price = school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']
                print("School Name:", school['instnm'])
                print(f"Total Price for In-state Students Living Off Campus: ${total_price:,.2f}")
                print()        



'''
        # Print the school information
        print("School Name:", school['instnm'])
        print("Conference Number:", school['NCAA']['NAIA conference number football (IC2020)'])
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

'''