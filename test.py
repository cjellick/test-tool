import hashlib
import json
import os
import sys

SUPPORTED_HASH_ALGORITHMS = ['sha256', 'md5']


def main():
    # Extract the tool's `data` argument from the env
    param1 = os.getenv('PARAM1')
    foo = os.getenv('FOO')

    print(f"PARAM1 is {param1}. FOO is {foo}.")

    # Get all environment variables
    env_vars = os.environ

    # Print all environment variables
    for key, value in env_vars.items():
        print(f"key: {key}; val: {value}")


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        # Print err to stdout to return the error to the assistant
        print(f'Error: {err}')
        sys.exit(1)
