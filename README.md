# dlsub

[![GitPod Ready-to-Code](https://img.shields.io/badge/Gitpod-Ready--to--Code-blue?logo=gitpod)](https://github.com/lobocode/dlsub)

dlsub is a command line tool for downloading transcripts of YouTube videos. It uses the YouTube Transcript API to download the transcript and save it to a file. The downloaded transcript can be optionally formatted to remove unwanted characters like numbers and punctuation.

## Usage

To download a transcript for a YouTube video, use the following command:

```bash
python dlsub.py --download <video_id> -o output.txt -l en
```

Replace `<video_id>` with the ID of the YouTube video you want to download subtitles from. The video ID is the part of the URL after `watch?v=`. By default, the transcript will not be formatted. To format the transcript, use the `-f` or `--format` option:

```bash
python dlsub.py --download <video_id> -o output.txt -l en -f 
```
Configure the file `config_ai.yaml` with your chatsonic api_key. Eg:

```yaml
api_key: add-your-api-key
```

To acquire your api_key, access the following video for information **[How to Get Chatsonic API Key](https://www.youtube.com/watch?v=YbRRPk9qRxY)**. Use with writesonic/chatsonic to generate a summary of the video:

```bash
python dlsub.py --download <video_id> -o output.txt -l en -ai
```

Use -s --sumarize to generate a summary of the video:

```bash
python dlsub.py --download <video_id> -o output.txt -l en -ai -s
```

## Installation

1. Clone this repository.
2. Create a Python virtual environment and activate it.
3. Install the required packages with `pip install -r requirements.txt`.
4. Run `python dlsub.py --download <video_id> -o output.txt -f` to download transcripts for YouTube videos.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate. Read our **[CONTRIBUTING.MD](https://github.com/lobocode/dlsub/blob/main/CONTRIBUTING.MD)** file.

## License

[MIT](https://choosealicense.com/licenses/mit/)
