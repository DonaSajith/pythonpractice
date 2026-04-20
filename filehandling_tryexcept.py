try:
    with open("sample.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print("Error",e)