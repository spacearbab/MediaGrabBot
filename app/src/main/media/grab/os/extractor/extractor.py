import yt_dlp
import asyncio
from typing import Optional
from app.src.main.media.grab.os.data.model.models import MediaInfo, MediaFormat

class MediaExtractor:
    """
    موتور اصلی استخراج لینک. 
    پشتیبانی از 1000+ سایت. کاملاً Async برای جلوگیری از فریز شدن ربات.
    """
    def __init__(self):
        self._ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,
            'noplaylist': True,
            'extract_flat': False,
        }

    async def extract(self, url: str) -> Optional[MediaInfo]:
        loop = asyncio.get_event_loop()
        try:
            info_dict = await loop.run_in_executor(None, self._extract_sync, url)
            if not info_dict:
                return None
            
            formats = []
            for f in info_dict.get('formats', []):
                formats.append(MediaFormat(
                    format_id=f.get('format_id', ''),
                    ext=f.get('ext', 'mp4'),
                    resolution=f.get('resolution', 'Audio Only' if f.get('vcodec') == 'none' else 'Unknown'),
                    filesize=f.get('filesize') or f.get('filesize_approx', 0),
                    vcodec=f.get('vcodec', 'none'),
                    acodec=f.get('acodec', 'none'),
                    fps=f.get('fps', 0.0)
                ))
            
            return MediaInfo(
                title=info_dict.get('title', 'Unknown'),
                thumbnail=info_dict.get('thumbnail'),
                duration=info_dict.get('duration', 0),
                uploader=info_dict.get('uploader', 'Unknown'),
                extractor=info_dict.get('extractor_key', 'Generic'),
                url=url,
                formats=formats
            )
        except Exception as e:
            print(f"Extraction Error for {url}: {e}")
            return None

    def _extract_sync(self, url: str) -> dict:
        with yt_dlp.YoutubeDL(self._ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)
