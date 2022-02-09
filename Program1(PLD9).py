#Assignment 9

#PDF Resume Creator
	#- Create a python program that will create your personal resume in PDF format
	#- All personal details are stored in a JSON file
	#- Your program should read the JSON file and write the details in the PDF
	#- The output file should be: LASTNAME_FIRSTNAME.pdf

#Note:
	#- Search for available PDF library that you can use
	#- Search how data is structured using JSON format
	#- Search how to read JSON file
	#- You will create the JSON file manually
	#- Your code should be in github before Feb12

from fpdf import FPDF
import json

pdf = FPDF('P', 'cm', 'A4') 
pdf.add_page()

with open('personalresume.json') as datafile:
	info = json.load(datafile)

# Personal details
First_name = info ["personal info"]["First Name"]
Middle_Initial = info ["personal info"]["Middle Initial"]
Last_name = info  ["personal info"]["Last Name"]
Place_of_Birth = info  ["personal info"]["Place of Birth"]
Gender = info  ["personal info"]["Gender"]
Date_of_Birth = info  ["personal info"]["Date of Birth"]
Marital_Status = info  ["personal info"]["Marital Status"]
Religion = info  ["personal info"]["Religion"]
Nationality = info  ["personal info"]["Nationality"]

# Objective
Objective = info ["Objective"]["Career Objective"]

# Contact Information
Contact = info ["Contact Information"]["Contact"]
Email = info ["Contact Information"] ["Email"]

# Educational Background
College = info ["Educational Background"]["2014-2018"]
Highschool = info ["Educational Background"]["2010-2014"]
Elementary = info ["Educational Background"]["2006-2010"]

# Skills
skill_1 = info ["Skills"]["skill 1"]
skill_2 = info ["Skills"]["skill 2"] 
skill_3 = info ["Skills"]["skill 3"] 
skill_4 = info ["Skills"]["skill 4"]
