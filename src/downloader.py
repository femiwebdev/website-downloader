class Downloader:
    def __init__(self, url, storage):
        self.url = url
        self.storage = storage

    def download_html(self):
        import requests
        response = requests.get(self.url)
        if response.status_code == 200:
            self.storage.save_html(self.url, response.text)
            return response.text
        else:
            raise Exception(f"Failed to download HTML from {self.url}")

    def download_resources(self, html_content):
        from parser import Parser
        parser = Parser()
        resources = parser.extract_resources(html_content)
        for resource in resources:
            self.download_resource(resource)

    def download_resource(self, resource_url):
        import os
        import requests

        response = requests.get(resource_url)
        if response.status_code == 200:
            resource_path = self.storage.get_resource_path(resource_url)
            os.makedirs(os.path.dirname(resource_path), exist_ok=True)
            with open(resource_path, 'wb') as file:
                file.write(response.content)
        else:
            print(f"Failed to download resource from {resource_url}")