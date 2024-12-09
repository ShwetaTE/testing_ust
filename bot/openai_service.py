import openai


from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY


def ask_openai(prompt):
    print("inside ask openai",prompt)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the latest model (gpt-4)
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,  # Controls the randomness of the response
            max_tokens=200,  # Limits the length of the response
            top_p=1,         # Nucleus sampling parameter
            frequency_penalty=0,  # Discourages repeated phrases
            presence_penalty=0    # Encourages new topics
        )
        # Extract and return the content of the response
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        # Handle errors and return an error message
        return f"An error occurred: {str(e)}"