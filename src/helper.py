import argparse
import sys

class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Download transcripts from YouTube videos.')
        self.add_arguments()

    def add_arguments(self):
        """
        Parse command line arguments.

        Returns:
            argparse.Namespace: The parsed arguments as a namespace object.
        """
        self.parser.add_argument('--download', metavar='VIDEO_ID', required=True, help='the video ID to download the transcript from')
        self.parser.add_argument('-o', '--output', metavar='OUTPUT_FILE', required=True, help='the name of the output file')
        self.parser.add_argument('-f', '--format', action='store_true', help='format the transcript by removing unwanted characters like numbers and punctuation')
        self.parser.add_argument('-l', '--language', metavar='LANGUAGE_CODE', default=['en'], nargs='+', help='language codes of the transcript, default is "en"')
        self.parser.add_argument('-ai', '--use-ai', action='store_true', help='use ChatGPT to format and improve the transcript content')
        self.parser.add_argument('-s', '--summarize', action='store_true', help='summarize the transcript video. This option requires the --use-ai option to be enabled')

    def parse_arguments(self):
        args = self.parser.parse_args()
        if args.summarize and not args.use_ai:
            self.parser.error("The option '-s' requires '-ai' to be enabled.")
        return args


def main():
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()
    # rest of your code

if __name__ == "__main__":
    main()
