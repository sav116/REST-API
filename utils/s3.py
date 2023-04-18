from typing import List, Dict, Iterator
from botocore.exceptions import ClientError
import boto3

from core.config import BUCKET, ACCESS_KEY, SECRET_KEY, ENDPOINT_URL

class S3Loader:
    """ Loader for s3 """

    def __init__(
            self,
            dir_path: str = None,
            file_path: str = None,
            files: list = None,
            bucket: str = BUCKET):
        self.dir_path = dir_path
        self.files = files
        self.bucket = bucket
        self.file_path = file_path
        self._resource = self._get_resource()
        self._client = self._get_client()
        self._bucket = self._get_bucket()
        if file_path:
            self.object = self._get_object()
            self.file_name = file_path.split('/')[-1]
        if dir_path:
            self.objects = self._get_list_objects()

    def _get_list_objects(self):
        return self._client.list_objects(
            Bucket=self.bucket, Prefix=self.dir_path)

    def _get_object(self):
        try:
            return self._client.get_object(
                Bucket=self.bucket, Key=self.file_path)
        except ClientError:
            return None

    def _get_session(self):
        return boto3.session.Session(aws_access_key_id=ACCESS_KEY,
                                     aws_secret_access_key=SECRET_KEY)

    def _get_client(self):
        return self._get_session().client('s3', endpoint_url=ENDPOINT_URL)

    def _get_resource(self):
        return self._get_session().resource('s3', endpoint_url=ENDPOINT_URL)

    def _get_bucket(self):
        return self._resource.Bucket(self.bucket)

    def get_file_names(self) -> List[dict]:
        files = []
        for obj in self.objects['Contents']:
            files.append({obj['Key']: {
                'last_modified': obj['LastModified'],
                'size': obj['Size']
            }})
        return files

    def streamer(self) -> Iterator:
        for i in self.object['Body']:
            yield i

    def upload_files(self) -> bool:
        for file in self.files:
            try:
                self._client.upload_fileobj(
                    file.file, self.bucket,
                    self.file_path + '/' + file.filename)
            except ClientError:
                return False
        return True

    def update_file(self) -> None:
        return self._client.upload_fileobj(
            self.files[0].file, self.bucket, self.file_path)

    def delete_file(self) -> Dict:
        return self._client.delete_object(
            Bucket=self.bucket, Key=self.file_path)
