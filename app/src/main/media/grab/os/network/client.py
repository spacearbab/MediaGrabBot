import aiohttp
from typing import Dict, Any

class NetworkClient:
    """
    کلاینت HTTP غیرهمزمان (Async) برای درخواست‌های شبکه.
    """
    def __init__(self):
        self.timeout = aiohttp.ClientTimeout(total=15)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    async def fetch(self, url: str) -> Dict[str, Any]:
        async with aiohttp.ClientSession(timeout=self.timeout, headers=self.headers) as session:
            try:
                async with session.get(url) as response:
                    response.raise_for_status()
                    return await response.json()
            except Exception as e:
                print(f"Network Error: {e}")
                return {}

network_client = NetworkClient()
