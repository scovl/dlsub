import openai

# Configure sua chave de API
openai.api_key = "YOUR-API-KEY"

def format_transcript_with_chatgpt(transcript, language):
    prompt = f"Rewrite the following text in {language}, correcting grammatical and punctuation errors, and making it didactic: {transcript}"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()
