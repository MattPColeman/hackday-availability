import boto3
import json
import pandas as pd


def get_s3_data():
    print('Downloading files from S3 bucket...')
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('team-avocado-test-bucket')

    for o in bucket.objects.filter(Delimiter='/'):
        print(o)

    # s3.download_file('team-avocado-test-bucket', 'OBJECT_NAME', 'FILE_NAME')


def main():
    print('\n######################################################\n##                Availabil' +
          'ity hack:                ##\n######################################################\n')
    get_s3_data()


if __name__ == '__main__':
    main()
