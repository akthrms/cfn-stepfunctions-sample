import json
import os

import boto3


def handler(event, _context):
    key = event["key"]

    client = boto3.client("s3")

    client.delete_object(
        Bucket=os.getenv("BUCKET_NAME"),
        Key=key,
    )

    return {
        "statusCode": 200,
        "body": json.dumps("Delete S3 Object"),
    }
