import os


class Disruptor:

    def __init__(self):
        self._url = 'https://speed.hetzner.de/10GB.bin'

    def download(self) -> int:
        os.system(f'wget {self._url}')
        os.system(f'rm -f 10GB.bin')

        return 200
