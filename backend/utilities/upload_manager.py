import os
import boto3
from botocore.exceptions import NoCredentialsError
import zipfile

aws_cred = {
    "aws_access_key_id": "AKIAXZV2YEWWPXRTAG5X",
    "aws_secret_access_key": "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"
}

path = "/workspace/resume-scorer/ziptest.zip"


class Upload_Manager:
    def __init__(self, path, s3_path):
        path = self.path
        s3_path = self.s3_path

    def unzip_folder(self):
        with zipfile.ZipFile(self.path, 'r') as zip:
            zip.extractall(self.s3_path)

    def save_files_to_s3(self):
        pass


class Transform_data:
    def __init__(self):
        pass

    def get_list_of_files(self):
        pass

    def transform_file(self):
        pass

class connection_to_s3:
    def __init__(self):
        self

    def connect_s3(self):
        session = boto3.Session(
            aws_access_key_id = aws_cred["aws_access_key_id"],
            aws_secret_access_key = aws_cred["aws_secret_access_key"]
        )

        s3 = session.resource('s3')
        bucket_name = 'gagan-s-bucket'
        bucket = s3.Bucket(bucket_name)
        return bucket_name


conn = connection_to_s3()

x = conn.connect_s3()

print(x)
