import os
from storages.backends.azure_storage import AzureStorage
# from keyvault import secret_1\
class AzureMediaStorage(AzureStorage):
    account_name = 'cases1967' # <storage_account_name>
    account_key = "LLGNzoU4NTehiEcVFPKxPAmYhd7oaFR59p04N+d1tK9y2giVpBtmE2f0+nwuJ+u9UB2eA4jtbi8S+AStsddylw=="# <storage_account_key>
    azure_container = 'cases'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'cases1967' # <storage_account_name>
    account_key = "LLGNzoU4NTehiEcVFPKxPAmYhd7oaFR59p04N+d1tK9y2giVpBtmE2f0+nwuJ+u9UB2eA4jtbi8S+AStsddylw==" # <storage_account_key>
    azure_container = 'cases'
    expiration_secs = None

