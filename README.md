# dlsub

dlsub is a command line tool for downloading transcripts of YouTube videos. It uses the YouTube Transcript API to download the transcript and save it to a file. The downloaded transcript can be optionally formatted to remove unwanted characters like numbers and punctuation.

## Usage

To download a transcript for a YouTube video, use the following command:

```bash
python main.py --download <video_id> -o output.txt
```

Replace `<video_id>` with the ID of the YouTube video you want to download subtitles from. The video ID is the part of the URL after `watch?v=`. By default, the transcript will not be formatted. To format the transcript, use the `-f` or `--format` option:

```bash
python main.py --download <video_id> -o output.txt -f
```

This will download the transcript and save it to `<path/to/transcript_formatted.txt>`. To minify the transcript, use the `-m` or `--minify` option:

```bash
python main.py --download <video_id> -o output.txt -m
```


## Installation

1. Clone this repository.
2. Create a Python virtual environment and activate it.
3. Install the required packages with `pip install -r requirements.txt`.
4. Run `python main.py` to download transcripts for YouTube videos.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
