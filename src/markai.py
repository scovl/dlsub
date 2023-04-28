import openai
import re

class Markai:
    def __init__(self, api_key):
        openai.api_key = api_key

    def convert_to_markdown(self, filepath, language='en'):
        # Read the text file
        with open(filepath, 'r') as file:
            text = file.read()

        # Remove special characters that may interfere with formatting
        text = re.sub(r'[^\x00-\x7F]+', ' ', text)

        # Set the model and format parameters for GPT-3
        model = f"text-davinci-{language}-002"
        prompt = (
            f"Convert the following text to Markdown format:\n"
            f"{text}\n"
            f"---\n"
        )
        temperature = 0.7
        max_tokens = 2048

        # Send the request to the GPT-3 API
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            n = 1,
            stop=None,
            timeout=10,
        )

        # Get the API response and format it as Markdown
        markdown = response.choices[0].text
        markdown = markdown.strip().replace('\n\n', '\n')
        markdown = re.sub(r' +\n', '\n', markdown)

        return markdown
