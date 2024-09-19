import re
import random
import openpyxl

with open('Functions_prototypes.h', 'r') as file:
    header_content = file.read()

# Regular expression pattern to match full function prototypes (return type, name, parameters)
function_pattern = r'([a-zA-Z_][a-zA-Z0-9_*\s]*\s+\**\s*[a-zA-Z_][a-zA-Z0-9_]*\s*\(.*?\)\s*;)'

# Find all matches of the pattern (full function prototype as one match)
function_prototypes = re.findall(function_pattern, header_content)


#for each iteration on function prototypes a new row is created 
workbook = openpyxl.Workbook()
sheet = workbook.active
for prototype in function_prototypes:
    sheet.append([prototype, f"IDX0{random.randint(0, 99)}"])    

workbook.save("Functions_Prototypes.xlsx")
print("Functions entry is done Sucessfully")

