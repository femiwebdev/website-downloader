class Crawler:
    def __init__(self, start_url, storage):
        self.start_url = start_url
        self.storage = storage
        self.visited = set()
        self.queue = [start_url]

    def crawl(self):
        while self.queue:
            url = self.queue.pop(0)
            if url not in self.visited:
                self.visited.add(url)
                self.process_url(url)

    def process_url(self, url):
        # Fetch the content of the URL
        content = self.fetch_content(url)
        if content:
            self.storage.save(url, content)
            links = self.extract_links(content)
            self.queue.extend(links)

    def fetch_content(self, url):
        # Logic to fetch content from the URL
        pass

    def extract_links(self, content):
        # Logic to extract links from the HTML content
        pass