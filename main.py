# main.py
from transcript_downloader import TranscriptDownloader
from transcript_processor import TranscriptProcessor

video_id = 'QOIJeIbxquM'
output_file = "transcript.txt"

# Instantiate an object of the TranscriptDownloader class
downloader = TranscriptDownloader(video_id)

# Call the download_transcript method to get the transcript
transcript = downloader.download_transcript()

# Instantiate an object of the TranscriptProcessor class
processor = TranscriptProcessor(transcript)

# Format the transcript and save it to a new file
formatted_transcript = processor.format_transcript()
with open(f"{output_file.split('.')[0]}_formatted.txt", "w", encoding="utf-8") as
