from youtube_transcript_api import YouTubeTranscriptApi

def save_transcript(video_id, output_file):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        with open(output_file, "w", encoding="utf-8") as f:
            for item in transcript_list:
                f.write(f"{item['text']}\n")
        print(f"Transcript saved in {output_file}.")
    except Exception as e:
        print(f"Error getting transcript: {str(e)}")

# Replace 'video_id' with the YouTube video ID of your choice
# ID of the YouTube video you want to download subtitles from. The video ID is the part of the URL after watch?v=.
video_id = 'QOIJeIbxquM'
output_file = f"{video_id}_transcript.txt"

save_transcript(video_id, output_file)
