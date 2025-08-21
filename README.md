# Website Downloader

Website Downloader is a Python application designed to scan a given web URL and download the entire website, including HTML content, files, and media, into a `public_html` directory. This tool is useful for web developers, researchers, and anyone interested in archiving web content.

## Features

- Crawl a specified URL and gather all linked resources.
- Download HTML pages, images, videos, and other media files.
- Save all downloaded content in a structured `public_html` directory.
- Configurable settings for base URLs and download paths.
- Logging support to track events and errors during execution.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/website-downloader.git
   cd website-downloader
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, you can use the provided shell script:

```
scripts/run.sh <URL>
```

Replace `<URL>` with the website you want to download.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.