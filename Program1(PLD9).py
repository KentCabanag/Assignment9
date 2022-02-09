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

file = FPDF('P', 'cm', 'A4') 
file.add_page()

with open('personalresume.json') as datafile:
	info = json.load(datafile)

# Personal details
First_name = info ["personal info"]["First Name"]
Middle_Initial = info ["personal info"]["Middle Initial"]
Last_name = info ["personal info"]["Last Name"]
Place_of_Birth = info ["personal info"]["Place of Birth"]
Gender = info ["personal info"]["Gender"]
Date_of_Birth = info ["personal info"]["Date of Birth"]
Marital_Status = info ["personal info"]["Marital Status"]
Religion = info ["personal info"]["Religion"]
Nationality = info ["personal info"]["Nationality"]

# Objective
Objective = info ["Objective"]["Career Objective"]

# Contact Information
Contact = info ["Contact Information"]["Contact"]
Email = info ["Contact Information"] ["Email"]
Address = info ["Contact Information"] ["Address"] 

# Educational Background
College = info ["Educational Background"]["2014-2018"]
Highschool = info ["Educational Background"]["2010-2014"]
Elementary = info ["Educational Background"]["2006-2010"]

# Skills
skill_1 = info ["Skills"]["skill 1"]
skill_2 = info ["Skills"]["skill 2"] 
skill_3 = info ["Skills"]["skill 3"] 
skill_4 = info ["Skills"]["skill 4"]

file.set_font("helvetica", "B", 24)
file.set_text_color(40,51,49)
file.set_fill_color(215,215,215)
file.cell(19, 3, f"{info['personal info']['First Name']}{info['personal info']['Middle Initial']}{info['personal info']['Last Name']}",ln=1, align="C", fill=1)

file.set_text_color(255,165,0)
file.set_fill_color(0,0,200)
file.set_font("Arial", "B", 15)
file.cell(19,1," Personal Details", align="L", ln=2, fill=1)
file.image('picture.jpg',1, 1, 3.8)

file.set_font("Arial", "")
file.set_font_size(12)
file.set_text_color(40,40,40)
file.cell(0,0.9," Place of Birth:  " + (info["personal info"]["Place of Birth"]),align="L", ln=1, fill=0)
file.cell(0,0.9," Gender:  " + (info["personal info"]["Gender"]),align="L", ln=1, fill=0)
file.cell(0,0.9," Date of Birth:  " + (info["personal info"]["Date of Birth"]),align="L", ln=1, fill=0)
file.cell(0,0.9," Marital Status:  " + (info ["personal info"]["Marital Status"]),align="L", ln=1, fill=0)
file.cell(0,0.9," Religion:  " + (info ["personal info"]["Religion"]),align="L", ln=1, fill=0)
file.cell(0,0.9," Nationality:  " + (info ["personal info"]["Nationality"]),align="L", ln=1, fill=0)

file.set_text_color(255,165,0)
file.set_fill_color(0,0,200)
file.set_font("Arial", "B", 15)
file.cell(19,1," Objective", align="L", ln=2, fill=1)

file.set_font("Arial", "")
file.set_font_size(12)
file.set_text_color(40,40,40)
file.multi_cell(0,0.9, info["Objective"]["Career Objective"])

file.set_text_color(255,165,0)
file.set_fill_color(0,0,200)
file.set_font("Arial", "B", 15)
file.cell(19,1," Contact Information", align="L", ln=2, fill=1)

file.set_font("Arial", "")
file.set_font_size(12)
file.set_text_color(40,40,40)
file.cell(0,0.9," Contact Number:  " + (info["Contact Information"]["Contact"]),align="L", ln=1, fill=0)
file.cell(0,0.9," Email:  " + (info["Contact Information"] ["Email"]),align="L", ln=1, fill=0)
file.cell(0,0.9," Address:  " + (info["Contact Information"] ["Address"]),align="L", ln=1, fill=0)

file.set_text_color(255,165,0)
file.set_fill_color(0,0,200)
file.set_font("Arial", "B", 15)
file.cell(19,1," Educational Background", align="L", ln=2, fill=1)

file.set_font("Arial", "")
file.set_font_size(12)
file.set_text_color(40,40,40)
file.cell(0,0.9," 2014-2018:  " + (info["Educational Background"]["2014-2018"]),align="L", ln=1, fill=0)
file.cell(0,0.9," 2010-2014:  " + (info["Educational Background"]["2010-2014"]),align="L", ln=1, fill=0)
file.cell(0,0.9," 2006-2010:  " + (info["Educational Background"]["2006-2010"]),align="L", ln=1, fill=0)

file.set_text_color(255,165,0)
file.set_fill_color(0,0,200)
file.set_font("Arial", "B", 15)
file.cell(19,1," Skills", align="L", ln=2, fill=1)

file.set_font("Arial", "")
file.set_font_size(12)
file.set_text_color(40,40,40)
file.cell(0,0.9, (info["Skills"]["skill 1"]),align="L", ln=1, fill=0)
file.cell(0,0.9, (info["Skills"]["skill 2"]),align="L", ln=1, fill=0)
file.cell(0,0.9, (info["Skills"]["skill 3"]),align="L", ln=1, fill=0)
file.cell(0,0.9, (info["Skills"]["skill 4"]),align="L", ln=1, fill=0)

file.output("CABANAG_KENTANGELO.pdf")