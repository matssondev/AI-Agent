from functions.get_files_info import get_files_info

print("Result for current directory:")
result = get_files_info("calculator", ".")
for line in result.split("\n"):
    print(f"    {line}")

print()
print("Result for 'pkg' directory:")
result = get_files_info("calculator", "pkg")
for line in result.split("\n"):
    print(f"    {line}")

print()
print("Result for '/bin' directory:")
result = get_files_info("calculator", "/bin")
for line in result.split("\n"):
    print(f"    {line}")

print()
print("Result for '../' directory:")
result = get_files_info("calculator", "../")
for line in result.split("\n"):
    print(f"    {line}")
