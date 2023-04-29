# transcript_processor.py
import re

class TranscriptProcessor:
    """
    A class that can process transcripts of YouTube videos.
    """
    def __init__(self, raw_transcript):
        self.raw_transcript = raw_transcript

    def format_transcript(self):
        """
        Format a transcript by removing unwanted characters like numbers and punctuation.

        Returns:
            List[str]: A list of formatted transcript lines.
        """
        formatted_transcript = []
        for line in self.raw_transcript:
            # Remove line breaks and extra whitespace
            line = line.strip()

            # Remove unwanted characters like numbers and punctuation
            line = re.sub(r'[^\w\s]', '', line)

            # Add formatted line to list
            formatted_transcript.append(line)

        return formatted_transcript

    def minify_transcript(self):
        """
        Minify a transcript by removing extra whitespace and line breaks.

        Returns:
            str: The minified transcript.
        """
        # Minify the transcript by removing extra whitespace and line breaks
        minified_transcript = re.sub(r'\s+', ' ', self.raw_transcript)
        minified_transcript = minified_transcript.strip()

        return minified_transcript
