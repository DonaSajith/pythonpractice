def count_errors(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            if "FAIL" in line:
                count += 1
    return count

def total_errors(file_list):
    total = 0
    for file in file_list:
        count = count_errors(file)
        print(f"{file}: {count} errors")
        total += count
    return total


files = ["output1.log", "output2.log", "output3.log"]
print("Total number of errors:", total_errors(files))