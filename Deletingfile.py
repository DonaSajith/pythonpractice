import os
if os.path.exists("txtnew.txt"):
    os.remove("txtnew.txt")
    print("File removed")