import boto3

def count_of_buckets():
    # count number of buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    number_of_buckets = len(response['Buckets'])
    return number_of_buckets


