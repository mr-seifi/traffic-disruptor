import requests


class Disruptor:

    def __init__(self):
        self._url = 'https://speed.hetzner.de/10GB.bin'

    def download(self) -> int:
        r = requests.get(
            self._url
        )

        return r.status_code
