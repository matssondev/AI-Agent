from functions.run_python_file import run_python_file

print("Test 1: run_python_file('calculator', 'main.py')")
print(run_python_file("calculator", "main.py"))
print()

print("Test 2: run_python_file('calculator', 'main.py', ['3 + 5'])")
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print()

print("Test 3: run_python_file('calculator', 'tests.py')")
print(run_python_file("calculator", "tests.py"))
print()

print("Test 4: run_python_file('calculator', '../main.py')")
print(run_python_file("calculator", "../main.py"))
print()

print("Test 5: run_python_file('calculator', 'nonexistent.py')")
print(run_python_file("calculator", "nonexistent.py"))
print()

print("Test 6: run_python_file('calculator', 'lorem.txt')")
print(run_python_file("calculator", "lorem.txt"))
