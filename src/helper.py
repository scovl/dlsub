import argparse

def parse_arguments():
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: The parsed command line arguments.
    """
    parser = argparse.ArgumentParser(description='Download YouTube subtitles')
    parser.add_argument('--download', metavar='VIDEO_ID', required=True,
                        help='YouTube video ID')
    parser.add_argument('-o', '--output', metavar='OUTPUT_FILE', required=True,
                        help='Path to output file')
    parser.add_argument('-f', '--format', action='store_true', default=False,
                        help='Format the transcript')

    return parser.parse_args()
