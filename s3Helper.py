import boto3


def listbuckets():
    # ec2 = boto3.client('ec2')

    session = boto3.Session(profile_name="veena")
    s3 = session.client("s3")
    '''
    s3 = boto3.client('s3',
                      aws_access_key_id='your_access_key_id',
                      aws_secret_access_key='your_secret_access_key'
                      )
    '''
    response = s3.list_buckets()
    for bucket in response["Buckets"]:
        print bucket["Name"]


def createbucket():
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket="haritestabc12345")
    print response


def uploadfiletobucket():
    s3 = boto3.client('s3')
    sourcefile = "c://temp/test.txt"
    bucket_name = "haritestabc12345"
    objectname = "test1/test2/test_python.txt"

    s3.upload_file(sourcefile, bucket_name, objectname)


def uploadfiletobucketusingread():
    s3 = boto3.client('s3')
    # sourcefile = "c://temp/test.txt"
    bucket_name = "haritestabc12345"
    objectname = "test1/test2/test_python.txt"

    with open("c://temp/test.txt", "rb") as data:
        s3.upload_file(data, bucket_name, objectname)


if __name__ == '__main__':
    listbuckets()
