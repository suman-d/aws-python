

import tempfile
import boto3
from PIL import Image
from chalice import Chalice

app = Chalice(app_name='chalice_image_thumbnails', debug=True)
s3_client = boto3.client('s3')

@app.on_s3_event(bucket='mydemoimgbucket',
                 suffix='.jpg')
def resize_image(event):
    app.log.debug("Resizing the image from s3://%s/%s",
                  event.bucket, event.key)
    with tempfile.NamedTemporaryFile('w') as f:
        s3_client.download_file(event.bucket, event.key, f.name)
        resized_file = f.name + '.thumbnail.jpg'
        with Image.open(f.name) as image:
            image.thumbnail((256,256))
            image.save(resized_file)
        s3_client.upload_file(
            Filename=resized_file,
            Bucket='mydemothumbnailbucket',
            Key=resized_file.rsplit("/", 1)[-1]
        )