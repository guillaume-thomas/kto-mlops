from abc import abstractmethod, ABC


class IS3ClientWrapper(ABC):
    @abstractmethod
    def download_file(self, bucket: str, s3_path: str, dest_filename: str) -> None:
        pass


class S3ClientWrapper(IS3ClientWrapper):
    def __init__(self, s3_client):
        self.s3_client = s3_client

    def download_file(self, bucket: str, s3_path: str, dest_filename: str):
        self.s3_client.download_file(bucket, s3_path, dest_filename)
