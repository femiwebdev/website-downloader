import unittest
from src.downloader import Downloader

class TestDownloader(unittest.TestCase):

    def setUp(self):
        self.downloader = Downloader()

    def test_download_html(self):
        url = "http://example.com"
        content = self.downloader.download_html(url)
        self.assertIn("<html", content)
        self.assertIn("</html>", content)

    def test_download_file(self):
        url = "http://example.com/sample.pdf"
        file_path = self.downloader.download_file(url)
        self.assertTrue(os.path.exists(file_path))

    def test_handle_invalid_url(self):
        url = "http://invalid-url"
        with self.assertRaises(ValueError):
            self.downloader.download_html(url)

    def test_download_media(self):
        url = "http://example.com/image.png"
        media_path = self.downloader.download_media(url)
        self.assertTrue(os.path.exists(media_path))

if __name__ == '__main__':
    unittest.main()