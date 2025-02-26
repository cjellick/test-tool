import os
import sys
import json
import asyncio
from gptscript import GPTScript, Options

async def main():
    # Set up GPTScript client
    client = GPTScript()

    # Create system prompt input
    sys_prompt = {
        "message": "Favorite color?",
        "fields": "color"
        "sensitive": False,
    }

    try:
        # Run GPTScript with the system prompt and get response
        res = await client.run(
            "sys.prompt", 
            Options(input=json.dumps(sys_prompt))
        ).text()
        
        print(res)

    except Exception as err:
        print(f"Error: {err}")
        sys.exit(1)

if __name__ == '__main__':
    asyncio.run(main())
