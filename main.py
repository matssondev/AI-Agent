import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

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
    )
    usage = response.usage_metadata

    # Checks for --verbose, if true print verbose output
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {usage.prompt_token_count}")
        print(f"Response tokens: {usage.candidates_token_count}")

    print(response.text)


if __name__ == "__main__":
    main()
