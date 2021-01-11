import os
from datetime import datetime
from post_service.config.base import MEDIA_ROOT


def save_file(file):
    if not file:
        return None
    filename, file_extension = os.path.splitext(file.filename)
    filename = f'{filename} + {datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}{file_extension}'
    if not os.path.isdir(MEDIA_ROOT):
        os.mkdir(MEDIA_ROOT)
    file_path = os.path.join(MEDIA_ROOT, filename)
    file.save(file_path)
    return filename
