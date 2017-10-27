"""
    Our own minio object
"""

from minio import Minio

from stock_common.conf.config import Config

CONFIGS = Config.get_configs()


minio_client = Minio(
    CONFIGS.MINIO_HOST,
    access_key=CONFIGS.MINIO_ACCESS_KEY,
    secret_key=CONFIGS.MINIO_SECRET_KEY,
    secure=False
)
