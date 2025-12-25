import os


def get_file_content(working_directory, file_path):
    if working_directory not in file_path:
        raise ValueError(
            f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        )
    elif not os.path.isfile(file_path):
        raise ValueError(f"File '{file_path}' does not exist")
    else:
        with open(file_path, "r") as file:
            content = file.read()
        return content
