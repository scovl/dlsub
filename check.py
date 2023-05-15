from pychatsonic.chat import ChatSonic

# Abrir o arquivo 'porta.txt' e ler seu conteúdo
with open('porta.txt', 'r') as file:
    transcript = file.read()

def format_transcript_with_chatsonic(transcript, language):

    chat = ChatSonic("8516f106-cacb-42ad-96a8-e49387865e9e", "pt")
    text = chat.ask(f"Apenas corrija o texto a seguir: {transcript}")

    print(text)
