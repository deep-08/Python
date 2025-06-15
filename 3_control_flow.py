# -------- 3. Control Flow --------
if age < 18:
    print("Underage")
elif 18 <= age < 60:
    print("Adult")
else:
    print("Senior")

# for loop
print("Skills List:")
for skill in skills:
    print("-", skill)

# while loop with break and continue
count = 0
while count < 5:
    count += 1
    if count == 2:
        continue  # Skip 2
    if count == 4:
        break     # Stop at 4
    print("Count:", count)