import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import available_functions, call_function
from prompts import system_prompt

# set environment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set")

# initialize client
client = genai.Client(api_key=api_key)


def main():
    # Command-line parser
    parser = argparse.ArgumentParser(description="AI Agent")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    # User input
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Response generation
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )
    usage = response.usage_metadata

    # Checks for --verbose, if true print verbose output
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {usage.prompt_token_count}")
        print(f"Response tokens: {usage.candidates_token_count}")

    function_calls = response.function_calls
    if function_calls:
        function_results = []
        for function_call in function_calls:
            function_call_result = call_function(function_call, verbose=args.verbose)

            if not function_call_result.parts:
                raise Exception("No parts in function call result")

            if function_call_result.parts[0].function_response is None:
                raise Exception("No function_response in result")

            if function_call_result.parts[0].function_response.response is None:
                raise Exception("No response in function_response")

            function_results.append(function_call_result.parts[0])

            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")
    elif response.text:
        print(response.text)


if __name__ == "__main__":
    main()
