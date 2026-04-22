import re
error_lines = []

input_path = r"C:\Users\User1\OneDrive - Univision Technology Consulting Pvt Ltd\Desktop\serial.log"
output_path = r"C:\Users\User1\Downloads\log4.txt"

with open(input_path, "r") as infile, open(output_path, "w") as outfile:
    for line in infile:
        if re.search(r'ERROR', line):
            print(line, end='')
            error_lines.append(line)