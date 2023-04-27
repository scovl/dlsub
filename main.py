from dlsub import dlsub

def main():
    # Video ID of the YouTube video you want to download subtitles from
    video_id = 'QOIJeIbxquM'

    # Path to the directory where the transcript will be saved
    output_dir = 'transcripts'

    # Path to the output file
    output_file = f"{output_dir}/{video_id}_transcript.txt"

    # Create the dlsub object and call save_transcript to download the transcript
    downloader = dlsub(video_id)
    downloader.save_transcript(output_file)

if __name__ == '__main__':
    main()
