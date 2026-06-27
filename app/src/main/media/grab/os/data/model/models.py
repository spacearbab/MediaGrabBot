from pydantic import BaseModel, Field
from typing import List, Optional

class MediaFormat(BaseModel):
    """مدل برای هر فرمت ویدیو یا صدا"""
    format_id: str
    ext: str
    resolution: Optional[str] = "audio-only"
    filesize: int = 0
    vcodec: Optional[str] = "none"
    acodec: Optional[str] = "none"
    fps: Optional[float] = 0.0

class MediaInfo(BaseModel):
    """مدل اصلی اطلاعات رسانه استخراج شده"""
    title: str
    thumbnail: Optional[str] = None
    duration: int = 0
    uploader: str = "Unknown"
    extractor: str = "generic"
    url: str
    formats: List[MediaFormat] = Field(default_factory=list)
    
    @property
    def progressive_formats(self) -> List[MediaFormat]:
        return [f for f in self.formats if f.vcodec != "none" and f.acodec != "none"]
    
    @property
    def audio_formats(self) -> List[MediaFormat]:
        return [f for f in self.formats if f.vcodec == "none" and f.acodec != "none"]
