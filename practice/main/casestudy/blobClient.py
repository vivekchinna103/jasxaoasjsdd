from datetime import datetime, timedelta
from typing import Container
from azure.storage.blob import BlobServiceClient, ContainerClient,generate_account_sas, AccountSasPermissions, ResourceTypes
from django.http import HttpResponse
import os,io
from dotenv import load_dotenv
load_dotenv()

# Get the Azure Storage account name and key from environment variables
#account_name = 'casestudystgacc'
#account_key = '91mplEP2wv9FNDa0Q2xe+2sFZlDz0If0lR4thVNHZvSg/3bfqcudc22m8L/KnG35kLf63VkS9bvk+AStjAqXtw=='

account_name="cases1967"
account_key="LLGNzoU4NTehiEcVFPKxPAmYhd7oaFR59p04N+d1tK9y2giVpBtmE2f0+nwuJ+u9UB2eA4jtbi8S+AStsddylw=="
account_url=f"https://{account_name}.blob.core.windows.net"
# Create a BlobServiceClient object
blob_service_client = BlobServiceClient(account_url, credential=account_key)


def get_url(blob):
    sas_token = create_account_sas()
    if not account_name:
        raise Exception('Azure storage account not found!')
    if not sas_token:
        raise Exception("Azure Storage accountkey not found!")
    blob_service_client = BlobServiceClient(account_url=account_url, credential=sas_token)
    container_name = 'cases'
    blob_name=blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    
    return blob_client.url


def create_account_sas():
    # Set the SAS token options

# Configure the SAS token options
    sas_options = {
#'services': AccountSasServices(blob=True, table=True, queue=True, file=True),
    'resource_types': ResourceTypes(object=True, container=True, service=True),
    'permissions': AccountSasPermissions(read=True, write=True, delete=True, list=True, add=True, create=True, update=True, process=True),
    'start': datetime.utcnow(),
    'expiry': datetime.utcnow() + timedelta(minutes=10),
    }

# Generate the SAS token
    sas_token = generate_account_sas(
      account_name=blob_service_client.account_name,
      account_key=blob_service_client.credential.account_key,
        resource_types=sas_options['resource_types'],
      #services=sas_options['services'],
     permission=sas_options['permissions'],
     start=sas_options['start'],
     expiry=sas_options['expiry'],
       )
    if sas_token[0]=="?":
        return sas_token
    else:
        return "?"+str(sas_token)
# Print the SAS token
    #print(sas_token)

def upload(file,file_name):
    sas_token=create_account_sas()
    if not account_name:
        raise Exception('Azure storage account not found!')
    if not sas_token:
        raise Exception("Azure Storage accountkey not found!")
    blob_service_client=BlobServiceClient(account_url=account_url, credential=sas_token)
    container_name="cases"
    container_client=ContainerClient(account_url=account_url,container_name=container_name)
    stream=io.Bytes(file.buffer)
    stream_length=len(file.buffer)
    block_blob_client=container_client.get_blob_client(file_name)
    block_blob_client.upload_blob(stream)



def download(file):
    sas_token=create_account_sas()
    if not account_name:
        raise Exception('Azure storage account not found!')
    if not sas_token:
        raise Exception("Azure Storage accountkey not found!")
    blob_service_client=BlobServiceClient(account_url=account_url, credential=sas_token)
    container_name="cases"
    container_client=ContainerClient(account_url=account_url,container_name=container_name)
    block_blob_client= container_client.get_blob_client(file)
    return block_blob_client.download_blob(offset=0)