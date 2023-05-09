import argparse

def parse_arguments():
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: The parsed arguments as a namespace object.
    """
    parser = argparse.ArgumentParser(description='Download transcripts from YouTube videos.')

    # Required arguments
    parser.add_argument('--download', metavar='VIDEO_ID', required=True, help='the video ID to download the transcript from')
    parser.add_argument('-o', '--output', metavar='OUTPUT_FILE', required=True, help='the name of the output file')

    # Optional arguments
    parser.add_argument('-f', '--format', action='store_true', help='format the transcript by removing unwanted characters like numbers and punctuation')
    parser.add_argument('-m', '--minify', action='store_true', help='minify the transcript by removing extra whitespace and line breaks')
    parser.add_argument('-l', '--language', metavar='LANGUAGE_CODE', default=['en'], nargs='+', help='language codes of the transcript, default is "en"')

    return parser.parse_args()
