import os


def write_file(working_directory, file_path, content):
    abs_working = os.path.abspath(working_directory)
    abs_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file.startswith(abs_working + os.sep):
        return f'Error: Cannot read "{abs_file}" as it is outside the permitted working directory'

    if os.path.isdir(abs_file):
        return f'Error: "{abs_file}" is not a file or does not exist'

    try:
        with open(abs_file, "w") as file:
            file.write(content)
        return f'Successfully wrote to "{abs_file}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Failed to write file "{abs_file}": {str(e)}'
