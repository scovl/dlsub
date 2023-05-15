import os
import json
from src.helper import ArgumentParser
from src.transcript_manager import download_and_process_transcript
from src.transcript_processor import TranscriptProcessor
from src.markai import AiProcessor

class DlSub:
    def __init__(self):
        self.argument_parser = ArgumentParser()
        self.args = self.argument_parser.parse_arguments()

    def format_transcript(self, formatted_transcript):
        output_file = os.path.splitext(self.args.output)[0] + '.txt'
        if os.path.exists(output_file):
            overwrite = input(f"File {output_file} already exists. Overwrite? (y/n) ")
            if overwrite.lower() != 'y':
                output_file = os.path.splitext(self.args.output)[0] + '_1.txt'

        with open(output_file, 'w', encoding='utf-8') as f:
            for line in formatted_transcript:
                f.write(f"{line}\n")
        print(f"Processed transcript saved in {output_file}.")

    def process_with_ai(self, ai_processor, formatted_transcript):
        output_file_ai = ai_processor.process_with_ai(self.args, formatted_transcript)
        print(f"AI processed transcript saved in {output_file_ai}.")

    def summarize_with_ai(self, ai_processor, formatted_transcript):
        output_file_ai = ai_processor.summarize_with_ai(self.args, formatted_transcript)
        print(f"AI summarized transcript saved in {output_file_ai}.")

    def run(self):
        # Download and process transcript
        transcript_list, downloader = download_and_process_transcript(self.args)
        if transcript_list is None:
            print("Transcript download failed.")
            return

        # Save transcript to output file
        with open(self.args.output, 'w', encoding='utf-8') as f:
            json.dump(transcript_list, f)
        print(f"Transcript saved in {self.args.output}.")

        # Process transcript
        if self.args.format or self.args.use_ai:
            with open(self.args.output, 'r', encoding='utf-8') as f:
                raw_transcript = json.load(f)

            processor = TranscriptProcessor(raw_transcript, self.args.language)
            formatted_transcript = processor.format_transcript()

            if self.args.format:
                self.format_transcript(formatted_transcript)

            if self.args.use_ai or self.args.summarize:
                ai_processor = AiProcessor("add-your-api-key")  # replace with your actual API key
                if self.args.use_ai:
                    self.process_with_ai(ai_processor, formatted_transcript)
                if self.args.summarize:
                    self.summarize_with_ai(ai_processor, formatted_transcript)


if __name__ == '__main__':
    app = DlSub()
    app.run()
