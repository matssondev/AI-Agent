import os

from google.genai import types

from config import MAX_CHARS

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets the content of a file within the permitted working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path to get content from, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)


# Get content of a file within the permitted working directory
def get_file_content(working_directory, file_path):
    abs_working = os.path.abspath(working_directory)
    abs_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file.startswith(abs_working + os.sep):
        return f'Error: Cannot read "{abs_file}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file):
        return f'Error: "{abs_file}" is not a file or does not exist'

    try:
        with open(abs_file, "r") as file:
            content = file.read(MAX_CHARS)
        return content
    except Exception as e:
        return f"Error: {e}"
