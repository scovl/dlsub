from pychatsonic.chat import ChatSonic
import os

def process_with_ai(args, formatted_transcript):
    api_key = "add-your-api-key"

    if not api_key or api_key == "add-your-api-key":
        print("Invalid API key. Please provide a valid API key.")
        return

    output_file_ai = os.path.splitext(args.output)[0] + '_ai.txt'
    try:
        chat = ChatSonic(api_key, f"{args.language}")
        ai_transcript = chat.ask(f"Just correct the following text in the language {args.language} and separate the paragraphs correctly: {' '.join(formatted_transcript)}")
    except Exception as e:
        print("Error processing with AI: {}".format(e))
        return
    
    with open(output_file_ai, 'w', encoding='utf-8') as file:
        file.write(ai_transcript)
    
    return output_file_ai
