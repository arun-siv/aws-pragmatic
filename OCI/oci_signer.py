import os

config = {
    "user": os.environ.get('USER'),
    "key_content": os.environ.get('KEY_CONTENT'),
    "fingerprint": os.environ.get('FINGERPRINT'),
    "tenancy": os.environ.get('TENANCY'),
    "region": os.environ.get('REGION')
}

## update the config to fn context oci.profile

print(config)
