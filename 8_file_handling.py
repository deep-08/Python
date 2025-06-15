# -------- 8. File Handling --------
with open("test_log.txt", "w") as file:
    file.write("Test run started.\n")

with open("test_log.txt", "a") as file:
    file.write("Test case 1: Passed\n")

with open("test_log.txt", "r") as file:
    print("File content:")
    print(file.read())