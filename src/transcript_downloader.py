# transcript_downloader.py
from youtube_transcript_api import YouTubeTranscriptApi

class TranscriptDownloader:
    """
    A class that can download transcripts of YouTube videos.
    """
    def __init__(self, video_id):
        self.video_id = video_id

    def download_transcript(self):
        """
        Download the transcript for a YouTube video.

        Returns:
            List[Dict[str, Union[str, float, int]]]: A list of dictionaries representing each
            part of the transcript, with 'text', 'start' and 'duration' keys.
        """
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(self.video_id)
            return transcript_list
        except Exception as e:
            print(f"Error getting transcript: {str(e)}")
            return None
