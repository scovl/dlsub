import os
import json
from src.helper import parse_arguments
from src.transcript_manager import download_and_process_transcript
from src.transcript_processor import TranscriptProcessor
from src.markai import format_transcript_with_chatgpt

def main():
    # Parse command line arguments
    args = parse_arguments()

    # Download and process transcript
    transcript_list, downloader = download_and_process_transcript(args)
    if transcript_list is None:
        print("Transcript download failed.")
        return

    # Save transcript to output file
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(transcript_list, f)
    print(f"Transcript saved in {args.output}.")

    # Process transcript
    if args.format or args.minify or args.use_ai:
        with open(args.output, 'r', encoding='utf-8') as f:
            raw_transcript = json.load(f)

        processor = TranscriptProcessor(raw_transcript, args.language)

        if args.format:
            formatted_transcript = processor.format_and_show_progress()
            output_file = os.path.splitext(args.output)[0] + '.txt'

        if args.minify:
            minified_transcript = processor.minify_transcript()
            output_file = os.path.splitext(args.output)[0] + '.txt'
            
        if args.use_ai: 
            with open(os.path.splitext(args.output)[0] + '.txt', 'r', encoding='utf-8') as f:
                raw_formatted_transcript = f.read()
            chatgpt_formatted_transcript = format_transcript_with_chatgpt(raw_formatted_transcript, args.language[0])
            output_file = os.path.splitext(args.output)[0] + '_ai.txt'

        with open(output_file, 'w', encoding='utf-8') as f:
            if args.format:
                for line in formatted_transcript:
                    f.write(f"{line}\n")

            if args.minify:
                f.write(minified_transcript)
                

            if args.use_ai: 
                f.write(chatgpt_formatted_transcript)

        print(f"Processed transcript saved in {output_file}.")

if __name__ == '__main__':
    main()
