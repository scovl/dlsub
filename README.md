# dlsub

dlsub is a command line tool for downloading transcripts of YouTube videos. It uses the YouTube Transcript API to download the transcript and save it to a file. The downloaded transcript can be optionally formatted to remove unwanted characters like numbers and punctuation.

## Usage

To download a transcript for a YouTube video, use the following command:

```bash
./dlsub.py --download <video_id> -o <path/to/transcript.txt>
```


Replace `<video_id>` with the ID of the YouTube video you want to download subtitles from. The video ID is the part of the URL after `watch?v=`. By default, the transcript will not be formatted. To format the transcript, use the `-f` or `--format` option:

```bash
./dlsub.py --download <video_id> -o <path/to/transcript.txt> -f
```

This will download the transcript and save it to `<path/to/transcript_formatted.txt>`.

## Installation

1. Create venv environment `python3 venv -m py3nv`.
2. Clone this repository.
3. Install the required packages with `pip install -r requirements.txt`.
4. Run `./dlsub.py` to download transcripts for YouTube videos.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

