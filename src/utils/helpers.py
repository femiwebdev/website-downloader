def normalize_url(url):
    from urllib.parse import urljoin, urlparse

    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = 'http://' + url
    return urljoin(url, '/')

def create_file_path(base_path, url):
    import os
    from urllib.parse import urlparse

    parsed_url = urlparse(url)
    path = os.path.join(base_path, parsed_url.netloc, parsed_url.path.lstrip('/'))
    if path.endswith('/'):
        path += 'index.html'
    return os.path.splitext(path)[0] + '.html'

def ensure_directory_exists(directory):
    import os

    if not os.path.exists(directory):
        os.makedirs(directory)

def get_file_extension(url):
    from urllib.parse import urlparse

    parsed_url = urlparse(url)
    return os.path.splitext(parsed_url.path)[1]