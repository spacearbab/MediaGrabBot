from typing import Optional
from app.src.main.media.grab.os.extractor.extractor import MediaExtractor

class DIContainer:
    """
    کانتینر تزریق وابستگی‌ها (Singleton Pattern).
    """
    def __init__(self):
        self._extractor: Optional[MediaExtractor] = None

    @property
    def extractor(self) -> MediaExtractor:
        if self._extractor is None:
            self._extractor = MediaExtractor()
        return self._extractor

container = DIContainer()
