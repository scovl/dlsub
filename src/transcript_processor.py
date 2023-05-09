import re
import json
from spellchecker import SpellChecker
from textwrap import fill
from tqdm import tqdm

class TranscriptProcessor:
    """
    A class that can process transcripts of YouTube videos.
    """
    def __init__(self, raw_transcript):
        self.raw_transcript = raw_transcript

    def format_transcript(self):
        """
        Format a transcript by extracting only 'text' values and grouping them into paragraphs of 5 lines each,
        with a blank line between every 5 paragraphs.

        Returns:
            List[str]: A list of formatted transcript paragraphs.
        """
        formatted_transcript = []
        paragraph_lines = []
        paragraph_count = 0

        for i, transcript_item in enumerate(self.raw_transcript):
            # Extract 'text' value and normalize whitespace
            text = re.sub(r'\s+', ' ', transcript_item['text']).strip()

            # Add text to the current paragraph
            paragraph_lines.append(text)

            # If the current paragraph has 5 lines or this is the last line, join the paragraph and add it to the list
            if (i + 1) % 5 == 0 or i == len(self.raw_transcript) - 1:
                paragraph = ' '.join(paragraph_lines)
                paragraph = paragraph.capitalize()
                formatted_transcript.append(paragraph)
                paragraph_lines = []

                # Increment paragraph count
                paragraph_count += 1

                # Add a blank line after every 5 paragraphs
                if paragraph_count % 5 == 0:
                    formatted_transcript.append("")

        return formatted_transcript

    def format_and_show_progress(self):
        # Call format_transcript() method
        formatted_transcript = self.format_transcript()

        # Calculate the total number of lines
        total_lines = len(formatted_transcript)

        # Iterate through the formatted_transcript and display progress
        for i, line in enumerate(formatted_transcript):
            print(f"\rProcessing line {i + 1}/{total_lines}", end="")

        print("\nFinished processing transcript.")
        return formatted_transcript

    def minify_transcript(self):
        """
        Minify a transcript by removing extra whitespace and line breaks.

        Returns:
            str: The minified transcript.
        """
        # Convert the raw_transcript list to a single string
        transcript_string = " ".join([item["text"] for item in self.raw_transcript])

        # Minify the transcript by removing extra whitespace and line breaks
        minified_transcript = re.sub(r'\s+', ' ', transcript_string)
        minified_transcript = minified_transcript.strip()

        return minified_transcript
