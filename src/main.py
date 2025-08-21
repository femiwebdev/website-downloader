import sys
from downloader import Downloader
from config import Config
from logger import setup_logger

def main():
    setup_logger()
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    downloader = Downloader(url)
    downloader.start_downloading()

if __name__ == "__main__":
    main()