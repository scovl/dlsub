from helper import parse_arguments
from youtube_transcript_api import YouTubeTranscriptApi
import re

class dlsub:
    def __init__(self, video_id):
        self.video_id = video_id
    
    def save_transcript(self, output_file, format=False):
        """
        Download the transcript for a YouTube video and save it to a file.

        Args:
            output_file (str): The name of the file to save the transcript to.
            format (bool, optional): Whether to format the transcript by removing
                unwanted characters like numbers and punctuation. Defaults to False.
        """
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(self.video_id)
            with open(output_file, "w", encoding="utf-8") as f:
                for item in transcript_list:
                    f.write(f"{item['text']}\n")
            print(f"Transcript saved in {output_file}.")
            
            if format:
                self.format_transcript(output_file, f"{output_file.split('.')[0]}_formatted.txt")
        except Exception as e:
            print(f"Error getting transcript: {str(e)}")
    
    def format_transcript(self, input_file, output_file):
        """
        Format a transcript file by removing unwanted characters like numbers and punctuation.

        Args:
            input_file (str): The name of the input file to be formatted.
            output_file (str): The name of the formatted output file.
        """
        with open(input_file, 'r', encoding='utf-8') as f:
            raw_transcript = f.readlines()

        formatted_transcript = []
        for line in raw_transcript:
            # Remove line breaks and extra whitespace
            line = line.strip()

            # Remove unwanted characters like numbers and punctuation
            line = re.sub(r'[^\w\s]', '', line)

            # Add formatted line to list
            formatted_transcript.append(line)

        # Save the formatted transcript to a new file
        with open(output_file, 'w', encoding='utf-8') as f:
            for line in formatted_transcript:
                f.write(f"{line}\n")

        print(f"Formatted transcript saved in {output_file}.")
        
    def minify_transcript(self, input_file, output_file):
        """
        Minify a transcript file by removing extra whitespace and line breaks.

        Args:
            input_file (str): The name of the input file to be minified.
            output_file (str): The name of the minified output file.
        """
        with open(input_file, 'r', encoding='utf-8') as f:
            raw_transcript = f.read()

        # Minify the transcript by removing extra whitespace and line breaks
        minified_transcript = re.sub(r'\s+', ' ', raw_transcript)
        minified_transcript = minified_transcript.strip()

        # Save the minified transcript to a new file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(minified_transcript)

        print(f"Minified transcript saved in {output_file}.")