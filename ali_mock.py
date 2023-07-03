import os
from alicloud_credentials import AccessKeyCredentials
from alicloud_sdk_core.client import AcsClient

# Read Alicloud credentials from environment variables
access_key_id = os.environ['ALICLOUD_ACCESS_KEY_ID']
access_key_secret = os.environ['ALICLOUD_ACCESS_KEY_SECRET']
region_id = os.environ['ALICLOUD_REGION']

# Create Alicloud client using the mocked credentials
credentials = AccessKeyCredentials(access_key_id, access_key_secret)
client = AcsClient(credentials, region_id)
