from celery import shared_task
from .services import Disruptor
import logging

logging.basicConfig(filename='disruptor.log',
                    format='%(asctime)s - %(message)s',
                    level=logging.INFO)


@shared_task
def start_download():
    disruptor = Disruptor()
    status_code = disruptor.download()

    logging.info(
        f'File downloaded: {status_code}'
    )
