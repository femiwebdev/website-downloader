class Storage:
    def __init__(self, base_path='public_html'):
        self.base_path = base_path

    def save_html(self, url, content):
        file_path = self._get_file_path(url, 'html')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    def save_file(self, url, content):
        file_path = self._get_file_path(url)
        with open(file_path, 'wb') as file:
            file.write(content)

    def _get_file_path(self, url, extension=None):
        from urllib.parse import urlparse
        import os

        parsed_url = urlparse(url)
        path = parsed_url.path.strip('/')

        if not path:
            path = 'index.html'
        elif extension:
            path = f"{path}.{extension}"

        file_path = os.path.join(self.base_path, path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        return file_path