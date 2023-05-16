from pychatsonic.chat import ChatSonic
import os

class InvalidApiKeyError(Exception):
    """Exception raised for errors in the API key.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Invalid API key. Please provide a valid API key."):
        self.message = message
        super().__init__(self.message)
        
class AiProcessor:
    def __init__(self, api_key):
        self.api_key = api_key
        try:
            if not self._check_api_key():
                raise InvalidApiKeyError()
        except InvalidApiKeyError as e:
            print(e)
            return
        self.chat = None
    
    def _check_api_key(self):
        return False if not self.api_key or self.api_key == "add-your-api-key" else True

    def _get_output_filename(self, output):
        return os.path.splitext(output)[0] + '.txt'

    def _process_transcript(self, language, formatted_transcript, question):
        try:
            self.chat = ChatSonic(self.api_key, language)
            ai_transcript = self.chat.ask(question.format(language=language, transcript=' '.join(formatted_transcript)))
            return ai_transcript
        except Exception as e:
            print("Error processing with AI: {}".format(e))
            return None

    def _write_to_file(self, output_file, ai_transcript):
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(ai_transcript)
    
    def process_with_ai(self, args, formatted_transcript):
        output_file = self._get_output_filename(args.output)
        question = "Just correct the following text in the language {language} and separate the paragraphs correctly: {transcript}"
        
        ai_transcript = self._process_transcript(args.language, formatted_transcript, question)
        if ai_transcript is None:
            return
        
        self._write_to_file(output_file, ai_transcript)

        return output_file

    def summarize_with_ai(self, args, formatted_transcript):
        output_file = self._get_output_filename(args.output)
        question = "Summarize the following text in the language {language} and separate the paragraphs correctly: {transcript}"

        ai_transcript = self._process_transcript(args.language, formatted_transcript, question)
        if ai_transcript is None:
            return

        self._write_to_file(output_file, ai_transcript)
        
        return output_file
