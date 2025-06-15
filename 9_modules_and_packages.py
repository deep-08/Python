# -------- 9. Modules & Packages --------
# Suppose we have a module 'helper.py' with a function called 'add'
# In real use: from helper import add

def add(x, y):
    return x + y

print("Addition from helper module:", add(5, 3))