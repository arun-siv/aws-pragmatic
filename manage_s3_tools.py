import boto3

import click

def count_of_buckets():
    # count number of buckets
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    number_of_buckets = len(response['Buckets'])
    return number_of_buckets

# write a function that returns list of empty buckets
def list_of_empty_buckets():
    s3 = boto3.client('s3')
    response = s3.list_buckets()
    empty_buckets = []
    for bucket in response['Buckets']:
        # check if bucket is empty
        response = s3.list_objects_v2(Bucket=bucket['Name'])
        if response['KeyCount'] == 0:
            empty_buckets.append(bucket['Name'])
    return empty_buckets

# create a click group
@click.group()
def cli():
    pass

# create a click subcommand
@cli.command("count_buckets")
def count_buckets():
    """Count the number of buckets"""
    print(f"Number of buckets: {count_of_buckets()}")


# create click command find-empty-buckets
@cli.command("find-empty-buckets")
def find_empty_buckets():
    """Find empty buckets"""
    print(f"Empty buckets: {list_of_empty_buckets()}")

if __name__ == "__main__":
    cli()