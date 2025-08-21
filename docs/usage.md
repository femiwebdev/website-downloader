# Usage Instructions for Website Downloader

## Overview
The Website Downloader is a Python application designed to scan a given URL and download the entire website, including HTML content, files, and media, into a `public_html` directory.

## Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

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
To use the Website Downloader, follow these steps:

1. **Run the application**:
   You can run the application using the provided shell script:
   ```
   ./scripts/run.sh
   ```

2. **Provide the URL**:
   When prompted, enter the URL of the website you wish to download. The application will start crawling the website and downloading the content.

3. **Check the output**:
   After the process completes, you will find all downloaded files in the `public_html` directory located in the project root.

## Example
To download a website, simply run the application and input the desired URL:
```
Enter the URL to download: https://example.com
```

The application will handle the rest, saving all relevant files and media in the `public_html` directory.

## Notes
- Ensure that you have permission to download the website content.
- The application may take some time to complete, depending on the size of the website and your internet connection speed.