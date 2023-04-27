import re

def format_transcript(input_file, output_file):
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

    print(f"Transcrição formatada salva em {output_file}.")

# Replace 'input_file' with the name of the input file containing the original transcript
input_file = f"{video_id}_transcript.txt"
output_file = f"{video_id}_formatted_transcript.txt"

format_transcript(input_file, output_file)
