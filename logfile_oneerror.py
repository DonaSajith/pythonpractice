import re

with open("serial.log", "r") as infile, open("log2.txt", "w") as outfile:
    for line in infile:
        if re.search(r'device not found', line, re.IGNORECASE):
            # remove [HH:MM:SS] timestamp
            cleaned = re.sub(r'^\[\d{2}:\d{2}:\d{2}\]\s*', '', line)
            print(cleaned, end='')
            outfile.write(cleaned)