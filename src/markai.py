from pychatsonic.chat import ChatSonic
import os

def process_with_ai(args, formatted_transcript):
    output_file_ai = os.path.splitext(args.output)[0] + '_ai.txt'
    chat = ChatSonic("add-your-api-key", f"{args.language}")
    ai_transcript = chat.ask(f"Apenas corrija o texto a seguir: {' '.join(formatted_transcript)}")

    with open(output_file_ai, 'w', encoding='utf-8') as file:
        file.write(ai_transcript)
    
    return output_file_ai
