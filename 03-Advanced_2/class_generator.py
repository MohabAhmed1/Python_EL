from datetime import datetime

# Configurable parameters
author_name = input("Enter the Author Name:")  
creation_date = datetime.now().strftime("%Y-%m-%d")
class_name = input("Enter the Name of the Class:") 

#C++ header file (.h)
header_template = """/*
*******************************************************
Author: {author}
Date: {date}
Description: Header file for the class {class_name}.
*******************************************************
*/

#ifndef {guard_name}
#define {guard_name}

class {class_name} {{
public:
    {class_name}();  // Constructor
    ~{class_name}();  // Destructor

    void hello();  // A member function

private:
    int member_variable;  // A member variable
}};

#endif  // {guard_name}
"""

#C++ source file (.cpp)
cpp_template = """/*
******************************************************
Author: {author}
Date: {date}
Description: Source file for the class {class_name}.
******************************************************
*/

#include "{class_name}.h"
#include <iostream>

{class_name}::{class_name}() {{
    member_variable = 0;
    // Constructor implementation
}}

{class_name}::~{class_name}() {{
    // Destructor implementation
}}

void {class_name}::hello() {{
    std::cout << "Hello from {class_name}!" << std::endl;
}}
"""

# Generate the header file content
header_content = header_template.format(
    author=author_name,
    date=creation_date,
    class_name=class_name,
    guard_name=class_name.upper() + "_H"
)

# Generate the source file content
cpp_content = cpp_template.format(
    author=author_name,
    date=creation_date,
    class_name=class_name
)

# Write the header file in file(.h)
with open(f"{class_name}.h", "w") as header_file:
    header_file.write(header_content)

# Write the source file in file(.cpp)
with open(f"{class_name}.cpp", "w") as cpp_file:
    cpp_file.write(cpp_content)

print(f"C++ class files for {class_name} generated successfully!")
