# main.py
import os
import json
from src.helper import parse_arguments
from src.transcript_downloader import TranscriptDownloader
from src.transcript_processor import TranscriptProcessor

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Download transcript
    downloader = TranscriptDownloader(args.download, ['pt', 'en'])  # Get transcript in Portuguese or English
    transcript_list = downloader.download_transcript()

    # Save transcript to output file
    if transcript_list is not None:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(transcript_list, f)
        print(f"Transcript saved in {args.output}.")
    else:
        print("Transcript download failed.")

    # Process transcript
    if args.format or args.minify:
        with open(args.output, 'r', encoding='utf-8') as f:
            raw_transcript = json.load(f)  # Use json.load() instead of f.readlines()

        processor = TranscriptProcessor(raw_transcript)

        if args.format:
            formatted_transcript = processor.format_transcript()
            output_file = os.path.splitext(args.output)[0] + '_formatted.txt'

        if args.minify:
            minified_transcript = processor.minify_transcript()
            output_file = os.path.splitext(args.output)[0] + '_minified.txt'

        with open(output_file, 'w', encoding='utf-8') as f:
            if args.format:
                for line in formatted_transcript:
                    f.write(f"{line}\n")

            if args.minify:
                f.write(minified_transcript)

        print(f"Processed transcript saved in {output_file}.")

if __name__ == '__main__':
    main()
