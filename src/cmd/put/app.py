import json
import os
from datetime import datetime

import boto3


def handler(_event, _context):
    client = boto3.client("s3")

    key = f"sample-{datetime.timestamp(datetime.now())}.json"
    client.put_object(
        Body=json.dumps({"message": "sample"}).encode("utf-8"),
        Bucket=os.getenv("BUCKET_NAME"),
        Key=key,
    )

    return {
        "statusCode": 200,
        "body": json.dumps("Put S3 Object"),
        "key": key,
    }
