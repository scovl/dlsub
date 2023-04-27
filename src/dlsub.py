import re
from youtube_transcript_api import YouTubeTranscriptApi

class dlsub:
    def __init__(self, video_id):
        self.video_id = video_id
    
    def save_transcript(self, output_file, format=False):
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

if __name__ == '__main__':
    video_id = 'QOIJeIbxquM'
    output_file = f"{video_id}_transcript.txt"

    downloader = dlsub(video_id)
    downloader.save_transcript(output_file, format=True)
