# transcript_downloader.py
from youtube_transcript_api import YouTubeTranscriptApi

class TranscriptNotAvailable(Exception):
    pass

class TranscriptDownloadError(Exception): 
    pass

class TranscriptDownloader:
    def __init__(self, video_id, language_codes=None):
        self.video_id = video_id
        self.language_codes = language_codes or ['en']

    def download_transcript(self):
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(self.video_id, languages=self.language_codes)
            return transcript_list
        except Exception as e:
            error_message = str(e)
            if "Could not retrieve a transcript for the video" in error_message:
                raise TranscriptDownloadError("Transcript not available for this video. Try another video ID or language code.")
            raise TranscriptNotAvailable(error_message)

def download_and_process_transcript(args):
    downloader = TranscriptDownloader(args.download, args.language)
    try:
        transcript_list = downloader.download_transcript()
        return transcript_list, downloader
    except TranscriptNotAvailable as e:
        print(f"Error getting transcript: {str(e)}")
        return None
    except TranscriptDownloadError as e:
        print(f"Error downloading transcript: {str(e)}")
        return None
