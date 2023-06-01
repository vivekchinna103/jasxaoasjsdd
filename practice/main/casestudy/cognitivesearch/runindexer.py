from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexerClient
from azure.search.documents.indexes.models import  IndexingParameters,SearchIndexer
#from azure.search.documents import odata
# Azure Cognitive Search endpoint and admin key
endpoint = 'https://dlpractice.search.windows.net'
admin_key = '37jMB2DPlxnGcEbeDnB66vlnXpbOwCFSJVOU7yU8uPAzSeA66uzd'
def runindexer():
    credential = AzureKeyCredential(admin_key)
    indexer_client = SearchIndexerClient(endpoint=endpoint, credential=credential)
    indexer_client.run_indexer()