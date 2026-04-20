try:
    with open("testcase.txt","x") as f:
        f.write("File created safely")
        print("File created")
except FileExistsError:
    print("File exists")
except Exception as e:
    print("Error", e)
