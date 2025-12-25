from functions.get_file_content import get_file_content

print("Result for lorem.txt:")
result = get_file_content("calculator", "lorem.txt")
for line in result.split("\n"):
    print(f"    {line}")

print("Result for main.py:")
result = get_file_content("calculator", "main.py")
for line in result.split("\n"):
    print(f"    {line}")

print()
print("Result for calculator.py:")
result = get_file_content("calculator", "pkg/calculator.py")
for line in result.split("\n"):
    print(f"    {line}")

print()
print("Result for '/bin/cat':")
result = get_file_content("calculator", "/bin/cat")
for line in result.split("\n"):
    print(f"    {line}")

print()
print("Result for pkg/does_not_exist.py:")
result = get_file_content("calculator", "pkg/does_not_exist.py")
for line in result.split("\n"):
    print(f"    {line}")
