# Basic s3 setup

### 

Make a directory and pipenv boto3

```
mkdir projectname && cd projectname
pipenv install boto3 --python 3.7
```

Make sure you have boto3 install using pip freeze
```
pipenv shell
pipfreeze
```

Make a file called connect.py
```
touch connect.py
```

Connect to s3 through boto3 using connect.py
```python
import boto3

client = boto3.client('s3')
```

Setup credentials by adding aws access key, secret key, and region to the connect.py file
```python
AWS_ACCESS_KEY_ID =  '<access_key>'
AWS_SECRET_ACCESS_KEY = '<secrete_key'
AWS_DEFAULT_REGION = 'us-east-1'
```

Add in the credential variables to boto3
```python
client = boto3.client('s3'
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)
```

run `python connect.py` in the command line and you should get a json with the response metadata

Update the policy in aws group permissions. 

### Interact with the aws session

Go into connect.py and add the following code. You should see all your buckets listed below the client data.

```python
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

s3 = session.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)
```

### List objects within the bucket

Update the policy in the groups you created to:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets"
            ],
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::your-bucket-name"
        }
    ]
}
```

### Upload file to bucket

Use the same access information to setup the session.

```python
import os
import sys
import threading
import boto3

BASE_DIR = os.getcwd()
IMAGE_DIR = os.path.join(BASE_DIR, 'images')

AWS_ACCESS_KEY_ID =  '<access-key>'
AWS_SECRET_ACCESS_KEY = '<secrete-key>'
AWS_DEFAULT_REGION = 'us-east-1'
AWS_BUCKET_NAME = '<bucket-name>'

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION
)

s3 = session.resource('s3')
```

Define the bucket name and establish the file path to the file you want to upload.

```python
bucket = s3.Bucket(name=AWS_BUCKET_NAME)

file_path = os.path.join(IMAGE_DIR, 'aws.png')
key_name = 'aws.png'
```

Add in a progress percentage class to check the percentage of upload.

```python
class ProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()
    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()
```

Here are a couple ways to upload files to your aws bucket.

```python
bucket.upload_file(file_path, 'aws.png', Callback=ProgressPercentage(file_path))
```

```python
with open(file_path, 'rb') as data:
    bucket.upload_fileobj(
        data,
        'aws.png',
        Callback=ProgressPercentage(file_path)
    )
```

```python
with open(file_path, 'rb') as data:
    bucket.put_object(
        ACL='public-read',
        Body=data,
        Key='1-aws.png'
    )
```









