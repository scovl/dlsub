# transcript_processor.py
import re
import json

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
            # Extract 'text' value
            text = transcript_item['text']

            # Add text to the current paragraph
            paragraph_lines.append(text)

            # If the current paragraph has 5 lines or this is the last line, join the paragraph and add it to the list
            if (i + 1) % 5 == 0 or i == len(self.raw_transcript) - 1:
                paragraph = ' '.join(paragraph_lines)
                formatted_transcript.append(paragraph)
                paragraph_lines = []

                # Increment paragraph count
                paragraph_count += 1

                # Add a blank line after every 5 paragraphs
                if paragraph_count % 5 == 0:
                    formatted_transcript.append("")

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

