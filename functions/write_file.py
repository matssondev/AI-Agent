import os

from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes to file within the permitted working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to write to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)


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
