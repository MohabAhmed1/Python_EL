from datetime import datetime
author_name = input("Enter the Name of the Author:")
creation_date = datetime.now().strftime("%Y-%m-%d")

Byte = ''
for bit_num in range(0,8):
    while True:
        bit_mode = input(f"Please Enter Bit {bit_num} mode( in / out ) :").strip().lower()
        if(bit_mode == 'in'):
            bit_mode = '1'
            break
        elif(bit_mode == 'out'):
            bit_mode = '0'
            break
        else:
            print("Wrong Entry please enter (in or out)")      
    Byte+=bit_mode

Port=''
while True:
    Port= input("Please Specify the Port Name (A,B,C,D):").strip().capitalize()
    if (Port == "A" or Port == "B" or Port == "C" or Port == "D" ):
        break
    else:
        print("Wrong Entry please enter (A or B or C or D)")

#Function Template

function_template =  """
/*
*******************************************************
Author: {author}
Date: {date}
*******************************************************
*/

/*This is function to pass direction of the pins to DDR port in AVR*/
void Init_PORT{port_name}_DIR (void)
{{
    DDR{port_name} = 0b{bytes_reg};
}}

"""

function_content = function_template.format(port_name = Port ,bytes_reg = Byte,author=author_name,date=creation_date)


with open("Init.c","w") as fun:
    fun.write(function_content)


print("The Init file is created successfully")
