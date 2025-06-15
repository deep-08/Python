# -------- 5. Exception Handling --------
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This will always execute.")