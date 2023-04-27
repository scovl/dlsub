import unittest
from unittest.mock import patch, MagicMock
from dlsub import dlsub

class TestDlSub(unittest.TestCase):

    @patch('youtube_transcript_api.YouTubeTranscriptApi.get_transcript')
    def test_save_transcript(self, mock_get_transcript):
        # Set up the test
        video_id = 'QOIJeIbxquM'
        output_file = f"{video_id}_test_transcript.txt"
        downloader = dlsub(video_id)

        # Mock the YouTubeTranscriptApi.get_transcript method
        mock_transcript = [{'text': 'Hello, world!'}]
        mock_get_transcript.return_value = mock_transcript

        # Call the save_transcript method
        downloader.save_transcript(output_file)

        # Check that the file was saved
        with open(output_file, 'r', encoding='utf-8') as f:
            transcript_text = f.read()
        self.assertIsNotNone(transcript_text)

    def test_format_transcript(self):
        # Set up the test
        input_file = 'test_transcript.txt'
        output_file = 'test_formatted_transcript.txt'
        downloader = dlsub('')

        # Call the format_transcript method
        downloader.format_transcript(input_file, output_file)

        # Check that the file was saved
        with open(output_file, 'r', encoding='utf-8') as f:
            formatted_text = f.read()
        self.assertIsNotNone(formatted_text)

if __name__ == '__main__':
    unittest.main()
