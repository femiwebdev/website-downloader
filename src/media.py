class MediaHandler:
    def __init__(self, storage):
        self.storage = storage

    def download_media(self, media_url):
        # Logic to download media files (images, videos, etc.)
        pass

    def save_media(self, media_content, media_name):
        # Logic to save media files to the storage
        pass

    def handle_media(self, media_urls):
        for url in media_urls:
            media_content = self.download_media(url)
            media_name = url.split("/")[-1]
            self.save_media(media_content, media_name)