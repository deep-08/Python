# Create a README.md file with an overview of the project
readme_content = """
# Python Basics for Testers

This repository contains beginner-friendly Python examples tailored for software testers. Each file covers a core Python concept essential for writing test scripts, automating workflows, or understanding Python-based tools.

## 📂 Folder Structure

- `1_variables_and_data_types.py` – Covers Python variables, data types like list, dict, set, tuple, etc.
- `2_operators.py` – Demonstrates arithmetic, comparison, logical, and assignment operators.
- `3_control_flow.py` – `if-else`, `for` and `while` loops, `break`, and `continue` statements.
- `4_functions.py` – Writing and using functions.
- `5_exception_handling.py` – Handling exceptions using `try`, `except`, and `finally`.
- `6_lists_and_dictionaries.py` – Using lists and dictionaries for test data.
- `7_string_manipulation.py` – Cleaning and formatting strings.
- `8_file_handling.py` – Reading from and writing to text files.
- `9_modules_and_packages.py` – Creating reusable modules/functions.

## ✅ Who is this for?

- QA Engineers starting with Python
- Manual testers transitioning into automation
- Anyone interested in the Python basics from a testing perspective

## 🚀 How to Use

1. Clone or download this repository.
2. Run each file in a Python environment (Python 3.7+ recommended).
3. Use these examples to build your own test utilities or practice scripts.

## 📌 Author

Created by **Deepak Sudhakar** — Software Tester | Automation Enthusiast | Bug Bounty Hunter

---

Feel free to fork and contribute!
"""

# Write the README.md file
readme_path = os.path.join(base_dir, "README.md")
with open(readme_path, "w") as f:
    f.write(readme_content.strip())

readme_path
