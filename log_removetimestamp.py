import re

with open("serial.log", "r") as infile, open("log1.txt", "w") as outfile:
    for line in infile:
        if "ERROR" in line:
            # remove [HH:MM:SS] at the start
            cleaned = re.sub(r'^\[\d{2}:\d{2}:\d{2}\]\s*', '', line)
            print(cleaned, end='')
            outfile.write(cleaned)