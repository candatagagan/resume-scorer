import os
import boto3
import zipfile
import json
import shutil


variables_file = open('variables.json')

variables = json.load(variables_file)

path = "ziptest.zip"

saved_path = "./test_folder"

s3_path = variables["s3_path"][0]["saved"]

bucket_name = variables["s3_path"][0]["bucket_name"]


class Upload_Manager:
    def __init__(self, path, s3_path, saved_path):
        self.path = path
        self.s3_path = s3_path
        self.saved_path = saved_path

    def unzip_folder(self):
       shutil.unpack_archive(self.path, self.saved_path)

    def save_files_to_s3(self, connection):
        s3.Bucket


class Transform_data:
    def __init__(self):
        pass

    def get_list_of_files(self):
        pass

    def transform_file(self):
        pass

class connection_to_s3:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def connect_s3(self):
        session = boto3.Session(
            aws_access_key_id = aws_cred["aws_access_key_id"],
            aws_secret_access_key = aws_cred["aws_secret_access_key"]
        )

        s3 = session.resource('s3')
        bucket = s3.Bucket(self.bucket_name)


if __name__ == "__main__":
    connection = connection_to_s3(bucket_name)
    connection.connect_s3()
    upload = Upload_Manager(path=path, s3_path=s3_path, saved_path=saved_path)
    upload.unzip_folder()
    print("completed")