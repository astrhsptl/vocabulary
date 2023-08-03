from os.path import join
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

MEDIA_DIR = "media"
MEDIA_ROOT = join(BASE_DIR, MEDIA_DIR)
MEDIA_URL = "/{MEDIA_DIR}/"