import json
from src.transcript_downloader import TranscriptDownloader, TranscriptNotAvailable, TranscriptDownloadError
from src.transcript_processor import TranscriptProcessor

def download_and_process_transcript(args):
    try:
        downloader = TranscriptDownloader(args.download, args.language)
        transcript_list = downloader.download_transcript()
    except TranscriptDownloadError as e:
        print(e)
        return None, None  # Return a tuple of None values
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None, None  # Return a tuple of None values

    return transcript_list, downloader
