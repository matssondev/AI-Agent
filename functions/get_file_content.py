import os

from config import MAX_CHARS


# Get content of a file within the permitted working directory
def get_file_content(working_directory, file_path):
    if working_directory not in file_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(file_path):
        return f'Error: "{file_path}" is not a file or does not exist'

    try:
        with open(file_path, "r") as file:
            content = file.read(MAX_CHARS)
        return content
    except Exception as e:
        return f"Error: {e}"
