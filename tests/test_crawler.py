import unittest
from src.crawler import Crawler

class TestCrawler(unittest.TestCase):

    def setUp(self):
        self.crawler = Crawler()

    def test_initialization(self):
        self.assertIsNotNone(self.crawler)

    def test_fetch_url(self):
        url = "http://example.com"
        response = self.crawler.fetch_url(url)
        self.assertEqual(response.status_code, 200)

    def test_extract_links(self):
        html_content = "<html><body><a href='http://example.com'>Example</a></body></html>"
        links = self.crawler.extract_links(html_content)
        self.assertIn("http://example.com", links)

    def test_crawl(self):
        start_url = "http://example.com"
        self.crawler.crawl(start_url)
        # Assuming the crawler has a method to get crawled URLs
        crawled_urls = self.crawler.get_crawled_urls()
        self.assertIn(start_url, crawled_urls)

if __name__ == '__main__':
    unittest.main()