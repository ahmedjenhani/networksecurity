
"""
import os


class S3Sync:
    def sync_folder_to_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync {Artifacts} {aws_bucket_url} "
        os.system(command)

    def sync_folder_from_s3(self,folder,aws_bucket_url):
        command = f"aws s3 sync  {aws_bucket_url} {Artifacts} "
        os.system(command)   """


import os

class GCSync:
    def sync_folder_to_gcs(self, folder, https://storage.cloud.google.com/{itbsml}/{ITBSMLPROJET}):
        command = f"gsutil -m rsync -r {Artifacts} {"https://storage.cloud.google.com/{itbsml}/{ITBSMLPROJET}"}
        os.system(command)

    def sync_folder_from_gcs(self, folder, https://storage.cloud.google.com/{itbsml}/{ITBSMLPROJET}):
        command = f"gsutil -m rsync -r https://storage.cloud.google.com/{itbsml}/{ITBSMLPROJET} {Artifacts}"
        os.system(command)

        """https://storage.cloud.google.com/{itbsml}/{ITBSMLPROJET/}"""