import sys
import json
import asyncio
import traceback
from gptscript import GPTScript, Options

async def main():
    # Set up GPTScript client
    client = GPTScript()

    # Create system prompt input
    sys_prompt = {
        "message": "I'd like to get to know you better. Can you tell me some of your favorite things?",
        "fields": [
            {
                "name": "Color",
                "sensitive": False,
                "description": "Your favorite color"
            },
            {
                "name": "Food",
                "sensitive": False,
                "description": "Your favorite food"
            },
            {
                "name": "Drink",
                "sensitive": False,
                "description": "Your favorite drink"
            }, 
            {
                "name": "Animal",
                "sensitive": False,
                "description": "Your favorite animal"
            },
            {
                "name": "Book",
                "sensitive": False,
                "description": "Your favorite book"
            }
        ]
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
        print("Full stack trace:")
        print(traceback.format_exc())
        sys.exit(1)

if __name__ == '__main__':
    asyncio.run(main())
