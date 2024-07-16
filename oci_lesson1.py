import os
from oci.identity import IdentityClient
key_content = os.environ.get('KEY_CONTENT')

config = {
    "user": os.environ.get('USER'),
    "key_content": os.environ.get('KEY_CONTENT'),
    "fingerprint": os.environ.get('FINGERPRINT'),
    "tenancy": os.environ.get('TENANCY'),
    "region": os.environ.get('REGION')
}

identity = IdentityClient(config)

tenancy = config['tenancy']

comp_list = identity.list_compartments(tenancy,compartment_id_in_subtree=True).data

print(comp_list)

