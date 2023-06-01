from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexerClient
from azure.search.documents.indexes.models import  IndexingParameters,SearchIndexer
#from azure.search.documents import odata
# Azure Cognitive Search endpoint and admin key
endpoint = 'https://dlpractice.search.windows.net'
admin_key = '37jMB2DPlxnGcEbeDnB66vlnXpbOwCFSJVOU7yU8uPAzSeA66uzd'

# Define the data source
#data_source_name = 'dlpractice'
#connection_string = 'Driver={ODBC Driver 18 for SQL Server};Server=tcp:dlpractice.database.windows.net,1433;Database=DL-practice;Uid=admin123;Pwd="Admin@123";Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
#data_source = DataSource(
  #  name=data_source_name,
   # type='azuresql',
   #connection_string=connection_string
#)

# Define the index


# Define the indexer
indexer_name = 'vivekdlcasestudyindexer'
indexer = SearchIndexer(
    name=indexer_name,
    data_source_name="dlpractice",
    target_index_name="dlcasestudynew"

)

# Create the indexer
credential = AzureKeyCredential(admin_key)
indexer_client = SearchIndexerClient(endpoint=endpoint, credential=credential)
indexer_client.create_indexer(indexer)
