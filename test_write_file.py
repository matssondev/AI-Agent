from functions.write_file import write_file

print(
    write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
)  # Overwrite existing
print(
    write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
)  # Create new (creates pkg if needed)
print(
    write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
)  # Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory
